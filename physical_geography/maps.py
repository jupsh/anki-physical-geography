"""Locator maps in the style of Ultimate Geography's maps.

Each map is a Lambert azimuthal equal-area projection centred on the feature, so shapes stay
true at any latitude and nothing tears at the antimeridian. Land, lakes, borders and coasts come
from Natural Earth 1:50m; the highlighted feature from 1:10m. Unlike UG, the maps also show major
rivers and the states/provinces of the largest countries, faintly, as landmarks. A small world locator sits in
whichever corner the feature leaves free.

Geometry is clipped in lon/lat to a box around the view before projecting. That keeps the far
side of the globe (where the projection blows up near the antipode) out of the picture.
"""

import io
import math

from geodata import lines, load, polygons

W = 1000  # px; height is 562 (16:9, like UG) unless the feature is tall, then up to square
H_MIN, H_MAX = 562, 1000

LAND = "#fdfbe5"
WATER = "#b3dff5"
BORDER = "#656565"
COAST = "#1178ac"
HI_LAND = "#c12838"
HI_WATER = "#4790c8"
RIVER = "#1d5f99"
FAINT_RIVER = "#8cc3e3"
STATE = "#cbc8b4"
INSET_BG = "#f8f9fa"
INSET_LAND = "#cecece"
INSET_EDGE = "#9ca3af"

R_KM = 6371.0
MARGIN = 0.125  # fraction of the feature's size added on each side ...
MARGIN_KM = (600, 450)  # ... or at least this much (x, y), whichever is larger
MIN_SPAN_KM = 2600  # narrowest map width, so small features keep their context
MAX_REACH = 100  # degrees: no part of a map may be further than this from its centre


# --------------------------------------------------------------------------- projection

class LAEA:
    def __init__(self, lon0, lat0):
        self.lon0 = lon0
        self.p0 = math.radians(lat0)
        self.sin0, self.cos0 = math.sin(self.p0), math.cos(self.p0)

    def fwd(self, rlon, lat):
        """Project (lon relative to lon0, lat) in degrees to unit-sphere x, y."""
        l, p = math.radians(rlon), math.radians(lat)
        sp, cp, cl = math.sin(p), math.cos(p), math.cos(l)
        d = 1 + self.sin0 * sp + self.cos0 * cp * cl
        k = math.sqrt(2 / d) if d > 1e-12 else 2.0
        return k * cp * math.sin(l), k * (self.cos0 * sp - self.sin0 * cp * cl)

    def inv(self, x, y):
        """Inverse: unit-sphere x, y -> (lon relative to lon0, lat) in degrees."""
        rho = math.hypot(x, y)
        if rho < 1e-12:
            return 0.0, math.degrees(self.p0)
        c = 2 * math.asin(min(1.0, rho / 2))
        sc, cc = math.sin(c), math.cos(c)
        lat = math.asin(cc * self.sin0 + y * sc * self.cos0 / rho)
        lon = math.atan2(x * sc, rho * self.cos0 * cc - y * self.sin0 * sc)
        return math.degrees(lon), math.degrees(lat)


def rel(lon, lon0):
    return (lon - lon0 + 180) % 360 - 180


def unwrap(pts, lon0):
    """Coordinates relative to lon0, kept continuous along the ring (may leave [-180, 180])."""
    out, prev = [], None
    for lon, lat, *_ in pts:
        r = rel(lon, lon0)
        if prev is not None:
            while r - prev > 180:
                r -= 360
            while r - prev < -180:
                r += 360
        out.append((r, lat))
        prev = r
    return out


# --------------------------------------------------------------------------- clipping

def clip_ring(ring, box):
    """Sutherland-Hodgman clip of a closed ring to box = (w, s, e, n); None = no limit."""
    w, s, e, n = box
    planes = [(0, w, 1), (0, e, -1), (1, s, 1), (1, n, -1)]
    pts = ring
    for axis, val, sign in planes:
        if val is None or not pts:
            continue
        out = []
        for i, cur in enumerate(pts):
            prev = pts[i - 1]
            cin = (cur[axis] - val) * sign >= 0
            pin = (prev[axis] - val) * sign >= 0
            if cin != pin:
                t = (val - prev[axis]) / (cur[axis] - prev[axis])
                out.append((prev[0] + t * (cur[0] - prev[0]), prev[1] + t * (cur[1] - prev[1])))
            if cin:
                out.append(cur)
        pts = out
    return pts


