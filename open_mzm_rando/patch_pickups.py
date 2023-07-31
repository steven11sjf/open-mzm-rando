import dataclasses
from pathlib import Path

from open_mzm_rando.patching.tileset import Tileset

from open_mzm_rando.patching.gfx import Gfx
from open_mzm_rando.patching.ROM import ROM
from open_mzm_rando.patching.Room import Room
from open_mzm_rando.patching.run_length_encoding import RLEResult, RLE_seek_target
from open_mzm_rando.locations import ItemType, Location, get_location_by_index
from open_mzm_rando.logger import LOG

@dataclasses.dataclass(frozen=True)
class Pickup:
    clipdata: int
    tile_id: int
    type: ItemType
    palette: list[int]
    behavior_type: int
    sprite_id: int = 0
    ability_gfx: str = "None.bin"
    ability_offset: int = 0
    equipment_id: int = 0

ALL_ITEMS: dict[str, Pickup] = {
    "Missile Tank": Pickup(
        clipdata=0x5D,
        tile_id=0x48,
        palette=[17120, 0, 32767, 22197, 14798, 8456, 3038, 1695, 992, 546, 14365, 2064, 32682, 31460, 28003, 24576],
        type=ItemType.TANK,
        behavior_type=0x39,
        ability_gfx="Missile.bin",
    ),
    "Super Missile Tank": Pickup(
        clipdata=0x5E,
        tile_id=0x4B,
        palette=[17120, 0, 32767, 22197, 14798, 8456, 3038, 1695, 992, 546, 14365, 2064, 32682, 31460, 28003, 24576],
        type=ItemType.TANK,
        behavior_type=0x3A,
        ability_gfx="SuperMissile.bin",
    ),
    "Power Bomb Tank": Pickup(
        clipdata=0x5F,
        tile_id=0x4A,
        palette=[17120, 0, 32767, 22197, 14798, 8456, 3038, 1695, 992, 546, 14365, 2064, 32682, 31460, 28003, 24576],
        type=ItemType.TANK,
        behavior_type=0x3B,
        ability_gfx="PowerBomb.bin",
    ),
    "Energy Tank": Pickup(
        clipdata=0x5C,
        tile_id=0x49,
        palette=[17120, 0, 32767, 22197, 14798, 8456, 3038, 1695, 992, 546, 14365, 2064, 32682, 31460, 28003, 24576],
        type=ItemType.TANK,
        behavior_type=0x38,
        ability_gfx="EnergyTank.bin",
    ),
    "Long Beam": Pickup(
        clipdata=0xB0,
        tile_id=0x0,
        palette=[15767, 0, 32767, 21151, 9535, 31, 1046, 2060, 28063, 31764, 20557, 12293, 23871, 23871, 23871, 23871],
        type=ItemType.EQUIPMENT,
        ability_offset=0x13902,
        equipment_id=0,
        behavior_type=0x70,
        sprite_id=0x23,
        ability_gfx="Long.bin",
    ),
    "Charge Beam": Pickup(
        clipdata=0xB1,
        tile_id=0x0,
        palette=[22607, 14336, 32767, 19446, 15245, 15115, 10917, 13760, 32758, 30383, 28007, 24608, 11199, 5727, 315, 2165],
        type=ItemType.EQUIPMENT,
        ability_offset=0x13650,
        equipment_id=1,
        behavior_type=0x71,
        sprite_id=0x44,
        ability_gfx="Charge.bin",
    ),
    "Ice Beam": Pickup(
        clipdata=0xB2,
        tile_id=0x0,
        palette=[15767, 0, 32767, 32763, 32758, 30383, 26950, 22528, 28287, 16408, 18509, 16388, 23871, 23871, 23871, 23871],
        type=ItemType.EQUIPMENT,
        ability_offset=0x13906,
        equipment_id=2,
        behavior_type=0x72,
        sprite_id=0x25,
        ability_gfx="Ice.bin",
    ),
    "Wave Beam": Pickup(
        clipdata=0xB3,
        tile_id=0x0,
        palette=[15767, 0, 32767, 32543, 32287, 31807, 16439, 17422, 15099, 10677, 9485, 7306, 23871, 23871, 23871, 23871],
        type=ItemType.EQUIPMENT,
        ability_offset=0x1390A,
        equipment_id=3,
        behavior_type=0x73,
        sprite_id=0x27,
        ability_gfx="Wave.bin",
    ),
    "Plasma Beam": Pickup(
        clipdata=0xB4,
        tile_id=0x0,
        palette=[15767, 1033, 29596, 25370, 20085, 12718, 8490, 23871, 23871, 23871, 23871, 23871, 23871, 23871, 23871, 5319],
        type=ItemType.EQUIPMENT,
        ability_offset=0x139E4,
        equipment_id=4,
        behavior_type=0x74,
        sprite_id=0x94,
        ability_gfx="Plasma.bin",
    ),
    "Bomb": Pickup(
        clipdata=0xB5,
        tile_id=0x0,
        palette=[25980, 0, 32767, 25370, 20085, 12718, 8490, 32287, 31807, 16439, 12298, 992, 18420, 5929, 3783, 1442],
        type=ItemType.EQUIPMENT,
        ability_offset=0x1390E,
        equipment_id=5,
        behavior_type=0x75,
        sprite_id=0x29,
        ability_gfx="Bomb.bin",
    ),
    "Varia Suit": Pickup(
        clipdata=0xB6,
        tile_id=0x0,
        palette=[12596, 0, 32767, 32758, 30383, 29003, 22535, 13279, 8895, 4479, 31, 142, 992, 992, 992, 992],
        type=ItemType.EQUIPMENT,
        ability_offset=0x1391E,
        equipment_id=6,
        behavior_type=0x76,
        sprite_id=0x31,
        ability_gfx="Varia.bin",
    ),
    "Gravity Suit": Pickup(
        clipdata=0xB7,
        tile_id=0x0,
        palette=[20680, 1033, 29596, 25370, 20085, 12718, 8490, 23871, 23871, 23871, 23871, 23871, 23871, 23871, 23871, 5319],
        type=ItemType.EQUIPMENT,
        ability_offset=0x1396C,
        equipment_id=7,
        behavior_type=0x77,
        sprite_id=0x58,
        ability_gfx="Gravity.bin",
    ),
    "Morph Ball": Pickup(
        clipdata=0xB8,
        tile_id=0x0,
        palette=[12596, 142, 32767, 32758, 30383, 29003, 22535, 6047, 8895, 4479, 31, 87, 0, 0, 0, 0],
        type=ItemType.EQUIPMENT,
        ability_offset=0x1316C,
        equipment_id=8,
        behavior_type=0x78,
        sprite_id=0x21,
        ability_gfx="Morph.bin",
    ),
    "Speedbooster": Pickup(
        clipdata=0xB9,
        tile_id=0x0,
        palette=[25980, 0, 32767, 25370, 20085, 12718, 8490, 32287, 31807, 16439, 12298, 992, 18420, 5929, 3783, 1442],
        type=ItemType.EQUIPMENT,
        ability_offset=0x13912,
        equipment_id=9,
        behavior_type=0x79,
        sprite_id=0x2B,
        ability_gfx="Speed.bin",
    ),
    "Hi-Jump Boots": Pickup(
        clipdata=0xBA,
        tile_id=0x0,
        palette=[20680, 1033, 29596, 25370, 20085, 12718, 8490, 13279, 8895, 4479, 23, 142, 992, 992, 992, 992],
        type=ItemType.EQUIPMENT,
        ability_offset=0x13916,
        equipment_id=10,
        behavior_type=0x7A,
        sprite_id=0x2D,
        ability_gfx="HiJump.bin",
    ),
    "Screw Attack": Pickup(
        clipdata=0xBB,
        tile_id=0x0,
        palette=[9874, 7302, 32767, 27415, 26221, 16714, 11466, 13279, 8895, 4479, 31, 2163, 992, 992, 992, 992],
        type=ItemType.EQUIPMENT,
        ability_offset=0x1391A,
        equipment_id=11,
        behavior_type=0x7B,
        sprite_id=0x2F,
        ability_gfx="Screw.bin",
    ),
    "Space Jump": Pickup(
        clipdata=0xBC,
        tile_id=0x0,
        palette=[32077, 1033, 29596, 25370, 20085, 12718, 8490, 23871, 23871, 23871, 23871, 23871, 23871, 23871, 23871, 5319],
        type=ItemType.EQUIPMENT,
        ability_offset=0x1396E,
        equipment_id=12,
        behavior_type=0x7C,
        sprite_id=0x59,
        ability_gfx="Space.bin",
    ),
    "Power Grip": Pickup(
        clipdata=0xBD,
        tile_id=0x0,
        palette=[16648, 5317, 32767, 25368, 19026, 10602, 7431, 26623, 18367, 5817, 3537, 1354, 32736, 32352, 29056, 21696],
        type=ItemType.EQUIPMENT,
        ability_offset=0x133AA,
        equipment_id=13,
        behavior_type=0x7D,
        sprite_id=0x4C,
        ability_gfx="Grip.bin",
    ),
    
}

