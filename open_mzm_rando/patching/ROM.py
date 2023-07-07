#from construct import (Bytes, Construct, Container, GreedyBytes, Hex, Struct, Tell, stream_size)
from pathlib import Path

#from open_mzm_rando.patching.rom_code_section import ROM_CODE
#from open_mzm_rando.patching.rom_data_section import ROM_DATA
#from open_mzm_rando.patching.construct_extensions.strings import PaddedStringRobust
from open_mzm_rando.patching.offsets import Offsets, OffsetForVersion
from open_mzm_rando.patching.MZM_Stream import MZM_Stream

class ROM:
    path: Path
    version: str
    offsets: Offsets
    stream: MZM_Stream
    area_header_offsets: list

    def __init__(self, filepath: Path):
        self.path = filepath
        self.stream = MZM_Stream(open(self.path, "rb"))

        self.get_version()
        self._get_area_header_offsets()
    
    def get_version(self):
        self.stream.seek(0xA0) # version string
        self.version = str(self.stream._read(0x10))[2:-1] # trim off the b""
        for k,v in OffsetForVersion.items():
            print(k)
        if self.version not in OffsetForVersion:
            raise ValueError(f"The provided ROM ({self.path}) has unsupported version string {self.version}. "
                             "Are you using an NTSC version of the game?")
        else:
            self.offsets = OffsetForVersion[self.version]

    def _get_area_header_offsets(self):
        self.stream.seek(self.offsets.AreaHeaderPtr)
        area_header_ptr = self.stream.read_Pointer()
        print(area_header_ptr)
        self.stream.seek(area_header_ptr)

        # parse area headers (0=brinstar, 1=kraid, ..., 6=chozodia)
        self.area_header_offsets = [ (i, hex(self.stream.read_Pointer())) for i in range(7) ]

# ROM_HEADER = Struct(
#     _unk = Bytes(0xA0),
#     version_str = PaddedStringRobust(0x10, "ascii"),
#     _unk2 = Bytes(0x10)
# )

# # the whole ROM
# # welcome to hecc
# class ROM_construct(Construct):
#     def _parse(self, stream, context, path):
#         if stream_size(stream) != 0x800000:
#             raise ValueError("ROM is not 8MiB long!")
        
#         obj = Container()

#         obj.header = ROM_HEADER._parsereport(stream, context, f"{path} -> Header")

#         if obj.header.version_str != "ZEROMISSIONEBMXE":
#             raise ValueError(f"Version {obj.header.version_str} is not a North American (U) version!")
        
#         obj.rom = Container()

#         obj.rom.code = ROM_CODE._parsereport(stream, context, f"{path} -> ROM code")
#         obj.tell = Hex(Tell)._parsereport(stream, context, path)

#         obj.rom.data = ROM_DATA._parsereport(stream, context, f"{path} -> ROM data")

#         obj.rom.extra = Bytes(0x88cc)._parsereport(stream, context, f"{path} -> ROM extra")
        
#         return obj

#     def _build(self, obj, stream, context, path):
#         ROM_HEADER._build(obj.header, stream, context, f"{path} -> Header")

#         ROM_CODE._build(obj.rom.code, stream, context, f"{path} -> ROM code")
#         ROM_DATA._build(obj.rom.data, stream, context, f"{path} -> ROM data")
#         Bytes(0x88cc)._build(obj.rom.extra, stream, context, f"{path} -> ROM extra")

#     def _sizeof(self, context, path):
#         return 0x800000