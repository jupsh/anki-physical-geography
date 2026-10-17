"""Build a local comparison of the existing maps and experimental terrain maps.

Run from the project root: uv run python scripts/preview_terrain.py
See physical_geography/terrain.py for the one-time raster download.
Writes only to build/terrain_preview/; does not rebuild the released deck.
"""

import argparse
import importlib
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "physical_geography"))

import maps  # noqa: E402
import countries  # noqa: E402

OUT = ROOT / "build/terrain_preview"
SAMPLES = [("mountains", "Himalayas"), ("lands", "Tibetan Plateau"),
           ("rivers", "Mekong"), ("deserts", "Sahara")]


def main(overlays_only=False):
    OUT.mkdir(parents=True, exist_ok=True)
    rows, sizes, features = [], {}, {}
    for module, name in SAMPLES:
        feature = next(f for f in importlib.import_module(f"content.{module}").FEATURES
                       if f.name == name)
        features[name] = feature
        slug = name.lower().replace(" ", "-")
        sizes[name] = {}
        for style in ("current", "terrain"):
            print(f"Rendering {name}: {style}", flush=True)
            terrain = style == "terrain"
            path = OUT / f"{slug}-{style}.{'webp' if terrain else 'png'}"
            if overlays_only and path.exists():
                data = path.read_bytes()
            else:
                data = maps.render_png(feature.src, **feature.view, terrain=terrain,
                                       webp_quality=80 if terrain else None)
                path.write_bytes(data)
            sizes[name][style] = len(data)
        (OUT / f"{slug}-countries.png").write_bytes(countries.for_feature(feature))
        rows.append(section(name, slug, feature.info))
    for style in ("current", "terrain"):
        print(f"Rendering Asia: {style}", flush=True)
        terrain = style == "terrain"
        path = OUT / f"asia-{style}.{'webp' if terrain else 'png'}"
        if overlays_only and path.exists():
            data = path.read_bytes()
        else:
            data = maps.render_continent_png("Asia", terrain=terrain,
                                             webp_quality=80 if terrain else None)
            path.write_bytes(data)
        overlay = maps.render_continent_png("Asia", features["Himalayas"].src,
                                           terrain=style == "terrain")
        (OUT / f"asia-{style}-highlight.png").write_bytes(overlay)
        sizes.setdefault("Asia", {})[style] = len(data)
    (OUT / "asia-countries.png").write_bytes(countries.render(maps.continent_view("Asia")))
    rows.append(section("Asia · recall map", "asia",
                        "Point to the Himalayas. Try locating the range before showing the answer.",
                        continent=True))
    (OUT / "index.html").write_text(HTML.replace("ROWS", "".join(rows)))
    (OUT / "sizes.json").write_text(json.dumps(sizes, indent=2))
    contact_sheet()
    # A standalone image is convenient when sharing the proposed country layer.
    bordered = Image.open(OUT / "himalayas-terrain.webp").convert("RGBA")
    bordered.alpha_composite(Image.open(OUT / "himalayas-countries.png"))
    bordered.save(OUT / "himalayas-with-countries.png")
    print(f"Preview: {OUT / 'index.html'}", flush=True)
    print(json.dumps(sizes, indent=2))


def section(name, slug, info, continent=False):
    cards = []
    for style, label in (("current", "Current"), ("terrain", "Terrain")):
        overlay = (f'<img class="highlight" src="asia-{style}-highlight.png" alt="Himalayas outline">'
                   if continent else "")
        ext = "webp" if style == "terrain" else "png"
        cards.append(f'<figure class="{style}"><figcaption>{label}</figcaption>'
                     f'<div class="map"><img src="{slug}-{style}.{ext}" '
                     f'alt="{name}, {label.lower()} map">{overlay}'
                     f'<img class="countries" src="{slug}-countries.png" '
                     f'alt="Country borders"></div></figure>')
    toggle = ('<label class="answer"><input type="checkbox" id="answer"> Show answer</label>'
              if continent else '')
    return (f'<section id="{slug}"><h2>{name}</h2><p>{info}</p>{toggle}'
            f'<div class="comparison">{"".join(cards)}</div></section>')


def contact_sheet():
    font = ImageFont.truetype("DejaVuSans.ttf", 26)
    small = ImageFont.truetype("DejaVuSans.ttf", 19)
    width, margin, gap = 650, 28, 20
    items = []
    for name in ("Himalayas", "Mekong"):
        slug = name.lower()
        images = [Image.open(OUT / f"{slug}-{style}.{'webp' if style == 'terrain' else 'png'}"
                             ).convert("RGB")
                  for style in ("current", "terrain")]
        images = [im.resize((width, round(width * im.height / im.width)), Image.Resampling.LANCZOS)
                  for im in images]
        items.append((name, images))
    height = sum(86 + images[0].height + gap for _, images in items) + margin
    sheet = Image.new("RGB", (2 * width + gap + 2 * margin, height), "#fafaf7")
    draw = ImageDraw.Draw(sheet)
    y = margin
    for name, images in items:
        draw.text((margin, y), name, fill="#24352d", font=font)
        for i, (label, im) in enumerate(zip(("CURRENT", "TERRAIN"), images)):
            x = margin + i * (width + gap)
            draw.text((x, y + 42), label, fill="#64756c", font=small)
            sheet.paste(im, (x, y + 78))
        y += 86 + images[0].height + gap
    sheet.save(OUT / "comparison.jpg", quality=92)


