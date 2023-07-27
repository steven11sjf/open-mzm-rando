from pathlib import Path
import json

from open_mzm_rando.patching.ROM import ROM
from open_mzm_rando.patching.Room import Room


ROM_PATH = "e:/Roms/GBA/MZMU.gba" # Put your path here!

REGIONS = {
    "Brinstar": (0x33E608, 0x63, 0),
    "Kraid": (0x33EAAC, 0x6B, 1),
    "Norfair": (0x33EFB0, 0x85, 2),
    "Ridley": (0x33F5EC, 0x4D, 3),
    "Tourian": (0x33FB98, 0x2C, 4),
    "Crateria": (0x33FB98, 0x35, 5),
    "Chozodia": (0x33FE14, 0xF6, 6)
}

def get_door_music_dict():
    path = Path(ROM_PATH)
    rom = ROM(path) 
    music = get_music_for_rooms(rom)

    # write to open_mzm_rando/files/door_to_music.json
    json_path = Path(__file__).parent.parent.joinpath("open_mzm_rando", "files", "door_to_music.json")
    print(json_path)
    with open(json_path, "w") as f:
        json.dump(music, f, indent=4)


def get_music_for_rooms(rom: ROM) -> dict[str, dict[str, str]]:
    all_doors = {}

    for region, data in REGIONS.items():
        region_doors = {}
        for doornum in range(data[1]):
            # get room for door
            rom.stream.seek(data[0] + (doornum * 0xC) + 1)
            src_room_idx = rom.stream.read_UInt8()
            
            # get music for room
            Room.get_room(rom, data[2], src_room_idx)
            rom.stream.seek_from_current(0x3A)
            music = rom.stream.read_UInt16()
            
            region_doors[hex(doornum)] = hex(music)
        all_doors[region] = region_doors
    
    return all_doors

get_door_music_dict()