def clip_line(line, box):
    """Split a polyline into the runs inside box, keeping one point either side of each run."""
    w, s, e, n = box

    def inside(p):
        return ((w is None or p[0] >= w) and (e is None or p[0] <= e)
                and (s is None or p[1] >= s) and (n is None or p[1] <= n))

    runs, cur = [], []
    for i, p in enumerate(line):
        if inside(p):
            if not cur and i > 0:
                cur.append(line[i - 1])
            cur.append(p)
        elif cur:
            cur.append(p)
            runs.append(cur)
            cur = []
    if cur:
        runs.append(cur)
    return runs


# --------------------------------------------------------------------------- view

class View:
    """A projection plus a pixel window onto it."""

    def __init__(self, seqs, zoom=1.0, span=None, center=None):
        """seqs: the feature's point sequences (rings or lines), which the view is fitted to."""
        pts = [p for seq in seqs for p in seq]
        if center is None:
            center = _centroid(pts)
        self.lon0, self.lat0 = center
        self.proj = LAEA(self.lon0, self.lat0)
        xy = [self.proj.fwd(*p) for p in unwrap(pts, self.lon0)]
        xs, ys = [p[0] for p in xy], [p[1] for p in xy]
        cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
        fw, fh = max(xs) - min(xs), max(ys) - min(ys)
        w = max(fw * (1 + 2 * MARGIN), fw + 2 * MARGIN_KM[0] / R_KM)
        h = max(fh * (1 + 2 * MARGIN), fh + 2 * MARGIN_KM[1] / R_KM)
        self.h = round(min(H_MAX, max(H_MIN, W * h / max(w, MIN_SPAN_KM / R_KM))))
        w = span / R_KM if span else max(w, h * W / self.h, MIN_SPAN_KM / R_KM) * zoom
        self.scale = W / w  # px per unit
        self.x0 = cx - W / 2 / self.scale
        self.y1 = cy + self.h / 2 / self.scale
        reach = max(math.degrees(2 * math.asin(min(1.0, math.hypot(*self.unpx(X, Y)) / 2)))
                    for X in (0, W) for Y in (0, self.h))
        if reach > MAX_REACH:
            raise SystemExit(f"map around {center} reaches {reach:.0f} degrees from its centre")
        self.box = self._latlon_box()

    def px(self, x, y):
        return (x - self.x0) * self.scale, (self.y1 - y) * self.scale

    def unpx(self, X, Y):
        return self.x0 + X / self.scale, self.y1 - Y / self.scale

    def border(self, n=60):
        """Points around the edge of the window, as (lon relative to lon0, lat)."""
        H = self.h
        edge = ([(W * i / n, 0) for i in range(n)] + [(W, H * i / n) for i in range(n)]
                + [(W - W * i / n, H) for i in range(n)] + [(0, H - H * i / n) for i in range(n)])
        return [self.proj.inv(*self.unpx(X, Y)) for X, Y in edge]

    def _latlon_box(self):
        b = self.border()
        lats = [p[1] for p in b]
        s, n = max(-90, min(lats) - 4), min(90, max(lats) + 4)
        for pole in (90, -90):
            X, Y = self.px(*self.proj.fwd(0, pole))
            if 0 <= X <= W and 0 <= Y <= self.h:
                # a pole is in view: every longitude is, too
                return (None, -90 if pole < 0 else s, None, 90 if pole > 0 else n)
        lons = [p[0] for p in b]
        return (min(lons) - 6, s, max(lons) + 6, n)

    def _variants(self, pts):
        """The unwrapped point list, shifted by whole turns to wherever it meets the box."""
        u = unwrap(pts, self.lon0)
        w, _, e, _ = self.box
        if w is None:
            return [u]
        lo, hi = min(p[0] for p in u), max(p[0] for p in u)
        return [[(x + k, y) for x, y in u] for k in (-360, 0, 360) if lo + k <= e and hi + k >= w]

    def _path(self, pts, close):
        out, last = [], None
        for p in _densify(pts, close):
            X, Y = self.px(*self.proj.fwd(*p))
            if last and abs(X - last[0]) < 0.6 and abs(Y - last[1]) < 0.6:
                continue
            out.append(f"{X:.1f} {Y:.1f}")
            last = (X, Y)
        if len(out) < 2:
            return ""
        return "M" + "L".join(out) + ("Z" if close else "")

    def poly_path(self, polys):
        parts = []
        for poly in polys:
            for ring in poly:
                for v in self._variants(ring):
                    c = clip_ring(v, self.box)
                    if len(c) >= 3:
                        parts.append(self._path(c, True))
        return "".join(parts)

    def line_path(self, lns):
        parts = []
        for ln in lns:
            for v in self._variants(ln):
                for run in clip_line(v, self.box):
                    parts.append(self._path(run, False))
        return "".join(parts)

    def pixels(self, seqs):
        return [self.px(*self.proj.fwd(*p)) for seq in seqs for p in unwrap(seq, self.lon0)]