HTML = """<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Physical Geography · Terrain study</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#f7f8f4;color:#24352d;font:16px/1.6 system-ui,sans-serif}
main{max-width:1600px;margin:auto;padding:36px}header{max-width:850px;margin-bottom:28px}
.eyebrow{font-size:12px;letter-spacing:.15em;text-transform:uppercase;color:#657b6c}h1{font-size:38px;line-height:1.2;margin:10px 0 16px;letter-spacing:-.03em}
header p,section>p{color:#5a695f}nav{display:flex;gap:8px;flex-wrap:wrap}a{color:#315a44}
nav a{padding:5px 12px;border:1px solid #d9e0d7;border-radius:20px;text-decoration:none;font-size:14px}
.toolbar{position:sticky;top:0;z-index:2;display:flex;gap:8px;align-items:center;flex-wrap:wrap;padding:12px 0;background:#f7f8f4f5;border-bottom:1px solid #d9e0d7}
button{font:inherit;font-size:14px;border:1px solid #cbd6cc;background:white;padding:8px 16px;border-radius:8px;cursor:pointer}
button[aria-pressed=true]{background:#315a44;color:white;border-color:#315a44}.phone-control{margin-left:auto;font-size:14px}
section{padding:36px 0;scroll-margin-top:80px;border-bottom:1px solid #d9e0d7}h2{font-size:26px;margin:0 0 8px}section>p{max-width:900px;margin:0 0 20px}
.comparison{display:grid;grid-template-columns:1fr 1fr;gap:24px}figure{margin:0;min-width:0}figcaption{font-size:12px;letter-spacing:.12em;text-transform:uppercase;margin-bottom:10px;color:#657b6c}
.map{position:relative}.map img{display:block;width:100%;height:auto;border-radius:10px}.highlight{position:absolute;inset:0;display:none!important}.reveal .highlight{display:block!important}
.countries{position:absolute;inset:0;display:none!important;pointer-events:none}.show-countries .countries{display:block!important}.country-control{font-size:14px}
.answer{display:inline-block;margin-bottom:16px;cursor:pointer}input{accent-color:#315a44}
body[data-mode=current] .terrain,body[data-mode=terrain] .current{display:none}body:not([data-mode=both]) .comparison{grid-template-columns:1fr;max-width:1000px;margin:auto}
body.phone figure{max-width:360px;margin:auto;width:100%}footer{padding:32px 0;font-size:13px;color:#657b6c}
@media(max-width:800px){main{padding:20px}h1{font-size:30px}.comparison{grid-template-columns:1fr}.phone-control{margin-left:0}section{scroll-margin-top:130px}}
</style>
<body data-mode="both" class="show-countries"><main><header><div class="eyebrow">Physical Geography / Map experiment</div>
<h1>Let the landscape do more of the teaching.</h1>
<p>Four features and one continent map, shown in the current style and with shaded relief.
The terrain version keeps the same framing and uses transparent area highlights. Toggle country borders for more context.</p>
<nav><a href="#himalayas">Himalayas</a><a href="#tibetan-plateau">Tibetan Plateau</a><a href="#mekong">Mekong</a><a href="#sahara">Sahara</a><a href="#asia">Asia recall</a></nav></header>
<div class="toolbar" aria-label="Comparison controls"><button data-mode="both" aria-pressed="true">Side by side</button><button data-mode="current" aria-pressed="false">Current</button><button data-mode="terrain" aria-pressed="false">Terrain</button><label class="country-control"><input id="countries" type="checkbox" checked> Country borders</label><label class="phone-control"><input id="phone" type="checkbox"> Phone width</label></div>
ROWS
<footer>Prototype · Natural Earth HYP_LR_SR v3.2.0, public domain.
Terrain colours combine elevation and environment; they are not a numerical elevation scale.
Region outlines remain approximate. <a href="https://www.naturalearthdata.com/downloads/10m-raster-data/10m-cross-blend-hypso/">Terrain source</a></footer>
</main><script>
document.querySelectorAll('button[data-mode]').forEach(button=>button.addEventListener('click',()=>{
document.body.dataset.mode=button.dataset.mode;
document.querySelectorAll('button[data-mode]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));
}));
document.querySelector('#phone').addEventListener('change',event=>document.body.classList.toggle('phone',event.target.checked));
document.querySelector('#countries').addEventListener('change',event=>document.body.classList.toggle('show-countries',event.target.checked));
document.querySelector('#answer').addEventListener('change',event=>document.querySelector('#asia').classList.toggle('reveal',event.target.checked));
</script></body></html>"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--overlays-only", action="store_true",
                        help="reuse existing base maps while rebuilding overlays and the preview")
    main(parser.parse_args().overlays_only)
