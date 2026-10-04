"""Feature data type used by the content modules.

Fields are HTML. `q`/`a` make an optional fact card; leave them empty for no fact card.
`view` options pass through to maps.render_svg: zoom (>1 zooms out), span (map width in km),
center ((lon, lat) to centre on).
"""

from dataclasses import dataclass, field


@dataclass
class Feature:
    name: str
    src: object  # geodata.Region / Lake / River
    regions: tuple  # continents, e.g. ("Africa",) or ("Europe", "Asia")
    info: str
    q: str = ""
    a: str = ""
    view: dict = field(default_factory=dict)


def F(name, src, regions, info, q="", a="", **view):
    if isinstance(regions, str):
        regions = (regions,)
    if bool(q) != bool(a):
        raise SystemExit(f"{name}: fact card needs both a question and an answer")
    return Feature(name, src, regions, info, q, a, view)
