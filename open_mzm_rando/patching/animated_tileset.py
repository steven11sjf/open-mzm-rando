from __future__ import annotations
import dataclasses

from open_mzm_rando.patching.base_component import BaseComponent
from open_mzm_rando.patching.ROM import ROM


@dataclasses.dataclass(kw_only=True)
class AnimTileset(BaseComponent):
    num: int
    entries: list

    @staticmethod
    def get(rom: ROM, atsNum: int):
        rom.stream.follow_pointer(rom.offsets.AnimTilesetPtr)
        rom.stream.seek_from_current(atsNum * 0x30)
        addr = rom.stream.stream.tell()

        entries = []
        for _ in range(0x10):
            entries.append([
                rom.stream.read_UInt8(),
                rom.stream.read_UInt8(),
                rom.stream.read_UInt8()
            ])
        
        return AnimTileset(
            address=addr,
            num=atsNum,
            entries=entries
        )
    
    def find_empty(self, animGfxNum: int):
        for i, ent in enumerate(self.entries):
            if ent[0] == 0:
                ent[0] = animGfxNum
                return i
        raise ValueError("No empty AnimGfx!")
    
    def write(self, rom: ROM, ats_num: int):
        rom.stream.follow_pointer(rom.offsets.AnimTilesetPtr)
        rom.stream.seek_from_current(ats_num * 0x30)
        for ent in self.entries:
            rom.stream.write_UInt8(ent[0])
            rom.stream.write_UInt8(ent[1])
            rom.stream.write_UInt8(ent[2])