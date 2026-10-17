"""Terrain background from Natural Earth HYP_LR_SR v3.2.0 (public domain).

The raster is downloaded once into build/natural_earth/terrain/ (103 MB zip)
and extracted there. The source is a global, pixel-centred equirectangular
raster (16200 x 8100). Colours blend elevation and environment; they are not
a numerical elevation key.
"""

import base64
import io
import math
import urllib.request
import warnings
import zipfile
from functools import cache
from pathlib import Path

from PIL import Image, ImageEnhance

SOURCE = Path(__file__).resolve().parent.parent / "build/natural_earth/terrain/HYP_LR_SR.tif"
URL = "https://naturalearth.s3.amazonaws.com/10m_raster/HYP_LR_SR.zip"
CELL = 20  # px; the projection is approximated by affine tiles this size


def _ensure():
    if SOURCE.exists():
        return
    SOURCE.parent.mkdir(parents=True, exist_ok=True)
    archive = SOURCE.parent / "HYP_LR_SR.zip"
    print(f"downloading {URL}")
    with urllib.request.urlopen(URL) as r, open(archive, "wb") as f:
        while chunk := r.read(1 << 20):
            f.write(chunk)
    with zipfile.ZipFile(archive) as z:
        z.extract("HYP_LR_SR.tif", SOURCE.parent)
    archive.unlink()


@cache
def _source():
    _ensure()
    # This known global dataset exceeds Pillow's conservative default pixel limit.
    # Keep the protection in place for other images, and validate this source's size.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", Image.DecompressionBombWarning)
        with Image.open(SOURCE) as image:
            if image.size != (16200, 8100):
                raise ValueError(f"Unexpected Natural Earth raster dimensions: {image.size}")
            return image.convert("RGB")


def _src_xy(view, sw, sh, X, Y):
    lon, lat = view.proj.inv(*view.unpx(X, Y))
    sx = ((lon + view.lon0 + 180) % 360) * sw / 360 - 0.5
    sy = min(sh - 1.0, max(0.0, (90 - lat) * sh / 180 - 0.5))
    return sx, sy


def relief_uri(view, width):
    """Project the global raster into the view.

    The inverse projection is approximated by affine tiles (PIL MESH, at C
    speed) instead of a per-pixel Python loop, which took ~20 s per map.
    Tiles that straddle the antimeridian cannot wrap in a mesh, so those
    narrow bands are re-rendered per pixel with modulo sampling.
    """
    source = _source()
    sw, sh = source.size
    height = view.h
    mesh, seam_bands = [], []
    for y0 in range(0, height, CELL):
        y1 = min(y0 + CELL, height)
        for x0 in range(0, width, CELL):
            x1 = min(x0 + CELL, width)
            corners = [_src_xy(view, sw, sh, X, Y)
                       for X, Y in ((x0, y0), (x0, y1), (x1, y1), (x1, y0))]  # NW SW SE NE
            cx, cy = _src_xy(view, sw, sh, (x0 + x1) / 2, (y0 + y1) / 2)
            fixed = []
            for sx, sy in corners:
                sx += sw * round((cx - sx) / sw)
                fixed.append((sx, sy))
            if min(s for s, _ in fixed) < 0 or max(s for s, _ in fixed) >= sw:
                seam_bands.append((x0, x1))
            flat = tuple(round(v, 1) for point in fixed for v in point)
            mesh.append(((x0, y0, x1, y1), flat))
    image = source.transform((width, height), Image.Transform.MESH, mesh,
                             Image.Resampling.BILINEAR)
    if seam_bands:
        pixels = source.load()
        for bx0, bx1 in sorted(set(seam_bands)):
            band = Image.new("RGB", (bx1 - bx0, height))
            bp = band.load()
            for row in range(height):
                y = view.y1 - (row + 0.5) / view.scale
                for col in range(bx0, bx1):
                    lon, lat = view.proj.inv(view.x0 + (col + 0.5) / view.scale, y)
                    sx = ((lon + view.lon0 + 180) % 360) * sw / 360 - 0.5
                    sy = min(sh - 1.0, max(0.0, (90 - lat) * sh / 180 - 0.5))
                    px, py = math.floor(sx), math.floor(sy)
                    fx, fy = sx - px, sy - py
                    qx, qy = (px + 1) % sw, min(py + 1, sh - 1)
                    px %= sw
                    a, b = pixels[px, py], pixels[qx, py]
                    c, d = pixels[px, qy], pixels[qx, qy]
                    bp[col - bx0, row] = tuple(
                        round((a[i] + fx * (b[i] - a[i])) * (1 - fy)
                              + (c[i] + fx * (d[i] - c[i])) * fy) for i in range(3))
            image.paste(band, (bx0, 0))
    image = ImageEnhance.Color(image).enhance(0.7)
    image = Image.blend(image, Image.new("RGB", image.size, "#fdfbe5"), 0.12)
    buf = io.BytesIO()
    image.save(buf, "JPEG", quality=85)  # relief is photographic: ~10x smaller than PNG here
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("ascii")
