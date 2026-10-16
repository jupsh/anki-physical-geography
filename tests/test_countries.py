"""The country overlay for the terrain preview draws borders only, no names.

Run: uv run python -m unittest discover -s tests
Needs the Natural Earth cache in build/natural_earth/ (downloaded on first build).
"""

import io
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "physical_geography"))

from PIL import Image  # noqa: E402

import countries  # noqa: E402
import maps  # noqa: E402

LABEL_INK = (53, 67, 74, 255)  # #35434a, the fill the removed name labels used


class TestCountryOverlay(unittest.TestCase):
    def test_borders_render_without_country_names(self):
        data = countries.render(maps.continent_view("Asia"))
        image = Image.open(io.BytesIO(data)).convert("RGBA")
        self.assertEqual(image.size, (maps.W, maps.continent_view("Asia").h))
        colours = image.getcolors(maxcolors=image.width * image.height)
        present = {colour for _, colour in colours}
        self.assertTrue(any(alpha for _, (*_, alpha) in colours if alpha),
                        "expected some visible border pixels")
        self.assertNotIn(LABEL_INK, present)


if __name__ == "__main__":
    unittest.main()
