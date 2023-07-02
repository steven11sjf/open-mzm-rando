from construct import (Struct, Int8ul, Int16ul)

from open_mzm_rando.construct_patching.rom_data_section import Pointer
from open_mzm_rando.construct_patching import data_enums

ActiveScroll = Struct(
    SamusWithinScrollFlag = Int8ul,
    XEnd = Int16ul,
    XStart = Int16ul,
    YStart = Int16ul,
    YEnd = Int16ul
)

AmmoDigits = Struct(
    OnesPlace = Int8ul,
    TensPlace = Int8ul,
    HundredsPlace = Int8ul,
    ThousandsPlace = Int8ul
)

AnimatedGraphicsEntry = Struct(
    AnimType = Int8ul,
    FramesPerState = Int8ul,
    NumOfStates = Int8ul,
    GfxPointer = Pointer
)

AnimatedPaletteAndTilesetNumber = Struct(
    AnimatedPaletteNumber = Int8ul,
    AnimatedTilesetNumber = Int8ul
)

AnimatedPaletteEntry = Struct(
    AnimType = Int8ul,
    FramesPerState = Int8ul,
    NumOfStates = Int8ul,
    PalettePtr = Pointer
)

AnimatedPaletteTiming = Struct(
    Counter = Int8ul,
    State = Int8ul,
    unk_02 = Int8ul,
)

AreaConnection = Struct(
    SourceArea = data_enums.AreaID,
    SourceDoor = Int8ul,
    DestinationArea = data_enums.AreaID
)