"""Scale-bar arithmetic for the terrain maps.

Run: uv run python -m unittest discover -s tests
"""

import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "physical_geography"))

import maps  # noqa: E402


def view_for_km_per_px(km_per_px):
    return SimpleNamespace(scale=maps.R_KM / km_per_px, h=600)


class TestScaleBar(unittest.TestCase):
    def test_steps_up_when_largest_fit_would_be_too_short_for_labels(self):
        # At 10 km/px the largest nice fit under 170 px is 1000 km (100 px),
        # too short for its own label, so it steps up to 2000 km (200 px).
        total, width = maps.scale_bar_km(view_for_km_per_px(10))
        self.assertEqual(total, 2000)
        self.assertAlmostEqual(width, 200)

    def test_bar_width_stays_label_safe(self):
        for km_per_px in (0.1, 1, 3.7, 12.26, 25, 80, 200):
            total, width = maps.scale_bar_km(view_for_km_per_px(km_per_px))
            self.assertIn(total, maps.NICE_KM)
            self.assertGreaterEqual(width, 50, km_per_px)
            self.assertLessEqual(width, 360, km_per_px)

    def test_asia_bar_labels_do_not_collide(self):
        # Regression: Asia rendered "0,000 km" when the 1000 km bar was
        # narrower than the "1,000 km" label drawn beside the "0".
        total, width = maps.scale_bar_km(maps.continent_view("Asia"))
        self.assertEqual(total, 2000)
        self.assertGreater(width, 140)

    def test_svg_contains_labelled_bar(self):
        svg = maps.scale_bar(view_for_km_per_px(10), "rb")
        self.assertIn("2,000 km", svg)
        self.assertNotIn(">0<", svg)  # undivided bar: no unaligned tick labels

    def test_webp_encoding_returns_webp(self):
        import io

        from PIL import Image

        svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="60" height="40">'
               '<rect width="60" height="40" fill="#7a9a6d"/>'
               '<circle cx="30" cy="20" r="12" fill="#c12838"/></svg>')
        png = maps.to_png(svg, full_color=True)
        webp = maps.to_png(svg, full_color=True, webp_quality=80)
        self.assertEqual(Image.open(io.BytesIO(webp)).format, "WEBP")
        self.assertEqual(Image.open(io.BytesIO(png)).format, "PNG")


if __name__ == "__main__":
    unittest.main()