def _densify(pts, close, step=0.5):
    """Add points along long edges (in degrees), so that edges created by clipping, which run
    along a parallel or meridian, curve with it once projected instead of cutting a chord."""
    out = []
    n = len(pts)
    for i in range(n if close else n - 1):
        a, b = pts[i], pts[(i + 1) % n]
        out.append(a)
        k = int(max(abs(b[0] - a[0]), abs(b[1] - a[1])) / step)
        out += [(a[0] + (b[0] - a[0]) * j / (k + 1), a[1] + (b[1] - a[1]) * j / (k + 1))
                for j in range(1, k + 1)]
    if not close and pts:
        out.append(pts[-1])
    return out


def _centroid(pts):
    x = y = z = 0.0
    for lon, lat, *_ in pts:
        l, p = math.radians(lon), math.radians(lat)
        x += math.cos(p) * math.cos(l)
        y += math.cos(p) * math.sin(l)
        z += math.sin(p)
    return math.degrees(math.atan2(y, x)), math.degrees(math.atan2(z, math.hypot(x, y)))


# --------------------------------------------------------------------------- layers

def _all_polys(name):
    return [p for f in load(name) for p in polygons(f["geometry"])]


def _all_lines(name):
    return [ln for f in load(name) if f["geometry"] for ln in lines(f["geometry"])]


def base_layers(v):
    out = [f'<rect width="{W}" height="{v.h}" fill="{WATER}"/>']
    out.append(f'<path d="{v.poly_path(_all_polys("ne_50m_land"))}" fill="{LAND}"/>')
    return out


def water_layers(v):
    return [f'<path d="{v.poly_path(_all_polys("ne_50m_lakes"))}" fill="{WATER}" '
            f'stroke="{COAST}" stroke-width="0.9"/>']


def line_layers(v):
    """Context lines: states/provinces of the largest countries and major rivers (both faint,
    since UG's maps have neither), then country borders and coasts."""
    rivers = [ln for f in load("ne_50m_rivers_lake_centerlines")
              if f["geometry"] and f["properties"]["scalerank"] <= 5 for ln in lines(f["geometry"])]
    return [
        f'<path d="{v.line_path(_all_lines("ne_50m_admin_1_states_provinces_lines"))}" fill="none" '
        f'stroke="{STATE}" stroke-width="0.7" stroke-linejoin="round"/>',
        f'<path d="{v.line_path(rivers)}" fill="none" stroke="{FAINT_RIVER}" stroke-width="1" '
        f'stroke-linejoin="round"/>',
        f'<path d="{v.line_path(_all_lines("ne_50m_admin_0_boundary_lines_land"))}" fill="none" '
        f'stroke="{BORDER}" stroke-width="1" stroke-linejoin="round"/>',
        f'<path d="{v.line_path(_all_lines("ne_50m_coastline"))}" fill="none" '
        f'stroke="{COAST}" stroke-width="1" stroke-linejoin="round"/>',
    ]


# --------------------------------------------------------------------------- inset

IW, IH = 230, 118  # locator ellipse


def _inset_xy(lon, lat, cx, cy):
    a, b = IW / 2 - 2, IH / 2 - 2
    k = math.sqrt(max(0.0, 1 - (lat / 90) ** 2))
    return cx + a * lon / 180 * k, cy - b * lat / 90


