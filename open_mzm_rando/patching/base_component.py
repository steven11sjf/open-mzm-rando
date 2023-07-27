from __future__ import annotations
import dataclasses

from open_mzm_rando.patching.ROM import ROM


@dataclasses.dataclass(kw_only=True)
class BaseComponent:
    address: int
    
