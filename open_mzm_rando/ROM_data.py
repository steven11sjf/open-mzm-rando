from enum import Enum

class Offsets(Enum):
    AREA_ROOM_ENTRY_OFFSET = 0x75FAC4
    NumTanksPerAreaOffset = 0x3459A0
    TankCollectionInfoOffset = 0x3459A0
    SpriteGfxOffset = 0x75EBF8
    SpritePaletteOffset = 0x75EEF0
    SpritesetOffset = 0x75F31C
    AnimPaletteOffset = 0x35FBFC
    ChozoTargetOffset = 0x40DF78
    MinimapDataOffset = 0x7601EC
    CharWidthsOffset = 0x40D7B0

    TilesetPtr = 0x56250
    AnimTilesetPtr = 0x5E200
    AnimGfxPtr = 0x5E1F8
    Tilemap400Ptr = 0x56318