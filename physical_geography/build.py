"""Build the Physical Geography Anki deck (a companion to Ultimate Geography).

    uv run python physical_geography/build.py            # -> dist/Physical_Geography.apkg
    uv run python physical_geography/build.py --html X   # also write an HTML preview of every note

Maps are rendered from Natural Earth data (downloaded on first run) and cached in
build/physical_geography/, keyed on the feature's source and the renderer's code.
"""

import argparse
import hashlib
import importlib
import re
import sys
from pathlib import Path

import genanki

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

import maps  # noqa: E402

ROOT = HERE.parent
BUILD = ROOT / "build" / "physical_geography"
DIST = ROOT / "dist"
DECK_ROOT = "Physical Geography"
MODULES = ["content.rivers", "content.mountains", "content.deserts", "content.lakes",
           "content.lands", "content.peninsulas"]

MODEL_ID = 1730418265

CSS = r"""
.card {
  font-family: -apple-system, "Segoe UI", Inter, Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 20px; line-height: 1.5; color: #1f2937; background: #fafaf9;
  text-align: center; margin: 0; padding: 0;
}
.wrap { max-width: 760px; margin: 0 auto; padding: 18px 14px 28px; }
.kind {
  font-size: 12px; font-weight: 600; letter-spacing: .06em; text-transform: uppercase;
  color: #b91c1c; margin-bottom: 12px;
}
.kind .regions { color: #6b7280; }
.map img {
  max-width: 100%; height: auto; box-sizing: border-box; border-radius: 10px;
  border: 1px solid #e5e7eb;
}
.map { margin: 6px 0 14px; }
/* Name → Map back: the feature's highlight, a transparent overlay, laid over the blank map */
.stack { position: relative; display: inline-block; vertical-align: top; }
.stack img { display: block; }
.stack img + img {
  position: absolute; left: 0; top: 0; width: 100%; height: 100%;
  border-color: transparent !important;
}
.prompt { color: #6b7280; font-size: .9em; }
.name { font-size: 1.6em; font-weight: 650; margin: 4px 0 8px; }
.q { font-size: 1.1em; font-weight: 500; margin: 10px 0; }
.a { font-size: 1.15em; font-weight: 650; margin: 6px 0 12px; }
.info {
  margin: 14px auto 0; max-width: 620px; padding: 10px 14px; border-radius: 10px; font-size: .86em;
  background: #f3f4f6; color: #4b5563; text-align: left;
}
hr#answer { border: none; border-top: 1px solid #e5e7eb; margin: 16px 0; }

/* night mode (desktop: .nightMode, AnkiDroid: .night_mode) */
.card.nightMode, .card.night_mode { background: #1c1c1e; color: #e5e7eb; }
.nightMode .kind, .night_mode .kind { color: #f87171; }
.nightMode .kind .regions, .night_mode .kind .regions,
.nightMode .prompt, .night_mode .prompt { color: #9ca3af; }
.nightMode .info, .night_mode .info { background: #27272a; color: #d4d4d8; }
.nightMode hr#answer, .night_mode hr#answer { border-top-color: #3f3f46; }
.nightMode .map img, .night_mode .map img { border-color: #3f3f46; }
"""

KIND = '<div class="kind">{{Kind}}</div>'
KIND_BACK = '<div class="kind">{{Kind}} <span class="regions">· {{Regions}}</span></div>'
INFO = '<div class="info">{{Info}}</div>'

TEMPLATES = [
    {"name": "Map → Name",
     "qfmt": '<div class="wrap">' + KIND + '<div class="map">{{Map}}</div>'
             '<div class="prompt">Name the highlighted feature.</div></div>',
     "afmt": '<div class="wrap">' + KIND_BACK + '<div class="map">{{Map}}</div>'
             '<hr id="answer"><div class="name">{{Name}}</div>' + INFO + '</div>'},
    {"name": "Name → Map",
     "qfmt": '<div class="wrap">' + KIND + '<div class="name">{{Name}}</div>'
             '<div class="map">{{Blank map}}</div>'
             '<div class="prompt">Point to it on the map.</div></div>',
     "afmt": '<div class="wrap">' + KIND_BACK + '<div class="name">{{Name}}</div>'
             '<hr id="answer"><div class="map"><div class="stack">{{Blank map}}{{Highlight}}</div></div>'
             '<div class="map">{{Map}}</div>'
             + INFO + '</div>'},
    {"name": "Fact",
     "qfmt": '{{#Question}}<div class="wrap">' + KIND + '<div class="q">{{Question}}</div></div>'
             '{{/Question}}',
     "afmt": '<div class="wrap">' + KIND + '<div class="q">{{Question}}</div>'
             '<hr id="answer"><div class="a">{{Answer}}</div><div class="map">{{Map}}</div>'
             '<div class="name">{{Name}}</div>' + INFO + '</div>'},
]

MODEL = genanki.Model(
    MODEL_ID, "Physical Geography",
    fields=[{"name": n} for n in ("Name", "Kind", "Regions", "Info", "Map", "Question", "Answer",
                                  "Blank map", "Highlight")],
    templates=TEMPLATES,
    css=CSS,
    sort_field_index=0,
)

DECK_DESCRIPTION = (
    "Rivers, mountain ranges, deserts, lakes, plateaus, plains and peninsulas of the world: a "
    "companion to Ultimate Geography, with maps in the same style. Each feature has a "
    "Map → Name card, a Name → Map card and, for most, a fact card. Map data: "
    "<a href='https://www.naturalearthdata.com/'>Natural Earth</a> (public domain)."
)


