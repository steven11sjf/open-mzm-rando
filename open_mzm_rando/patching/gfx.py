from __future__ import annotations
import dataclasses

from open_mzm_rando.patching.appendable_data import AppendableData
from open_mzm_rando.patching.ROM import ROM
from open_mzm_rando.patching.LZ77 import compress_LZ77, decompress_LZ77


class Gfx(AppendableData):
    data: bytearray
    width: int

    def __init__(self, data: bytearray, width: int):
        self.data = data
        self.width = width
    
    def add_gfx(self, src_gfx: Gfx, x: int, y: int):
        dst_byte_width = self.width * 0x20
        dst_index = (y * dst_byte_width) + (x * 0x20)
        src_data = src_gfx.data
        src_byte_width = src_gfx.width * 0x20
        src_height = len(src_data) // src_byte_width
        src_index = 0

        for _ in range(src_height):
            for i in range(src_byte_width):
                self.data[dst_index + i] = src_data[src_index + i]
            
            dst_index += dst_byte_width
            src_index += src_byte_width
    
    def write(self, rom: ROM, sprite_id: int):
        compressed = compress_LZ77(self.data)
        offset = rom.appended._write_to_open_region([], compressed)
        rom.get_sprite_gfx_pointer(sprite_id)
        rom.stream.write_Pointer(offset)