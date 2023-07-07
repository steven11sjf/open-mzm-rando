import dataclasses

@dataclasses.dataclass(frozen=True)
class Offsets:
    AreaHeaderPtr: int
    TilesetPtr: int
    AnimTilesetPtr: int
    AnimGfxPtr: int
    TankGfxOffset: int
    AnimPalettePtr: int
    GenericBgGfxOffset: int
    GenericBgPaletteOffset: int
    GenericSpriteGfxOffset: int
    GenericSpritePaletteOffset: int
    SpriteGfxPtr: int
    SpritePalettePtr: int
    SpriteStats1Ptr: int
    SpriteStats2Ptr: int
    SpriteAI1Ptr: int
    SpriteAI2Ptr: int
    SpritesetPtr: int
    DoorsPtr: int
    AreaConnectionsPtr: int
    DoorEventsPtr: int
    NumOfDoorEventsOffset: int
    LocationNamesPtr: int
    HatchLockEventsPtr: int
    NumOfHatchLockEventsOffset: int
    ScrollsPtr: int
    ClipdataTypePtr: int
    MinimapGfxPtr: int
    MinimapPaletteOffset: int
    MinimapDataPtr: int
    TextGfxPtr: int
    TextPaletteOffset: int
    CharacterWidthsPtr: int
    Languages: list[str]
    DemoInputPtr: int
    DemoRamPtr: int

OffsetForVersion = {
    "ZEROMISSIONEBMXE": Offsets(
        AreaHeaderPtr=0x56480,
        TilesetPtr=0x56250,
        AnimTilesetPtr=0x5E200,
        AnimGfxPtr=0x5E1F8,
        TankGfxOffset=0x752AB4,
        AnimPalettePtr=0x5E320,
        GenericBgGfxOffset=0x5D940C,
        GenericBgPaletteOffset=0x5DFE20,
        GenericSpriteGfxOffset=0x32BAC8,
        GenericSpritePaletteOffset=0x32BA08,
        SpriteGfxPtr=0xE070,
        SpritePalettePtr=0xE07C,
        SpriteStats1Ptr=0xE684,
        SpriteStats2Ptr=0xE654,
        SpriteAI1Ptr=0xD01C,
        SpriteAI2Ptr=0xCFCC,
        SpritesetPtr=0xE060,
        DoorsPtr=0x569B0,
        AreaConnectionsPtr=0x5EEB8,
        DoorEventsPtr=0x5EFEC,
        NumOfDoorEventsOffset=0x5EFE4,
        LocationNamesPtr=0x11F04,
        HatchLockEventsPtr=0x5F70C,
        NumOfHatchLockEventsOffset=0x3602D8,
        ScrollsPtr=0x5849C,
        ClipdataTypePtr=0x56310,
        MinimapGfxPtr=0x6A6B4,
        MinimapPaletteOffset=0x411360,
        MinimapDataPtr=0x6B174,
        TextGfxPtr=0x6E554,
        TextPaletteOffset=0x3FD030,
        CharacterWidthsPtr=0x6E478,
        Languages=["Japanese", "Hiragana", "English"],
        DemoInputPtr=0x60C14,
        DemoRamPtr=0x753C8,
    )
}