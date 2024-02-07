from enum import Enum
from open_mzm_rando.patching.ROM import ROM


class RLEResult(Enum):
    COMPRESSED = "COMPRESSED"
    DECOMPRESSED = "DECOMPRESSED"
    NOT_FOUND = "NOT_FOUND"

def RLE_seek_target(rom: ROM, target: int) -> RLEResult:
    count = 0
    stream = rom.stream

    while(count <= target):
        byte = stream.read_UInt8()
        if byte > 0x80:
            # repeat next clipdata byte for (byte-0x80) tiles
            count += byte - 0x80
            if count > target:
                # in compressed data
                return RLEResult.COMPRESSED
            stream.read_UInt8() # consume next tile, we don't care what it is
        else:
            if byte == 0:
                raise ValueError("RLE seek encountered a run of zero - check your offsets!")
            # read the next `byte` bytes
            if count + byte < target:
                count += byte
                stream.seek_from_current(byte) # consume `byte` bytes
            else:
                # count + byte >= target
                # off = target - count
                stream.seek_from_current(target - count - 1)
                return RLEResult.DECOMPRESSED
    return RLEResult.NOT_FOUND

def RLE_find_target_bytes_in_clip(rom: ROM, targets: dict[int, str]) -> list:
    count = 0
    stream = rom.stream
    
    width = stream.read_UInt8()
    height = stream.read_UInt8()
    rom.stream.seek_from_current(1)
    
    datas = []
    end = width * height
    while(count <= end):
        byte = stream.read_UInt8()
        if byte > 0x80:
            # repeat next clipdata byte for (byte-0x80) tiles
            count += byte - 0x80
            val = stream.read_UInt8()

            if val in targets:
                raise ValueError(f"Encountered a compressed run of {targets[val]}!")
        else:
            if byte == 0:
                raise ValueError("RLE seek encountered a run of zero - check your offsets!")
            # read the next `byte` bytes
            for i in range(byte):
                val = stream.read_UInt8()
                count += 1
                if val in targets:
                    x = count % width
                    y = count // height
                    datas.append({
                        "type": targets[val],
                        "x": x,
                        "y": y
                    })
    
    return datas