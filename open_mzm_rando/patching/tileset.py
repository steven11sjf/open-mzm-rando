from __future__ import annotations
import dataclasses

from open_mzm_rando.patching.ROM import ROM


TILESETS: dict[int, Tileset] = {}

@dataclasses.dataclass
class Tileset:
    pointer: int
    ts_num: int
    palette_ptr: int

    @staticmethod
    def add_tileset(rom: ROM, ts_num: int):
        rom.get_tilesets()
        rom.stream.seek_from_current(ts_num * 0x14)