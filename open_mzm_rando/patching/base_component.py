from __future__ import annotations
import dataclasses

from open_mzm_rando.patching.ROM import ROM


@dataclasses.dataclass(kw_only=True)
class BaseComponent:
    address: int

    @staticmethod
    def get(rom: ROM):
        raise NotImplementedError()
    
    def _create(rom: ROM):
        raise NotImplementedError()
    