# --------------------------------------------------------------------------- helpers

def deck_id(name):
    return 1_600_000_000 + int(hashlib.sha1(name.encode()).hexdigest()[:7], 16)


def slug(s):
    s = s.lower().replace("'", "")
    for a, b in (("é", "e"), ("ô", "o"), ("á", "a"), ("ä", "a")):
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "_", s).strip("_")


def validate(where, *fields):
    for f in fields:
        if f and re.search(r"<(?![a-zA-Z/!])", f):
            raise SystemExit(f"{where}: raw '<' (use &lt;): {f[:80]}")


RENDER_KEY = hashlib.sha1(
    ((HERE / "maps.py").read_text() + (HERE / "geodata.py").read_text()).encode()).hexdigest()[:10]


def src_spec(feat):
    return (feat.src.__class__.__name__, vars(feat.src))


def map_file(feat):
    """Render (or reuse) the feature's close-up map; returns its path."""
    return cached(f"pg-map-{slug(feat.name)}", (src_spec(feat), sorted(feat.view.items())),
                  lambda: maps.render_png(feat.src, **feat.view))


def continent_file(region, feat=None):
    """Render (or reuse) the blank continent map, or the feature's highlight to lay over it."""
    if feat is None:
        return cached(f"pg-blank-{slug(region)}", region, lambda: maps.render_continent_png(region))
    return cached(f"pg-highlight-{slug(feat.name)}", (region, src_spec(feat)),
                  lambda: maps.render_continent_png(region, feat.src))


def cached(name, spec, render):
    key = hashlib.sha1((RENDER_KEY + repr(spec)).encode()).hexdigest()[:10]
    cache = BUILD / "cache" / f"{name}-{key}.png"
    if not cache.exists():
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_bytes(render())
    out = BUILD / "media" / f"{name}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    if not out.exists() or out.read_bytes() != cache.read_bytes():
        out.write_bytes(cache.read_bytes())
    return out


# --------------------------------------------------------------------------- build

def build(html_out=None, only=None):
    root = genanki.Deck(deck_id(DECK_ROOT), DECK_ROOT, description=DECK_DESCRIPTION)
    decks, media, seen, preview, counts = [root], [], set(), [], {}
    due = 0
    for mod_name in MODULES:
        mod = importlib.import_module(mod_name)
        name = f"{DECK_ROOT}::{mod.DECK}"
        deck = genanki.Deck(deck_id(name), name)
        decks.append(deck)
        for feat in mod.FEATURES:
            if only and not re.search(only, feat.name, re.I):
                continue
            where = f"{mod.DECK}: {feat.name}"
            if feat.name in seen:
                raise SystemExit(f"{where}: duplicate feature")
            seen.add(feat.name)
            validate(where, feat.name, feat.info, feat.q, feat.a)
            path = map_file(feat)
            blank = continent_file(feat.regions[0])
            highlight = continent_file(feat.regions[0], feat)
            media += [str(path), str(highlight)]
            if str(blank) not in media:
                media.append(str(blank))
            fields = [feat.name, mod.KIND, ", ".join(feat.regions), feat.info,
                      f'<img src="{path.name}">', feat.q, feat.a,
                      f'<img src="{blank.name}">', f'<img src="{highlight.name}">']
            tags = [f"PG::{slug(mod.DECK).title()}"] + [f"PG::{r.replace(' ', '_')}" for r in feat.regions]
            due += 1
            deck.add_note(genanki.Note(model=MODEL, fields=fields, tags=tags,
                                       guid=genanki.guid_for("pg", mod.KIND, feat.name), due=due))
            counts[mod.DECK] = counts.get(mod.DECK, 0) + 1
            preview.append((fields, (path, blank, highlight)))
            print(f"\r{len(seen)} maps", end="", flush=True)
    print()

    out = (BUILD if only else DIST) / "Physical_Geography.apkg"  # partial builds stay out of dist/
    out.parent.mkdir(parents=True, exist_ok=True)
    genanki.Package(decks, media_files=media).write_to_file(out)
    total = sum(counts.values())
    facts = sum(1 for f, _ in preview if f[5])
    print(f"wrote {out}  ({total} notes, {2 * total + facts} cards, {len(media)} maps)")
    for d, c in counts.items():
        print(f"  {d}: {c}")
    if html_out:
        write_preview(Path(html_out), preview)


def write_preview(path, preview):
    """Static HTML of every note (map, name, info, fact) for proofreading."""
    import shutil
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for (name, kind, regions, info, img, q, a, blank, highlight), srcs in preview:
        for src in srcs:
            shutil.copy(src, path.parent / src.name)
        fact = f'<div class="q">{q}</div><div class="a">{a}</div>' if q else ""
        rows.append(f'<div class="wrap" style="border-bottom:6px solid #ddd">'
                    f'<div class="kind">{kind} <span class="regions">· {regions}</span></div>'
                    f'<div class="map">{img}</div>'
                    f'<div class="map"><div class="stack">{blank}{highlight}</div></div>'
                    f'<div class="name">{name}</div>'
                    f'<div class="info">{info}</div>{fact}</div>')
    path.write_text("<!doctype html><html><head><meta charset='utf-8'>"
                    f"<style>{CSS}</style></head><body class='card'>" + "".join(rows) + "</body></html>")
    print(f"preview: {path}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", help="write an HTML preview to this path")
    ap.add_argument("--only", help="only build features whose name matches this regex (for testing)")
    args = ap.parse_args()
    build(args.html, args.only)
