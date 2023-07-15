from __future__ import annotations
import dataclasses

from open_mzm_rando.patching.base_component import BaseComponent
from open_mzm_rando.patching.ROM import ROM


# list of all RoomEntry
ROOMS: dict[str, Room] = {}

@dataclasses.dataclass(kw_only=True)
class Room(BaseComponent):
    region: int # enum for region (0=brinstar, etc)
    room: int # index of room in region
    BG0: int # pointer to BG0 (foreground), offset +0x8
    BG1: int # pointer to BG1 (main layer), offset +0xC
    BG2: int # pointer to BG2 (behind main layer), offset +0x10
    BG3: int # pointer to BG3 (scrolling background), offset +0x18
    clipdata: int # pointer to Clipdata, offset +0x14
    map_x: int # x coordinate on map, offset +0x35
    map_y: int # y coordinate on map, offset +0x36

    
    # seeks stream from anywhere to the RoomEntry for a region
    @staticmethod
    def get_room(rom: ROM, region: int, room: int) -> Room:
        """seeks stream from anywhere to the requested RoomEntry; returns a pointer to the room"""
        room_key = f"a{region}r{room}"
        if room_key in ROOMS.keys():
            room = ROOMS[room_key]
            rom.stream.seek(room.address)
            return room
        else:
            return Room._create_room(rom, region, room, room_key)
    
    def get_clip_data(self, rom: ROM):
        """seeks stream from RoomEntry to its clipdata"""
        rom.stream.seek(self.clipdata)
    
    
    def get_bg1(self, rom: ROM):
        """seeks stream from RoomEntry to its bg1"""
        rom.stream.seek(self.BG1)

    @staticmethod
    def _create_room(rom: ROM, region: int, room: int, key: str) -> Room:
        # parse data
        rom.get_region_header(region)
        rom.stream.seek_from_current(room * 0x3C)
        
        ptr = rom.stream.stream.tell()
        rom.stream._read(8) # skip
        bg0 = rom.stream.read_Pointer()
        bg1 = rom.stream.read_Pointer()
        bg2 = rom.stream.read_Pointer()
        clip = rom.stream.read_Pointer()
        bg3 = rom.stream.read_Pointer()
        rom.stream._read(19) # skip
        map_x = rom.stream.read_UInt8()
        map_y = rom.stream.read_UInt8()

        # make entry
        new_room = Room(
            address=ptr,
            region=region,
            room=room,
            BG0=bg0,
            BG1=bg1,
            BG2=bg2,
            BG3=bg3,
            clipdata=clip,
            map_x=map_x,
            map_y=map_y
        )
        ROOMS[key] = new_room
        rom.stream.seek(new_room.address)
        return new_room