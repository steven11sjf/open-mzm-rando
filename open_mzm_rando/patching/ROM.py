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
    area_header_offsets: list

    def __init__(self, filepath: Path):

        # store data in new file
        self.path = filepath
        self.stream = MZM_Stream(open(self.path, "rb+"))
        self.appended = AppendedDataManager(self.stream)
        self.stream.seek(0)
        self.next_empty_tileset = 0x4F

        self.get_version()
        self._get_area_header_offsets()
    
    def get_version(self):
        self.stream.seek(0xA0) # version string
        self.version = str(self.stream._read(0x10))[2:-1] # trim off the b""

        if self.version not in OffsetForVersion:
            raise ValueError(f"The provided ROM ({self.path}) has unsupported version string {self.version}. "
                             "Are you using an NTSC version of the game?")
        else:
            self.offsets = OffsetForVersion[self.version]

    def _get_area_header_offsets(self):
        self.stream.seek(self.offsets.AreaHeaderPtr)
        area_header_ptr = self.stream.read_Pointer()
        self.stream.seek(area_header_ptr)

        # parse area headers (0=brinstar, 1=kraid, ..., 6=chozodia)
        self.area_header_offsets = [ (i, hex(self.stream.read_Pointer())) for i in range(7) ]

    def get_tilesets(self):
        self.stream.follow_pointer(self.offsets.TilesetPtr)
    
    def next_tileset(self):
        self.next_empty_tileset += 1
        return self.next_empty_tileset - 1

    def get_region_header(self, region: int):
        self.stream.follow_pointer(self.offsets.AreaHeaderPtr)
        self.stream.seek_from_current(region * 0x4)
        self.stream.follow_pointer()
    
    def close(self):
        self.appended.write_all()
        self.stream.stream.close()