def inset(v, corner):
    m = 12
    cx = m + IW / 2 if corner[0] == "l" else W - m - IW / 2
    cy = m + IH / 2 if corner[1] == "t" else v.h - m - IH / 2
    border = [(rel(lon + v.lon0, 0), lat) for lon, lat in v.border(30)]
    lons = [p[0] for p in border]
    c0 = 180 if max(lons) - min(lons) > 180 else 0  # view straddles the antimeridian
    out = [f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{IW / 2}" ry="{IH / 2}" fill="{INSET_BG}" '
           f'stroke="{INSET_EDGE}" stroke-width="1"/>']
    d = []
    for poly in _all_polys("ne_110m_land"):
        for ring in poly:
            for k in (-360, 0, 360):
                u = [(x + k, y) for x, y in unwrap(ring, c0)]
                c = clip_ring(u, (-180, -90, 180, 90))
                if len(c) >= 3:
                    d.append("M" + "L".join("%.1f %.1f" % _inset_xy(x, y, cx, cy) for x, y in c) + "Z")
    out.append(f'<path d="{"".join(d)}" fill="{INSET_LAND}"/>')
    if v.box[0] is None:  # a pole is in view: mark the whole polar cap
        s, n = v.box[1], v.box[3]
        edge = n if s == -90 else s
        pole = -90 if s == -90 else 90
        steps = [edge + (pole - edge) * i / 10 for i in range(11)]
        box = ([(x, edge) for x in range(-180, 181, 10)] + [(180, y) for y in steps]
               + [(-180, y) for y in reversed(steps)])
    else:
        box = unwrap(border, c0)
    pts = "L".join("%.1f %.1f" % _inset_xy(x, y, cx, cy) for x, y in box)
    out.append(f'<path d="M{pts}Z" fill="none" stroke="{HI_LAND}" stroke-width="1.8"/>')
    return out


def _corner(pixels, H):
    def hits(c):
        x0 = 0 if c[0] == "l" else W - IW - 24
        y0 = 0 if c[1] == "t" else H - IH - 24
        return sum(x0 <= X <= x0 + IW + 24 and y0 <= Y <= y0 + IH + 24 for X, Y in pixels)
    return min(("lb", "rb", "lt", "rt"), key=hits)


# --------------------------------------------------------------------------- render

def render_svg(source, zoom=1.0, span=None, center=None):
    kind, shapes = source.shapes()
    seqs = shapes if kind == "river" else [ring for poly in shapes for ring in poly]
    v = View(seqs, zoom=zoom, span=span, center=center)
    out = base_layers(v)
    if kind == "area":
        out.append(f'<path d="{v.poly_path(shapes)}" fill="{HI_LAND}" fill-opacity="0.85" '
                   f'fill-rule="evenodd"/>')
    out += water_layers(v)
    if kind == "lake":
        out.append(f'<path d="{v.poly_path(shapes)}" fill="{HI_WATER}" stroke="{COAST}" '
                   f'stroke-width="1" fill-rule="evenodd"/>')
    out += line_layers(v)
    if kind == "river":
        out.append(f'<path d="{v.line_path(shapes)}" fill="none" stroke="{RIVER}" stroke-width="3.6" '
                   f'stroke-linecap="round" stroke-linejoin="round"/>')
    pix = [p for p in v.pixels(seqs) if 0 <= p[0] <= W and 0 <= p[1] <= v.h]
    if pix:
        xs, ys = [p[0] for p in pix], [p[1] for p in pix]
        size = max(max(xs) - min(xs), max(ys) - min(ys))
        if size < 30:  # too small to spot: ring it, as UG does for small countries
            colour = HI_LAND if kind == "area" else RIVER
            out.append(f'<circle cx="{(min(xs) + max(xs)) / 2:.1f}" cy="{(min(ys) + max(ys)) / 2:.1f}" '
                       f'r="{size / 2 + 16:.1f}" fill="none" stroke="{colour}" stroke-width="2.5"/>')
    out += inset(v, _corner(pix, v.h))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{v.h}" '
            f'viewBox="0 0 {W} {v.h}">' + "".join(out) + "</svg>")


def render_png(source, **view):
    import cairosvg
    from PIL import Image

    png = cairosvg.svg2png(bytestring=render_svg(source, **view).encode())
    im = Image.open(io.BytesIO(png)).convert("RGB").quantize(colors=128, method=Image.Quantize.FASTOCTREE)
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    return buf.getvalue()
