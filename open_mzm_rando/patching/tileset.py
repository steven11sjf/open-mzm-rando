from __future__ import annotations
import dataclasses

from open_mzm_rando.patching.animated_tileset import AnimTileset
from open_mzm_rando.patching.palette import Palette
from open_mzm_rando.patching.ROM import ROM
from open_mzm_rando.patching.tilemap import Tilemap
from open_mzm_rando.logger import LOG


TILESETS: dict[int, Tileset] = {}

@dataclasses.dataclass
class Tileset:
    pointer: int
    bg0_gfx_ptr: int
    palette_ptr: int
    palette: Palette
    bg3_gfx_ptr: int
    tilemap_ptr: int
    ts_num: int
    ats_num: int
    ap_num: int
    animated_tileset: AnimTileset
    tilemap: Tilemap


    @staticmethod
    def get_tileset(rom: ROM, ts_num: int):
        if ts_num in TILESETS:
            rom.stream.seek(TILESETS[ts_num].pointer)
            return TILESETS[ts_num]
        else:
            return Tileset.add_tileset(rom, ts_num)
        
    @staticmethod
    def add_tileset(rom: ROM, ts_num: int):
        rom.get_tilesets()
        rom.stream.seek_from_current(ts_num * 0x14)

        ptr = rom.stream.stream.tell()
        rle_background_gfx_ptr = rom.stream.read_Pointer()
        background_palette_ptr = rom.stream.read_Pointer()
        lz77_background_gfx_ptr = rom.stream.read_Pointer()
        background_tilemap_ptr = rom.stream.read_Pointer()
        ats_num = rom.stream.read_UInt8()
        animated_palette = rom.stream.read_UInt8()

        # Create palette
        rom.stream.seek(background_palette_ptr)
        pal = Palette._create(rom, 14)
        pal.add_pointer(ptr + 0x4)

        # read animated tileset
        ats = AnimTileset.get(rom, ats_num)

        # create tilemap
        tm = Tilemap.add_tilemap(rom, background_tilemap_ptr)

        ts = Tileset(
            pointer=ptr,
            ts_num=ts_num,
            bg0_gfx_ptr=rle_background_gfx_ptr,
            palette_ptr=background_palette_ptr,
            bg3_gfx_ptr=lz77_background_gfx_ptr,
            tilemap_ptr=background_tilemap_ptr,
            palette=pal,
            ats_num=ats_num,
            animated_tileset=ats,
            ap_num=animated_palette,
            tilemap=tm
        )

        TILESETS[ts_num] = ts
        return ts

    def add_equipment(self, rom: ROM, equipment_id: int, palette: list[int]) -> int:
        anim_gfx_num = 0x26 + equipment_id

        # find empty spot in palette
        palRow = 15
        for r in range(1, 14):
            color = self.palette.get_color(r, 1)
            blank = True

            for c in range(2, 16):
                if self.palette.get_color(r,c) != color:
                    blank = False
                    break
            
            if blank:
                self.palette.copy_row(palette, r)
                palRow = r + 2
                break
        
        # find empty slot in animGfx
        anim_gfx_slot = self.animated_tileset.find_empty(anim_gfx_num)

        # add to tilemap
        tile_val = (palRow << 12) | (anim_gfx_slot * 4)
        bg1_num = self.tilemap.find_empty_spot(tile_val)

        # fix Tilemap400
        rom.stream.follow_pointer(rom.offsets.Tilemap400Ptr)
        rom.stream.seek_from_current((0xD0 + equipment_id) * 8)
        rom.stream.write_UInt16(tile_val)
        rom.stream.write_UInt16(tile_val+1)
        rom.stream.write_UInt16(tile_val+2)
        rom.stream.write_UInt16(tile_val+3)

        return bg1_num
    
    def write(self, rom: ROM, ts_num: int):
        LOG.info("Writing tileset %i to %i", self.ts_num, ts_num)
        rom.get_tilesets()
        rom.stream.seek_from_current(ts_num * 0x14)
        rom.stream.write_Pointer(self.bg0_gfx_ptr)
        
        addr = rom.stream.stream.tell()

        pal_off = self.palette.write(rom)
        rom.stream.seek(addr)
        rom.stream.write_Pointer(pal_off)
        rom.stream.write_Pointer(self.bg3_gfx_ptr)

        addr = rom.stream.stream.tell()

        tm_off = self.tilemap.write(rom)
        rom.stream.seek(addr)
        rom.stream.write_Pointer(tm_off)

        addr = rom.stream.stream.tell()

        diff = ts_num - 0x4F # num of tilesets
        atsNum = diff + 0x8 # num of animTilesets
        self.animated_tileset.write(rom, atsNum)
        rom.stream.seek(addr)
        rom.stream.write_UInt8(atsNum)
        rom.stream.write_UInt8(self.ap_num)