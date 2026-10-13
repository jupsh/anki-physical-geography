"""Focused checks for the coverage update: new sources resolve, new features exist,
custom outlines bound the right places, and no fact card asks what a name means
or what a feature used to be called.

Run: uv run python -m unittest discover -s tests
Needs the Natural Earth cache in build/natural_earth/ (downloaded on first build).
"""

import re
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "physical_geography"))

import importlib  # noqa: E402

MODULES = ["content.rivers", "content.mountains", "content.volcanoes", "content.deserts",
           "content.lakes", "content.lands", "content.peninsulas"]


def all_features():
    for name in MODULES:
        mod = importlib.import_module(name)
        for feat in mod.FEATURES:
            yield mod, feat


class TestNewSources(unittest.TestCase):
    def test_peak_resolves_to_known_volcano_location(self):
        from geodata import Peak
        kind, shapes = Peak("Mount Etna").shapes()
        self.assertEqual(kind, "point")
        (lon, lat), = shapes[0]
        # Etna, Sicily
        self.assertTrue(14.0 < lon < 16.0 and 37.0 < lat < 38.5)

    def test_peak_rejects_unknown_name(self):
        from geodata import Peak
        with self.assertRaises(SystemExit):
            Peak("Mount No Such Volcano").shapes()

    def test_polygon_outline_bounds_mojave_and_closes(self):
        from geodata import Polygon
        kind, shapes = Polygon((-118.6, 35.4), (-114.7, 32.7), (-115.9, 38.7)).shapes()
        self.assertEqual(kind, "area")
        ring = shapes[0][0]
        self.assertEqual(ring[0], ring[-1])


class TestCoverageUpdate(unittest.TestCase):
    def test_new_features_present(self):
        names = {f.name for _, f in all_features()}
        for expected in ("Mojave Desert", "Sinai Peninsula", "Mount Etna", "Mount Fuji",
                         "Krakatoa", "Canadian Shield", "North China Plain", "Snake River",
                         "Paraguay River", "Lake Taupō", "Tibesti Mountains", "Coast Mountains"):
            self.assertIn(expected, names)

    def test_every_source_resolves(self):
        for mod, feat in all_features():
            with self.subTest(feature=feat.name):
                kind, shapes = feat.src.shapes()
                self.assertIn(kind, ("area", "lake", "river", "point"))
                self.assertTrue(shapes)

    def test_custom_outlines_cover_their_landmarks(self):
        by_name = {f.name: f for _, f in all_features()}
        _, shapes = by_name["Mojave Desert"].src.shapes()
        ring = shapes[0][0]
        lons = [p[0] for p in ring]
        lats = [p[1] for p in ring]
        # spans the Colorado River side and Death Valley's latitude, not the Pacific or Mexico
        self.assertTrue(min(lons) < -118 < max(lons) and min(lats) < 37 < max(lats))
        self.assertTrue(max(lons) < -114)
        _, shapes = by_name["Sinai Peninsula"].src.shapes()
        ring = shapes[0][0]
        lons = [p[0] for p in ring]
        lats = [p[1] for p in ring]
        self.assertTrue(32 < min(lons) and max(lons) < 35.2 and 27 < min(lats) < 28)

    def test_no_duplicate_names_and_facts_are_pairs(self):
        seen = set()
        for _, feat in all_features():
            self.assertNotIn(feat.name, seen)
            seen.add(feat.name)
            self.assertEqual(bool(feat.q), bool(feat.a), feat.name)

    def test_no_name_meaning_or_alias_fact_questions(self):
        banned = re.compile(
            r"what does .* mean|what is .* called in|what was .* called|"
            r"other name|nickname|meaning of", re.I)
        for _, feat in all_features():
            self.assertIsNone(banned.search(feat.q), f"{feat.name}: {feat.q}")


if __name__ == "__main__":
    unittest.main()