def _get_gfx(gfx_name: str) -> bytes:
    with Path(__file__).parent.joinpath("files", "item_gfx", gfx_name) as f:
        LOG.info("Reading GFX %s", f.as_posix())
        return f.read_bytes()

def patch_item_clipdata(rom: ROM, location: Location, item: Pickup):
    room = Room.get_room(rom, location.area.value, location.room)
    room.get_clip_data(rom)

    width = rom.stream.read_UInt8()
    rom.stream.read_UInt16() # skip height and unk variable
    clip_type = RLE_seek_target(rom, location.y * width + location.x)
    
    if clip_type == RLEResult.DECOMPRESSED:
        if location.hidden:
            rom.stream.write_UInt8(item.clipdata + 0x10) # hidden tank clipdata = normal clipdata + 0x10
        else:
            # TODO figure out why this is needed
            rom.stream.seek_from_current(1)
            rom.stream.write_UInt8(item.clipdata)
    else:
        raise ValueError(f"Clipdata for location {location.rdv_index} has RLEResult {clip_type.value}")
    
def patch_item_bg1(rom: ROM, location: Location, bg1_val: int):
    room = Room.get_room(rom, location.area.value, location.room)
    room.get_bg1(rom)
    width = rom.stream.read_UInt8()
    rom.stream.read_UInt16() # skip height and unk variable
    bg1_type = RLE_seek_target(rom, location.y * width + location.x)

    if bg1_type == RLEResult.NOT_FOUND: 
        raise ValueError(f"Location {location.rdv_index} has OOB clipdata!")
    elif bg1_type == RLEResult.DECOMPRESSED:
        # only patch if not in compressed data
        rom.stream.seek_from_current(1)
        rom.stream.write_UInt8(bg1_val)

