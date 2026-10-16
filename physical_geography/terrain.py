"""Experimental terrain background from Natural Earth HYP_LR_SR v3.2.0.

Download https://naturalearth.s3.amazonaws.com/10m_raster/HYP_LR_SR.zip and
extract HYP_LR_SR.tif into build/natural_earth/terrain/ before running the preview.
The source is a global, pixel-centred equirectangular raster (16200 x 8100).
Colours blend elevation and environment; they are not a numerical elevation key.
"""

import base64
import io
import math
import warnings
from functools import cache
from pathlib import Path

from PIL import Image, ImageEnhance

SOURCE = Path(__file__).resolve().parent.parent / "build/natural_earth/terrain/HYP_LR_SR.tif"


@cache
def _source():
    # This known global dataset exceeds Pillow's conservative default pixel limit.
    # Keep the protection in place for other images, and validate this source's size.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", Image.DecompressionBombWarning)
        with Image.open(SOURCE) as image:
            if image.size != (16200, 8100):
                raise ValueError(f"Unexpected Natural Earth raster dimensions: {image.size}")
            return image.convert("RGB")


def relief_uri(view, width):
    """Inverse-project each output pixel and bilinearly sample the global raster.

    Sampling longitude modulo the source width avoids a seam at the antimeridian;
    clamping latitude handles the poles without needing a second projection stack.
    """
    source = _source()
    sw, sh = source.size
    pixels = source.load()
    result = bytearray(width * view.h * 3)
    inv = view.proj.inv
    offset = 0
    for row in range(view.h):
        y = view.y1 - (row + 0.5) / view.scale
        for col in range(width):
            lon, lat = inv(view.x0 + (col + 0.5) / view.scale, y)
            sx = ((lon + view.lon0 + 180) % 360) * sw / 360 - 0.5
            sy = min(sh - 1.0, max(0.0, (90 - lat) * sh / 180 - 0.5))
            x0, y0 = math.floor(sx), math.floor(sy)
            fx, fy = sx - x0, sy - y0
            x1, y1 = (x0 + 1) % sw, min(y0 + 1, sh - 1)
            x0 %= sw
            a, b = pixels[x0, y0], pixels[x1, y0]
            c, d = pixels[x0, y1], pixels[x1, y1]
            for band in range(3):
                upper = a[band] + fx * (b[band] - a[band])
                lower = c[band] + fx * (d[band] - c[band])
                result[offset] = round(upper + fy * (lower - upper))
                offset += 1
    image = Image.frombytes("RGB", (width, view.h), bytes(result))
    image = ImageEnhance.Color(image).enhance(0.7)
    image = Image.blend(image, Image.new("RGB", image.size, "#fdfbe5"), 0.12)
    buf = io.BytesIO()
    image.save(buf, "PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("ascii")
