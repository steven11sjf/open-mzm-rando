import dataclasses
from pathlib import Path
import json

from open_mzm_rando.patching.ROM import ROM
from open_mzm_rando.patching.Room import Room
from open_mzm_rando.patching.run_length_encoding import RLE_seek_target, RLEResult


ROM_PATH = "e:/Roms/GBA/MF.gba" # Put your path here!
ROOM_NAME_JSON: str = "d:/randovania-dev/mzm_db_dumps/area_names_dict.json" # renames rooms to provided names
DUMP_PATH = "d:/randovania-dev/mzm_db_dumps" # directory db dumps are sent to

# consts
TILE_SIZE_RDV = 16.0 # rdv units per tile
# global vars
item_idx = 0
room_names = None

@dataclasses.dataclass
class AreaData:
    name: str
    idx: int
    room_count: int
    door_offset: int
    door_count: int

@dataclasses.dataclass
class ItemData:
    type: str
    x: int
    y: int
    idx: int
    hidden: bool

@dataclasses.dataclass
class DoorData:
    offset: str
    idx: int
    type: int
    dock_type: str
    door_type: str
    src_room: int
    x: float
    y: float
    len_x: int
    len_y: int
    dst_area: int
    dst_room: int
    dst_door: int
    event: int

@dataclasses.dataclass
class RoomData:
    room_num: int
    width: int
    height: int
    tank_data: list[ItemData]
    door_data: list[DoorData]
    
all_areas_data: dict[int, list[RoomData]] = None

AREA_DATA = {
    "MainDeck": AreaData(
        name="Main Deck",
        idx=0,
        room_count=0x57,
        door_offset=0x3c0030,
        door_count=0xcc,
    ),
    "Sector1": AreaData(
        name="Sector 1",
        idx=1,
        room_count=0x36,
        door_offset=0x3c09d8,
        door_count=0x73,
    ),
    "Sector2": AreaData(
        name="Sector2",
        idx=2,
        room_count=0x3d,
        door_offset=0x3c0f48,
        door_count=0x92,
    ),
    "Sector3": AreaData(
        name="Sector3",
        idx=3,
        room_count=0x27,
        door_offset=0x3c162c,
        door_count=0x5a,
    ),
    "Sector4": AreaData(
        name="Sector 4",
        idx=4,
        room_count=0x30,
        door_offset=0x3c204c,
        door_count=0x76,
    ),
    "Sector5": AreaData(
        name="Sector 5",
        idx=5,
        room_count=0x34,
        door_offset=0x3c1a70,
        door_count=0x7c,
    ),
    "Sector6": AreaData(
        name="Sector 6",
        idx=6,
        room_count=0x29,
        door_offset=0x3c25e0,
        door_count=0x5e,
    )
}

CLIP_VALS = {
    0x62: "Missile Tank",
    0x63: "Energy Tank",
    0x64: "Hidden Missile Tank",
    0x65: "Hidden Energy Tank",
    0x66: "Underwater Missile Tank",
    0x67: "Underwater Energy Tank",
    0x68: "Power Bomb Tank",
    0x69: "Hidden Power Bomb Tank",
    0x6a: "Underwater Power Bomb Tank",
}

DOOR_CLIPS = {
    # 0x20: "Door Transition",
    # 0x27: "Door Transition Up",
    # 0x28: "Door Transition Down",
    0x30: "Power Beam Door",
    0x31: "Power Beam Door",
    0x32: "Power Beam Door",
    0x33: "Power Beam Door",
    0x34: "Power Beam Door",
    0x35: "Power Beam Door",
    0x36: "Power Beam Door",
    0x40: "Missile Door",
    0x46: "Super Missile Door",
    0x4C: "Power Bomb Door",

}

