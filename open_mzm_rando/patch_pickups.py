import dataclasses

from enum import Enum

from open_mzm_rando.patching.ROM import ROM
from open_mzm_rando.patching.Room import Room
from open_mzm_rando.patching.run_length_encoding import RLEResult, RLE_seek_target
from open_mzm_rando.locations import ItemType, Location, get_location_by_index

@dataclasses.dataclass(frozen=True)
class Pickup:
    clipdata: int
    tile_id: int
    type: ItemType

ALL_ITEMS: dict[str, Pickup] = {
    "Missile Tank": Pickup(
        clipdata=0x5D,
        tile_id=0x48,
        type=ItemType.TANK
    ),
    "Super Missile Tank": Pickup(
        clipdata=0x5E,
        tile_id=0x4B,
        type=ItemType.TANK
    ),
    "Power Bomb Tank": Pickup(
        clipdata=0x5F,
        tile_id=0x4A,
        type=ItemType.TANK
    ),
    "Energy Tank": Pickup(
        clipdata=0x5C,
        tile_id=0x49,
        type=ItemType.TANK
    )
}

def patch_tank_to_tank(rom: ROM, location: Location, item: Pickup):
    # patch BG1 (main tile layer) if decompressed
    if not location.hidden:
        Room.get_room(rom, location.area, location.room).get_bg1(rom)
        width = rom.stream.read_UInt8()
        rom.stream.read_UInt16() # skip height and unk variable
        bg1_type = RLE_seek_target(rom, location.y * width + location.x)

        if bg1_type == RLEResult.NOT_FOUND: 
            raise ValueError(f"Location {location.rdv_index} has OOB clipdata!")
        elif bg1_type == RLEResult.DECOMPRESSED:
            rom.stream.seek_from_current(1)
            rom.stream.write_UInt8(item.tile_id)

    # patch clip data
    Room.get_room(rom, location.area, location.room).get_clip_data(rom)
    print(f"Clipdata: {hex(rom.stream.stream.tell())}")
    width = rom.stream.read_UInt8()
    rom.stream.read_UInt16() # skip height and unk variable
    clip_type = RLE_seek_target(rom, location.y * width + location.x)
    print(f"CLIPDATA AT {hex(rom.stream.stream.tell())}")
    
    if clip_type == RLEResult.DECOMPRESSED:
        #rom.stream.seek_from_current(1)
        if location.hidden:
            rom.stream.write_UInt8(item.clipdata + 0x10) # hidden tank clipdata = normal clipdata + 0x10
        else:
            rom.stream.write_UInt8(item.clipdata)
    else:
        raise ValueError(f"Clipdata for location {location.rdv_index} has RLEResult {clip_type.value}")


def patch_pickup(rom: ROM, location_idx: int, item: str):
    loc = get_location_by_index(location_idx)
    new_pickup = ALL_ITEMS[item]

    if loc.type is ItemType.EQUIPMENT:
        raise ValueError("Patching from non-tanks is not supported!")
    if new_pickup.type is ItemType.EQUIPMENT:
        raise ValueError("Patching to non-tanks is not supported!")
    if loc.type is ItemType.TANK:
        if new_pickup.type is ItemType.TANK:
            patch_tank_to_tank(rom, loc, new_pickup)
        else:
            # TODO tank to ability
            pass
    else:
        if new_pickup.type is ItemType.TANK:
            # TODO ability to tank
            pass
        else:
            # TODO ability to ability
            pass