from __future__ import annotations
import dataclasses

from open_mzm_rando.patching.appendable_data import AppendableData
from open_mzm_rando.patching.base_component import BaseComponent
from open_mzm_rando.patching.ROM import ROM


PALETTES: dict[int, Palette] = {}

@dataclasses.dataclass(kw_only=True)
class Palette(BaseComponent, AppendableData):
    pointer: int
    data: list[list[int]]
    rows: int

    @staticmethod
    def _create(rom: ROM, rows: int = 14):
        addr = rom.stream.stream.tell()
        data = [ [rom.stream.read_UInt16() for _ in range(16)] for _ in range(rows) ]

        palette = Palette(
            address=addr,
            orig_size=rows*16,
            orig_address=addr,
            pointed_to_by=[],
            rows=rows,
            data=data,
            pointer=None
        )
        rom.appended.add_data(palette)
        PALETTES[addr] = palette
        rom.stream.seek(palette.address)
        return palette
    
    def to_bytes(self) -> bytes:
        res = bytearray()
        for row in self.data:
            for color in row:
                res.extend(color.to_bytes(2, "little"))
        
        return bytes(res)
    
    def get_color(self, row: int, col: int):
        return self.data[row][col]
    
    def copy_row(self, source: list[int], dst_row: int):
        self.data[dst_row] = source

    def write(self, rom: ROM) -> int:
        newLen = len(self.data) * 2
        if newLen < self.rows * 16:
            return rom.appended.write_immediate(self)
        else:
            raise ValueError("Palette grew!")
