# Contributing

Thanks for helping! Seen something wrong or out of date, or think a feature is missing?
[Open an issue](https://github.com/jupsh/anki-physical-geography/issues). Pull requests are
welcome too.

## Making changes

Each feature is one `F(...)` entry in `physical_geography/content/*.py`:

```python
F("Danube", R("Danube"), EU,
  "Europe's second-longest river (about 2,850 km). Rises in Germany's Black Forest and ...",
  "Which capital's name joins those of two towns on opposite banks of the Danube?", "Budapest"),
```

The arguments are: the name, the map source (`Region`, `Lake` or `River`; see `geodata.py`), the
continent(s), the info text, and an optional fact question and answer. The map framing can be
changed with `span=` (width in km) or `zoom=`. The first continent picks the map that the
_Name → Map_ card uses; the continent frames are `CONTINENTS` in `maps.py`.

Build with `uv run python physical_geography/build.py --html out.html` and check your feature's
map and text in `out.html`. Every push and pull request is also built on GitHub, which catches
errors such as a map source that doesn't exist in Natural Earth.

## Content inclusion rules

- **Don't duplicate Ultimate Geography.** It already covers sovereign states, territories,
  continents, oceans, seas, straits, channels and passages, and a few lakes (the Caspian Sea,
  Aral Sea, Dead Sea and Sea of Galilee). Its inclusion rules are in its
  [CONTRIBUTING.md](https://github.com/anki-geo/ultimate-geography/blob/master/CONTRIBUTING.md#physical-geography).
  If Ultimate Geography adds a feature that is also here, remove it from this deck.
- **Include major, well-known features:** the ones a general atlas labels on a continent-scale
  map.
- **The map must be accurate enough to learn from.** If Natural Earth's outline is misleading
  (for example it covers only part of a range), leave the feature out.

## Writing style

This follows Ultimate Geography's
[writing style](https://github.com/anki-geo/ultimate-geography/blob/master/CONTRIBUTING.md#writing-style):

- Keep the info text concise. When the subject is the feature itself, use a truncated phrase
  ("Flows north through ..."), not a full sentence ("The Nile flows north through ...").
- End the info text with a full stop. Don't end fact answers with one.
- Use "about" for lengths and areas, and leave out figures that sources disagree on.
- A fact question should link the feature to something the learner knows from Ultimate
  Geography (a country, capital, sea or strait) or to one memorable fact.
- The fact card's front shows only the question, with no map or name, so the question must name
  its feature ("the Balkan Mountains", not "these mountains").
- A fact question should have one right answer: "Which provincial capital lies on Lake Ontario?",
  not "Which major Canadian city ...?" (Hamilton is on the lake too).
- Ask for one thing, or at most a pair or three. Put longer lists (the capitals on the Danube) in
  the info text and ask about one of them instead.
- Answer only what was asked. Elevations, areas and other figures go in the info text.

## Versioning and releases

Releases are numbered `x.y`, like Ultimate Geography's:

- `y` goes up for content changes: new, corrected or removed features, or new maps.
- `x` goes up when users would lose progress on upgrade, for example when many features are
  renamed (note GUIDs come from each feature's kind and name).

To release:

1. Update the counts in `README.md` if they changed, and commit.
1. Tag the commit and push the tag, e.g. `git tag v1.1 && git push origin v1.1`.
1. GitHub builds the deck and creates a **draft release** with the `.apkg` attached.
1. Write the release notes from a user's point of view: new features, changed features (name
   them), map changes, other changes. If the note type's fields changed, tell users to tick
   _Merge notetypes_ when importing, or the update won't apply to their existing notes. Then
   publish the release.
1. Update the deck on [AnkiWeb](https://ankiweb.net/decks/): import the new `.apkg` into Anki,
   sync, then select _Actions_ > _Share_ on the deck, update the description if needed, tick the
   _Copyright_ box and click _Share_.
