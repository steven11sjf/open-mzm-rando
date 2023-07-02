import construct
from construct import (Bytes, Construct, Container, GreedyBytes, Hex, Struct, Tell, stream_size)

from open_mzm_rando.construct_patching.rom_code_section import ROM_CODE
from open_mzm_rando.construct_patching.rom_data_section import ROM_DATA
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
        
        obj.rom = Container()

        obj.rom.code = ROM_CODE._parsereport(stream, context, f"{path} -> ROM code")
        obj.tell = Hex(Tell)._parsereport(stream, context, path)

        obj.rom.data = ROM_DATA._parsereport(stream, context, f"{path} -> ROM data")

        obj.rom.extra = Bytes(0x88cc)._parsereport(stream, context, f"{path} -> ROM extra")
        
        return obj

    def _build(self, obj, stream, context, path):
        ROM_HEADER._build(obj.header, stream, context, f"{path} -> Header")

        ROM_CODE._build(obj.rom.code, stream, context, f"{path} -> ROM code")
        ROM_DATA._build(obj.rom.data, stream, context, f"{path} -> ROM data")
        Bytes(0x88cc)._build(obj.rom.extra, stream, context, f"{path} -> ROM extra")

    def _sizeof(self, context, path):
        return 0x800000