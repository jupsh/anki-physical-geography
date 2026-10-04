"""Natural Earth data (public domain), downloaded once into build/natural_earth/.

Feature sources used by the content modules:

    Region("HIMALAYAS")                   # ne_10m_geography_regions_polys, matched on NAME
    Lake("Baikal")                        # ne_10m_lakes, matched on name / name_en
    River("Nile", "White Nile", ...)      # ne_10m_rivers_lake_centerlines, all segments with these names

`within=(west, south, east, north)` keeps only geometry whose bbox centre is inside that box,
for names that occur more than once (e.g. the Colorado in Texas vs. the one in Arizona).
`exclude=(west, south, east, north)` drops river segments whose centre is inside it, for
mislabelled segments (Natural Earth names part of the Snake "Columbia").
"""

import json
import math
import re
import urllib.request
from dataclasses import dataclass
from functools import cache
from pathlib import Path

NE_VERSION = "v5.1.2"
NE_URL = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/{}/geojson/{}.geojson"
CACHE = Path(__file__).resolve().parent.parent / "build" / "natural_earth"


@cache
def load(name):
    path = CACHE / f"{name}.geojson"
    if not path.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        url = NE_URL.format(NE_VERSION, name)
        print(f"downloading {url}")
        with urllib.request.urlopen(url) as r:
            path.write_bytes(r.read())
    return json.loads(path.read_text())["features"]


def _norm(s):
    return re.sub(r"\s+", " ", (s or "")).strip().casefold()


def polygons(geom):
    """GeoJSON geometry -> list of polygons, each a list of rings [(lon, lat), ...]."""
    t, c = geom["type"], geom["coordinates"]
    if t == "Polygon":
        return [c]
    if t == "MultiPolygon":
        return list(c)
    raise ValueError(t)


def lines(geom):
    t, c = geom["type"], geom["coordinates"]
    if t == "LineString":
        return [c]
    if t == "MultiLineString":
        return list(c)
    raise ValueError(t)


def _centre(pts):
    lons = [p[0] for p in pts]
    lats = [p[1] for p in pts]
    return (min(lons) + max(lons)) / 2, (min(lats) + max(lats)) / 2


def _inside(pts, box):
    if box is None:
        return True
    lon, lat = _centre(pts)
    w, s, e, n = box
    return w <= lon <= e and s <= lat <= n


@dataclass(frozen=True)
class Region:
    name: str
    within: tuple | None = None

    def shapes(self):
        polys = [p for f in load("ne_10m_geography_regions_polys")
                 if _norm(f["properties"]["NAME"]) == _norm(self.name)
                 for p in polygons(f["geometry"]) if _inside(p[0], self.within)]
        if not polys:
            raise SystemExit(f"region not found: {self.name}")
        return "area", polys


@dataclass(frozen=True)
class Lake:
    name: str
    within: tuple | None = None

    def shapes(self):
        want = _norm(self.name)
        polys = [p for f in load("ne_10m_lakes")
                 if want in (_norm(f["properties"]["name"]), _norm(f["properties"]["name_en"]))
                 for p in polygons(f["geometry"]) if _inside(p[0], self.within)]
        if not polys:
            raise SystemExit(f"lake not found: {self.name}")
        first = polys[0][0][0]
        if any(_km(first, p[0][0]) > 800 for p in polys):
            raise SystemExit(f"lake {self.name}: matches lakes far apart; use within=(w, s, e, n)")
        return "lake", polys


class River:
    def __init__(self, *names, within=None, exclude=None):
        self.names = names
        self.within = within
        self.exclude = exclude

    def shapes(self):
        want = {_norm(n) for n in self.names}
        found, segs = set(), []
        for f in load("ne_10m_rivers_lake_centerlines"):
            p = f["properties"]
            hit = want & {_norm(p["name"]), _norm(p["name_en"])}
            if not hit or f["geometry"] is None:
                continue
            new = [ln for ln in lines(f["geometry"]) if _inside(ln, self.within)
                   and not (self.exclude and _inside(ln, self.exclude))]
            if new:
                found |= hit
                segs += new
        if missing := want - found:
            raise SystemExit(f"river segments not found: {sorted(missing)}")
        _check_connected(self.names, segs)
        return "river", segs


def _km(a, b):
    la1, la2 = math.radians(a[1]), math.radians(b[1])
    h = (math.sin((la2 - la1) / 2) ** 2
         + math.cos(la1) * math.cos(la2) * math.sin(math.radians(b[0] - a[0]) / 2) ** 2)
    return 2 * 6371 * math.asin(math.sqrt(h))


def _check_connected(names, segs, gap_km=150):
    """Catch same-named rivers elsewhere: every segment must end near another segment."""
    segs = [seg for seg in segs if sum(_km(a, b) for a, b in zip(seg, seg[1:])) > 20]  # skip stubs
    if len(segs) < 2:
        return
    ends = [(seg[0], seg[-1]) for seg in segs]
    for i, (a, b) in enumerate(ends):
        others = [p for j, e in enumerate(ends) if j != i for p in e]
        if min(_km(p, q) for p in (a, b) for q in others) > gap_km:
            raise SystemExit(f"river {names}: segment near ({a[0]:.1f}, {a[1]:.1f}) is cut off "
                             "from the rest; use within=(w, s, e, n)")
