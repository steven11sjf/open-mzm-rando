from __future__ import annotations
import dataclasses

from open_mzm_rando.patching.base_component import BaseComponent
from open_mzm_rando.patching.ROM import ROM


PALETTES: dict[int, Palette] = {}

@dataclasses.dataclass(kw_only=True)
class Palette(BaseComponent):
    pointer: int

