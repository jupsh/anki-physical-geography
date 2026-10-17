# Physical Geography for Anki

An Anki deck of the world's major rivers, mountain ranges, volcanoes, deserts, lakes, plateaus,
plains and peninsulas. It's built as a companion to
[Ultimate Geography](https://github.com/anki-geo/ultimate-geography): it covers what Ultimate
Geography doesn't. Its maps are shaded relief with country borders (no country names) and a
scale bar.

**[Download Physical_Geography.apkg](https://github.com/jupsh/anki-physical-geography/releases/latest/download/Physical_Geography.apkg)**,
then in Anki choose **File → Import**.

## What's in it

251 features, 711 cards:

| Subdeck | Features |
|---|---|
| Rivers | 66 |
| Mountain Ranges | 47 |
| Volcanoes | 14 |
| Deserts | 25 |
| Lakes | 36 |
| Plateaus, Plains & Regions | 37 |
| Peninsulas | 26 |

Each feature has a _Map → Name_ card and a _Name → Map_ card. On the _Name → Map_ card you point
to the feature on a blank map of its continent; the back highlights it on the same map, so you can
check exactly where you pointed. 209 features also have a _Fact_ card: one question that ties the
feature to countries, seas and cities.

<table>
  <tr><th scope="col" colspan="2">Map → Name</th></tr>
  <tr><th scope="col">Front</th><th scope="col">Back</th></tr>
  <tr>
    <td><img src="doc/map-name-front.png" width="380"></td>
    <td><img src="doc/map-name-back.png" width="380"></td>
  </tr>
</table>

<table>
  <tr><th scope="col" colspan="2">Name → Map</th></tr>
  <tr><th scope="col">Front</th><th scope="col">Back</th></tr>
  <tr>
    <td><img src="doc/name-map-front.png" width="380"></td>
    <td><img src="doc/name-map-back.png" width="380"></td>
  </tr>
</table>

<table>
  <tr><th scope="col" colspan="2">Fact</th></tr>
  <tr><th scope="col">Front</th><th scope="col">Back</th></tr>
  <tr>
    <td><img src="doc/fact-front.png" width="380"></td>
    <td><img src="doc/fact-back.png" width="380"></td>
  </tr>
</table>

### Custom study

Every note is tagged with its subdeck and continent (`PG::Rivers`, `PG::Europe`, …), so you can
build [filtered decks](https://docs.ankiweb.net/filtered-decks.html) for narrower goals:

- `card:"Map → Name"` to learn locations and nothing else;
- `tag:PG::Rivers tag:PG::Europe` to learn Europe's rivers;
- `-card:Fact` to skip the fact cards;
- `tag:PG::Africa or tag:PG::Asia` to focus on two continents.

## Maps

The maps are shaded-relief (topographic) maps drawn from
[Natural Earth](https://www.naturalearthdata.com/) data (public domain), with a world locator in
one corner. Each map is centred on its feature (Lambert azimuthal equal-area), so shapes stay
true at any latitude. They show country borders as landmarks — borders only, with no country
names — plus major rivers, and a scale bar whose full length is the labelled distance (true at
the map centre; the projection stretches distances away from it). Area features are outlined
in red with a white casing so they stay legible over busy relief. Terrain colours combine
elevation and environment; they are not a numerical elevation scale. Maps are saved as WebP,
roughly a ninth the size of equivalent full-colour PNGs.

The _Name → Map_ cards also use a fixed map of each continent, in the same style but without the
locator.

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

The first build downloads the Natural Earth files (~30 MB) plus the shaded-relief raster
(103 MB) into `build/natural_earth/` and takes a while — about 40 minutes for all 251
terrain maps on first render. Maps are then cached in `build/physical_geography/`, so later
builds are fast.

Note GUIDs come from each feature's kind and name, so re-importing a new version updates your
existing notes and keeps your progress. Renaming a feature, though, adds it as a new note.

### Terrain style comparison

A small preview compares the previous flat style with the shaded-relief maps for the
Himalayas, Tibetan Plateau, Mekong, Sahara and the Asia recall map:

<img src="doc/terrain-comparison.jpg" width="760" alt="Flat and terrain maps of the Himalayas and the Mekong, side by side">

The relief raster (Natural Earth HYP_LR_SR v3.2.0, public domain) is downloaded automatically
on the first build. To rebuild just the comparison, run:

```sh
uv run python scripts/preview_terrain.py
```

Open `build/terrain_preview/index.html` to compare styles, toggle country borders,
view maps at phone width and reveal the Himalayas on the continent map. Use `--overlays-only`
to reuse the base maps when iterating on overlays.

## Contributing

Spotted a mistake, or think a feature is missing? [Open an issue](https://github.com/jupsh/anki-physical-geography/issues).
To change the deck yourself, see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Public domain ([Unlicense](LICENSE.md)), like Ultimate Geography. The maps are generated from
public-domain Natural Earth data.
