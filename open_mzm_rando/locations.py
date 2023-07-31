import dataclasses

from enum import Enum
from open_mzm_rando.constants import Region

class ItemType(Enum):
    EQUIPMENT = "Equipment"
    TANK = "Tank"


@dataclasses.dataclass(frozen=True)
class Location:
    area: Region
    room: int
    x: int
    y: int
    rdv_index: int
    type: ItemType
    hidden: bool
    orig_item: str = ""

ALL_LOCATIONS: list[Location] = [
    Location(
        area=Region.BRINSTAR,
        room=0,
        x=11,
        y=27,
        rdv_index=0,
        type=ItemType.EQUIPMENT,
        hidden=False,
        orig_item="Morph Ball"
    ),
    Location(
        area=Region.BRINSTAR,
        room=0x1,
        x=13,
        y=7,
        rdv_index=1,
        type=ItemType.TANK,
        hidden=False
    ),
    Location(
        area=Region.BRINSTAR,
        room=0x2,
        x=29,
        y=2,
        rdv_index=2,
        type=ItemType.TANK,
        hidden=True
    ),
    Location(
        area=Region.BRINSTAR,
        room=0xC,
        x=54,
        y=6,
        rdv_index=9,
        type=ItemType.TANK,
        hidden=False
    )
]

def get_location_by_index(idx: int) -> Location:
    for loc in ALL_LOCATIONS:
        if loc.rdv_index == idx:
            return loc
    return None