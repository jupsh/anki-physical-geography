# Physical Geography for Anki

An Anki deck of the world's major rivers, mountain ranges, deserts, lakes, plateaus, plains and
peninsulas. It's built as a companion to
[Ultimate Geography](https://github.com/anki-geo/ultimate-geography): it covers what Ultimate
Geography doesn't, and its maps use the same style.

**[Download Physical_Geography.apkg](https://github.com/jupsh/anki-physical-geography/releases/latest/download/Physical_Geography.apkg)**,
then in Anki choose **File → Import**.

## What's in it

184 features, 516 cards:

| Subdeck | Features |
|---|---|
| Rivers | 50 |
| Mountain Ranges | 34 |
| Lakes | 28 |
| Plateaus, Plains & Regions | 27 |
| Peninsulas | 23 |
| Deserts | 22 |

Each feature has up to three cards:

- **Map → Name:** a map with the feature highlighted; name it.
- **Name → Map:** the name; picture where it is.
- **Fact:** one question that links it to countries, seas and cities, e.g. "Which four capital
  cities stand on the Danube?" (148 features have one.)

Tags: `PG::<Subdeck>` and `PG::<Continent>`, e.g. `PG::Rivers`, `PG::Europe`.

## Maps

The maps are drawn from [Natural Earth](https://www.naturalearthdata.com/) data (public domain) in
Ultimate Geography's colours, with a world locator in one corner. Each map is centred on its
feature (Lambert azimuthal equal-area), so shapes stay true at any latitude. Unlike Ultimate
Geography's maps, they also show major rivers and the state/province lines of the largest
countries, faintly, as landmarks.

The outlines of regions like deserts and mountain ranges are Natural Earth's, and some are rough.
They show where a feature is, not its exact boundary.

## Building it yourself

Needs [uv](https://docs.astral.sh/uv/) and the Cairo library (for `cairosvg`; e.g.
`apt install libcairo2` or `brew install cairo`).

```sh
uv run python physical_geography/build.py                 # writes dist/Physical_Geography.apkg
uv run python physical_geography/build.py --html out.html # plus an HTML preview of every note
uv run python physical_geography/build.py --only Nile     # just matching features, into build/
```

The first build downloads the Natural Earth files (~30 MB) into `build/natural_earth/` and takes
about a minute. Maps are then cached in `build/physical_geography/`.

Features live in `physical_geography/content/*.py`. Each one names its map source (`Region`,
`Lake` or `River`; see `geodata.py`) and can change the map framing with `span=` (width in km) or
`zoom=`. Note GUIDs come from the feature's kind and name, so re-importing updates existing notes,
but renaming a feature adds it as a new note.

Corrections are welcome: open an issue or a pull request.
