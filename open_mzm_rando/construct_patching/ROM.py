import construct
from construct import (Bytes, Construct, Container, Struct, stream_size)

from open_mzm_rando.construct_patching.rom_code_section import ROM_CODE
from open_mzm_rando.construct_patching.construct_extensions.strings import PaddedStringRobust

ROM_HEADER = Struct(
    _unk = Bytes(0xA0),
    version_str = PaddedStringRobust(0x10, "ascii"),
    _unk2 = Bytes(0x10)
)

# the whole ROM
# welcome to hecc
class ROM(Construct):
    def _parse(self, stream, context, path):
        if stream_size(stream) != 0x800000:
            raise ValueError("ROM is not 8MiB long!")
        
        obj = Container()

        obj.header = ROM_HEADER._parsereport(stream, context, f"{path} -> Header")

        if obj.header.version_str != "ZEROMISSIONEBMXE":
            raise ValueError(f"Version {obj.header.version_str} is not a North American (U) version!")
        
        obj.rom_code = ROM_CODE._parsereport(stream, context, f"{path} -> ROM code")
        
        return obj

    def _build(self, obj, stream, context, path):
        ROM_HEADER._build(obj.header, stream, context, f"{path} -> Header")

        ROM_CODE._build(obj.rom_code, stream, context, f"{path} -> ROM code")

    def _sizeof(self, context, path):
        return 0x800000