def RLE_find_target_bytes_in_clip(rom: ROM, targets: dict[int, str]) -> list[ItemData]:
    global item_idx
    count = 0
    stream = rom.stream
    
    width = stream.read_UInt8()
    height = stream.read_UInt8()
    rom.stream.seek_from_current(1)
    
    datas = []
    end = width * height
    while(count < end):
        byte = stream.read_UInt8()
        if byte > 0x80:
            # repeat next clipdata byte for (byte-0x80) tiles
            count += byte - 0x80
            val = stream.read_UInt8()

            if val in targets:
                raise ValueError(f"Encountered a compressed run of {targets[val]}!")
        else:
            if byte == 0:
                raise ValueError(f"RLE seek encountered a run of zero at {hex(count)}- check your offsets!")
            # read the next `byte` bytes
            for _ in range(byte):
                val = stream.read_UInt8()
                count += 1
                if val in targets:
                    x = count % width - 1
                    y = count // width
                    datas.append(ItemData(
                        type=targets[val],
                        x=x,
                        y=y,
                        idx=item_idx,
                        hidden=(val > 0x60)
                    ))
                    item_idx += 1
    
    return datas

def parse_doors_for_area(rom: ROM, area: AreaData, all_rooms: list[RoomData]):
    for door_num in range(area.door_count):
        rom.stream.seek(area.door_offset + (door_num * 0xC))
        type = rom.stream.read_UInt8()
        src_room = rom.stream.read_UInt8()
        x1 = rom.stream.read_UInt8()
        x2 = rom.stream.read_UInt8()
        y1 = rom.stream.read_UInt8()
        y2 = rom.stream.read_UInt8()
        dst_door = rom.stream.read_UInt8()

        len_x = x2-x1+1
        len_y = y2-y1+1

        dock_type: str = None
        door_type = None
        if len_x == 1 and len_y == 4:
            dock_type = "door"

            Room.get_room(rom, area.idx, src_room).get_clip_data(rom)
            w = rom.stream.read_UInt8()
            rom.stream.read_UInt16()
            pos = rom.stream.stream.tell()
            
            # check left
            res = RLE_seek_target(rom, y1 * w + x1 - 1)
            if res == RLEResult.DECOMPRESSED:
                rom.stream.read_UInt8()
                t = rom.stream.read_UInt8()
                if t in DOOR_CLIPS:
                    door_type = DOOR_CLIPS[t]
            # check right
            if not door_type:
                rom.stream.seek(pos)
                res = RLE_seek_target(rom, y1 * w + x1 + 1)
                if res == RLEResult.DECOMPRESSED:
                    rom.stream.read_UInt8()
                    t = rom.stream.read_UInt8()
                    if t in DOOR_CLIPS:
                        door_type = DOOR_CLIPS[t]
            
            # just make a basic dock if it's neither
            if not door_type:
                dock_type = "dock"
                door_type = "Access Open"
        elif len_x == 1 and len_y == 1:
            dock_type = "tunnel"
            door_type = "Tunnel"
        else:
            dock_type = "dock"
            door_type = "Access Open"

        all_rooms[src_room].door_data.append(DoorData(
            offset=hex(area.door_offset + (0xC * door_num)),
            idx=door_num,
            type=type,
            dock_type=dock_type,
            door_type=door_type,
            src_room=src_room,
            x=(x1+x2)/2,
            y=(y1+y2)/2,
            len_x=len_x,
            len_y=len_y,
            dst_area=area.idx,
            dst_room=None,
            dst_door=dst_door,
            event=0,
        ))

def parse_rooms_for_area(rom: ROM, area: AreaData) -> list[RoomData]:

    all_rooms = []
    print(f"Starting item index for {area.name}: {item_idx}")
    for room_idx in range(area.room_count):
        # get clipdata
        Room.get_room(rom, area.idx, room_idx).get_clip_data(rom)
        width = rom.stream.read_UInt8()
        height = rom.stream.read_UInt8()
        rom.stream.seek_from_current(-2)
        tank_data = RLE_find_target_bytes_in_clip(rom, CLIP_VALS)


        all_rooms.append(RoomData(
            room_num=room_idx,
            width=width,
            height=height,
            tank_data=tank_data,
            door_data=[]
        ))
    print(f"Ending item idx for {area.name}: {item_idx}")
    return all_rooms

