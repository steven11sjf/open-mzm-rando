from enum import Enum

from open_mzm_rando.patching.ROM import ROM


class ClipdataType(Enum):
    COMPRESSED = 0
    DECOMPRESSED = 1
    NOT_FOUND = 2

class Clipdata:
    @staticmethod
    def GetWidthHeight(rom: ROM) -> list[int, int]:
        """Returns the width/height as a list for the current clipdata. returns stream to start of clipdata. """
        width = rom.stream.read_UInt8()
        height = rom.stream.read_UInt8()
        rom.stream.seek_from_current(-2)
        return [width, height]

    @staticmethod
    def FindTile(rom: ROM, target: int) -> ClipdataType:
        """Finds clipdata for the target tile in the current clipdata"""
        count = 0
        stream = rom.stream
        width = rom.stream.read_UInt8()
        rom.stream.read_UInt16() # skip hiehgt and unk

        while(count <= target):
            byte = stream.read_UInt8()
            if byte > 0x80:
                # repeat next clipdata byte for (byte-0x80) tiles
                count += byte - 0x80
                if count > target:
                    # in compressed data
                    return ClipdataType.COMPRESSED
                stream.read_UInt8() # consume next tile, we don't care what it is
            else:
                # read the next `byte` bytes
                if count + byte < target:
                    count += byte
                    stream.seek_from_current(byte) # consume `byte` bytes
                else:
                    # count + byte >= target
                    # off = target - count
                    stream.seek_from_current(target - count - 1)
                    return ClipdataType.DECOMPRESSED
        return ClipdataType.DECOMPRESSED