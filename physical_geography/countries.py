"""Transparent country borders, baked into the deck's terrain maps.

Borders only — no country names. The locator corner, when present, is masked
out so the overlay never draws over the inset.
"""

import maps


def render(v, corner=None):
    width, height = maps.W, v.h
    reserved = ""
    if corner:
        x = 0 if corner[0] == "l" else width - maps.IW - 24
        y = 0 if corner[1] == "t" else height - maps.IH - 24
        reserved = (f'<rect x="{x}" y="{y}" width="{maps.IW + 24}" '
                    f'height="{maps.IH + 24}" fill="black"/>')
    boundary = v.line_path(maps._all_lines("ne_50m_admin_0_boundary_lines_land"))
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">'
           f'<defs><mask id="visible"><rect width="{width}" height="{height}" fill="white"/>'
           f'{reserved}</mask></defs>'
           f'<g mask="url(#visible)"><path d="{boundary}" fill="none" stroke="white" '
           f'stroke-opacity="0.5" stroke-width="2.4" stroke-linejoin="round"/>'
           f'<path d="{boundary}" fill="none" stroke="#4a555b" stroke-opacity="0.75" '
           f'stroke-width="1.1" stroke-linejoin="round"/></g></svg>')
    return maps.to_png(svg, alpha=True, full_color=True)


def for_feature(feature):
    kind, shapes = feature.src.shapes()
    seqs = maps._seqs(kind, shapes)
    view = maps.View(seqs, **feature.view)
    points = [p for p in view.pixels(seqs) if 0 <= p[0] <= maps.W and 0 <= p[1] <= view.h]
    return render(view, maps._corner(points, view.h))