def add_area_connections(rom: ROM, all_areas: dict[int, list[RoomData]]):
    for area_conn_idx in range(0x22):
        # read conn data
        rom.stream.seek(0x3c8b90 + (area_conn_idx * 0x3))
        print(hex(rom.stream.stream.tell()))
        src_area = rom.stream.read_UInt8()
        src_door = rom.stream.read_UInt8()
        dst_area = rom.stream.read_UInt8()
        if dst_area > 6:
            raise ValueError("???" + hex(area_conn_idx) + "          " + hex(rom.stream.stream.tell()))

        # find door in area
        area = all_areas[src_area]
        src_door_data: DoorData = None
        for room in area:
            for door in room.door_data:
                if door.idx == src_door:
                    src_door_data = door
                    break
            if src_door_data:
                break
        if not src_door_data:
            raise ValueError(f"Door {src_door} not found!")
        
        # set new area
        src_door_data.dst_area = dst_area
        if dst_area > 6:
            raise ValueError("WTF")
        
def add_door_dst_rooms(rom: ROM, all_areas: dict[int, list[RoomData]]):
    # iterate all doors
    for area in all_areas.values():
        for room in area:
            for door in room.door_data:
                dst_door = door.dst_door
                
                # iterate to find area
                dst_room = None
                print(door)
                for room in all_areas[door.dst_area]:
                    for otherdoor in room.door_data:
                        if otherdoor.idx == dst_door:
                            dst_room = room.room_num
                            break
                    if dst_room:
                        break
                
                door.dst_room = dst_room

def generate_all_areas() -> dict[int, list[RoomData]]:
    # get the rom
    path = Path(ROM_PATH)
    rom = ROM(path)
    all_areas: dict[int, list[RoomData]] = {}

    for area in AREA_DATA.values():
        area_rooms = parse_rooms_for_area(rom, area)
        parse_doors_for_area(rom, area, area_rooms)
        all_areas[area.idx] = area_rooms
    
    # fix area connections
    add_area_connections(rom, all_areas)
    add_door_dst_rooms(rom, all_areas)
    
    return all_areas

###############################
###############################
#####                     #####
#####   JSON GENERATION   #####
#####                     #####
###############################
###############################

def idx_to_region(idx: int):
    if idx == 0:
        return "Brinstar"
    if idx == 1:
        return "Kraid"
    if idx == 2:
        return "Norfair"
    if idx == 3:
        return "Ridley"
    if idx == 4:
        return "Tourian"
    if idx == 5:
        return "Crateria"
    if idx == 6:
        return "Chozodia"
    raise ValueError("Bad idx!")

def get_room_name(area: int, room: int):
    global room_names

    area_name = None
    for a in AREA_DATA.values():
        if a.idx == area:
            area_name = a.name
    
    room_name = f"A_{area_name}_R_{hex(room)}"
    if room_names and (area_name in room_names) and (hex(room) in room_names[area_name]):
        rn = room_names[area_name][hex(room)]
        if rn != "":
            room_name = rn
    
    return room_name

def get_door(area: int, door: int) -> DoorData:
    global all_areas_data

    areadata = all_areas_data[area]
    for room in areadata:
        for doordata in room.door_data:
            if doordata.idx == door:
                return doordata

def game_xy_to_rdv_coordinate(item, width_room: int, height_room: int) -> dict:
    # rdv's x is same as game's x, multiplied by px per tile. add 0.5 to center. 
    rdv_x = (item.x + 0.5) * TILE_SIZE_RDV
    
    # rdv's y is more complex; inverted y axis. 
    rdv_y = (height_room - 0.5 - item.y) * TILE_SIZE_RDV

    return {
        "x": rdv_x,
        "y": rdv_y,
        "z": 0.0
    }