def patch_tank_to_tank(rom: ROM, location: Location, item: Pickup):
    # patch BG1 (main tile layer) if not hidden
    if not location.hidden:
        patch_item_bg1(rom, location, item.tile_id)

    # patch clipdata
    patch_item_clipdata(rom, location, item)

def patch_tank_to_ability(rom: ROM, location: Location, item: Pickup):
    room = Room.get_room(rom, location.area.value, location.room)
    # modify tileset
    ts = Tileset.get_tileset(rom, room.ts_num)
    bg1_val = ts.add_equipment(rom, item.equipment_id, item.palette)
    new_ts_num = rom.next_tileset()

    ts.write(rom, new_ts_num)
    room.ts_num = new_ts_num
    rom.stream.seek(room.address)
    rom.stream.write_UInt8(new_ts_num)

    # write clipdata and BG1
    patch_item_clipdata(rom, location, item)
    if not location.hidden:
        patch_item_bg1(rom, location, bg1_val)

def patch_ability_to_item(rom: ROM, location: Location, item: Pickup):
    # replace BehaviorType
    orig_item = ALL_ITEMS[location.orig_item]
    rom.stream.seek(orig_item.ability_offset)
    rom.stream.write_UInt8(item.behavior_type)

    # get base gfx
    base_data: bytearray = _get_gfx("ChozoStatue.bin")
    x: int = 4
    y: int = 4

    # special cases
    if location.orig_item in ["Morph Ball", "Charge Beam"]:
        base_data = bytearray(0x800)
        x = 0
        y = 0
    if location.orig_item == "Power Grip":
        base_data = bytearray(0x1000)
        x = 0
        y = 0
    
    # copy item gfx into base gfx and write item
    item_gfx_data = _get_gfx(item.ability_gfx)
    base_gfx = Gfx(base_data, 32)
    item_gfx = Gfx(item_gfx_data, 6)
    base_gfx.add_gfx(item_gfx, x, y)
    base_gfx.write(rom, orig_item.sprite_id)

    # overwrite palette with new item
    rom.get_sprite_palette_pointer(orig_item.sprite_id)
    rom.stream.follow_pointer()
    
    for i in item.palette:
        rom.stream.write_UInt16(i)



def patch_pickup(rom: ROM, location_idx: int, item: str):
    loc = get_location_by_index(location_idx)
    new_pickup = ALL_ITEMS[item]
    LOG.info("Patching location %i (area %s room %s) to item %s", loc.rdv_index, loc.area.name, hex(loc.room), item)

    if loc.type is ItemType.TANK:
        if new_pickup.type is ItemType.TANK:
            patch_tank_to_tank(rom, loc, new_pickup)
        else:
            patch_tank_to_ability(rom, loc, new_pickup)
    else:
        patch_ability_to_item(rom, loc, new_pickup)