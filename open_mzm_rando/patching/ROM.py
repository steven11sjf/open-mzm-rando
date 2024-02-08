from pathlib import Path

from open_mzm_rando.patching.appendable_data import AppendedDataManager
from open_mzm_rando.patching.offsets import Offsets, OffsetForVersion
from open_mzm_rando.patching.MZM_Stream import MZM_Stream

class ROM:
    path: Path
    version: str
    offsets: Offsets
    stream: MZM_Stream
    appended: AppendedDataManager
    next_empty_tileset: int

    def __init__(self, filepath: Path):

        # store data in new file
        self.path = filepath
        self.stream = MZM_Stream(open(self.path.as_posix(), "rb+"))
        self.appended = AppendedDataManager(self.stream)
        self.stream.seek(0)
        self.next_empty_tileset = 0x4F

        self.get_version()
    
    def get_version(self):
        self.stream.seek(0xA0) # version string
        self.version = self.stream.read_String()

        if self.version not in OffsetForVersion:
            raise ValueError(f"The provided ROM ({self.path}) has unsupported version string {self.version}. "
                             "Are you using an American (U) version of the game?")
        else:
            self.offsets = OffsetForVersion[self.version]

    def get_tilesets(self):
        self.stream.follow_pointer(self.offsets.TilesetPtr)
    
    def next_tileset(self):
        self.next_empty_tileset += 1
        return self.next_empty_tileset - 1

    def get_sprite_gfx_pointer(self, sprite_id: int):
        self.stream.follow_pointer(self.offsets.SpriteGfxPtr)
        self.stream.seek_from_current((sprite_id - 0x10) * 4)
        return self.stream.stream.tell()
    
    def get_sprite_palette_pointer(self, sprite_id: int):
        self.stream.follow_pointer(self.offsets.SpritePalettePtr)
        spp_off = self.stream.stream.tell()
        sprid_off = (sprite_id - 0x10) * 4
        print(f"%% sprid_off = {sprid_off}")
        self.stream.seek_from_current((sprite_id - 0x10) * 4)
        print(f"%% offset traveled = {hex(self.stream.stream.tell() - spp_off)}")
        print(f"%% final addy = {hex(self.stream.stream.tell())}")
        return self.stream.stream.tell()

    def get_region_header(self, region: int):
        self.stream.follow_pointer(self.offsets.AreaHeaderPtr)
        self.stream.seek_from_current(region * 0x4)
        self.stream.follow_pointer()
    
    def close(self):
        self.appended.write_all()
        self.stream.stream.close()