def generate_area_json(area: AreaData, rooms: list[RoomData]):
    global room_names

    res = {}
    res["name"] = area.name
    res["extra"] = { "area_id": area.idx }

    res["areas"] = {}
    for roomdata in rooms:
        room_name = get_room_name(area.idx, roomdata.room_num)
        room = {}
        room["default_node"] = None
        room["extra"] = {
            "map_name": f"{area.name}{roomdata.room_num}",
            "room_id": roomdata.room_num
        }
        room["nodes"] = {}
        
        for item in roomdata.tank_data:
            itemname = f"Pickup ({item.type})"
            if itemname in room["nodes"]:
                itemname = f"Pickup ({item.type} 2)"
            itemnode = {
                "node_type": "pickup",
                "heal": False,
                "coordinates": game_xy_to_rdv_coordinate(item, roomdata.width, roomdata.height),
                "description": "",
                "layers": [ "default" ],
                "extra": {},
                "valid_starting_location": False,
                "pickup_index": item.idx,
                "location_category": "minor",
                "connections": {}
            }
            room["nodes"][itemname] = itemnode
        
        for door in roomdata.door_data:
            doorname = f"{door.dock_type.capitalize()} to {get_room_name(door.dst_area, door.dst_room)}"
            other_end = get_door(door.dst_area, door.dst_door)
            doornode = {
                "node_type": "dock",
                "heal": False,
                "coordinates": game_xy_to_rdv_coordinate(door, roomdata.width, roomdata.height),
                "description": "",
                "layers": [ "default" ],
                "extra": {
                    "door_idx": door.idx
                },
                "valid_starting_location": False,
                "dock_type": door.dock_type,
                "default_connection": {
                    "region": idx_to_region(door.dst_area),
                    "area": get_room_name(door.dst_area, door.dst_room),
                    "node": f"{other_end.dock_type.capitalize()} to {get_room_name(other_end.dst_area, other_end.dst_room)}"
                },
                "default_dock_weakness": door.door_type,
                "exclude_from_dock_rando": False,
                "incompatible_dock_weaknesses": [],
                "override_default_open_requirement": None,
                "override_default_lock_requirement": None,
                "connections": {}
            }
            if doorname not in room["nodes"]:
                room["nodes"][doorname] = doornode
            else:
                room["nodes"][f"{doorname} ({door.idx})"] = doornode

        res["areas"][room_name] = room
    
    json_path = Path(DUMP_PATH).joinpath(f"{area.name}.json")
    with open(json_path, "w") as file:
        json.dump(res, file, indent=4)


def convert_to_jsons(data: dict[int, list[RoomData]]):
    for area_idx, rooms in data.items():
        area = None
        for a in AREA_DATA.values():
            if a.idx == area_idx:
                area = a
                break
        generate_area_json(area, rooms)

def make_blank_room_name_json():
    res = {}
    for area in AREA_DATA.values():
        area_name = area.name
        areadict = {}
        for roomidx in range(area.room_count):
            areadict[hex(roomidx)] = ""
        res[area_name] = areadict
    
    json_path = Path(DUMP_PATH).joinpath(f"area_names_dict.json")
    with open(json_path, "w") as file:
        json.dump(res, file, indent=4)

@dataclasses.dataclass
class PickupThingy:
    area: str
    room: int
    item: ItemData

def generate_location_data(data: dict[int, list[RoomData]]):
    items: list[PickupThingy] = []

    for area_idx, rooms in data.items():
        area = None
        for a in AREA_DATA.values():
            if a.idx == area_idx:
                area = a.name
                break
        
        for room in rooms:
            for item in room.tank_data:
                items.append(PickupThingy(area=area, room=room.room_num, item=item))
    
    res = "ALL_LOCATIONS: list[Location] = [\n"
    for it in items:
        res += "\tLocation(\n"
        res += f"\t\tarea=Region.{it.area.upper()},\n"
        res += f"\t\troom={hex(it.room)},\n"
        res += f"\t\tx={it.item.x},\n"
        res += f"\t\ty={it.item.y},\n"
        res += f"\t\trdv_index={it.item.idx},\n"
        res += "\t\ttype=ItemType.TANK,\n"
        res += f"\t\thidden={it.item.hidden}\n"
        res += f"\t),\n"
    res += "]\n"

    py_path = Path(DUMP_PATH).joinpath("locations.py")
    py_path.write_text(res)

def main():
    # get room name dict if it exists
    global room_names
    global all_areas_data
    if ROOM_NAME_JSON:
        with open(Path(ROOM_NAME_JSON)) as f:
            room_names = json.load(f)

    all_areas_data = generate_all_areas()
    convert_to_jsons(all_areas_data)

    generate_location_data(all_areas_data)
main()

# enable to generate a blank room name json in DUMP_PATH\area_names_dict.json
# make_blank_room_name_json()