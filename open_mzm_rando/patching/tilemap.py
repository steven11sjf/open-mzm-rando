from __future__ import annotations
import dataclasses

from open_mzm_rando.patching.appendable_data import AppendableData
from open_mzm_rando.patching.base_component import BaseComponent
from open_mzm_rando.patching.ROM import ROM
from open_mzm_rando.logger import LOG


@dataclasses.dataclass
class Tilemap(BaseComponent, AppendableData):
    pointer: int
    rows: int
    data: list[int]


    @staticmethod
    def add_tilemap(rom: ROM, pointer: int) -> Tilemap:
        rom.stream.seek(pointer + 1)
        rows = rom.stream.read_UInt8()
        length = rows * 0x40 + 1
        rom.stream.seek(pointer)
        data = [ rom.stream.read_UInt16() for _ in range(length) ]

        tm = Tilemap(
            address=pointer,
            orig_address=pointer,
            orig_size=length*2,
            pointed_to_by=[],
            pointer=pointer,
            rows=rows,
            data=data
        )
        rom.appended.add_data(tm)
        rom.stream.seek(tm.address)
        return tm
    
    def to_bytes(self) -> bytes:
        res = bytearray()
        for v in self.data:
            res.extend(v.to_bytes(2, "little"))
        
        return bytes(res)
    
    def write(self, rom: ROM):
        newLen = len(self.data) * 2
        if self.orig_size < newLen:
            raise ValueError("Tilemap extended!")
        else:
            return rom.appended.write_immediate(self)

    def find_empty_spot(self, tileVal: int) -> int:
        """Finds an empty spot in the tiletable, sets its values and returns the BG1 value"""
        blockNum = 0x4C

        for i in range(blockNum, 0x50):
            offset = i*4+1
            if self.data[offset:offset+4] == [0x40, 0x40, 0x40, 0x40]:
                LOG.info("Found empty spot at %i (%i) - data is [%i,%i,%i,%i]", i, offset, 
                         self.data[offset], self.data[offset+1], self.data[offset+2], self.data[offset+3])
                self.data[offset] = tileVal
                self.data[offset+1] = tileVal+1
                self.data[offset+2] = tileVal+2
                self.data[offset+3] = tileVal+3

                return i
