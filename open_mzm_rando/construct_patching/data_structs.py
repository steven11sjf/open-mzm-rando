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

BG0Movement = Struct(
    Type = Int8ul,
    YPositionOffset = Int8ul,
    Unk1=Int8ul,
    Unk2=Int8ul,
    XPositionOffset=Int16ul,
    SnowflakesRelated=Int16ul
)

BG0WaterMovement = Struct(
    MovingFlag=Int8ul,
    Stage=Int8ul,
    LoopCounter=Int8ul,
    YPositionOffset=Int8ul
)

BG2Movement = Struct(
    XPositionOffset=Int16ul,
    YPositionOffset=Int16ul
)

BG3Movement = Struct(
    Direction=data_enums.Direction, # my guess
    Counter=Int8ul,
    MoveLeftToRightStage=Int8ul,
    XPositionOffset=Int16ul
)

BGPositions = Struct(
    BG0XPosition=Int16ul,
    BG0YPosition=Int16ul,
    BG1XPosition=Int16ul,
    BG1YPosition=Int16ul,
    BG2XPosition=Int16ul,
    BG2YPosition=Int16ul,
    BG3XPosition=Int16ul,
    BG3YPosition=Int16ul,
    DoorTransitionXPosition=Int16ul,
    DoorTransitionYPosition=Int16ul
)

BGPtrsAndDimensions = Struct(
    DecompressedBG0Ptr=Pointer,
    WidthOfBG0InBlocks=Int16ul,
    HeightOfBG0InBlocks=Int16ul,
    DecompressedBG1Ptr=Pointer,
    WidthOfBG1InBlocks=Int16ul,
    HeightOfBG1InBlocks=Int16ul,
    DecompressedBG2Ptr=Pointer,
    WidthOfBG1InBlocks=Int16ul,
    HeightOfBG2InBlocks=Int16ul,
    DecompressedClipdataPtr=Pointer,
    WidthOfClipdataInBlocks=Int16ul,
    HeightOfClipdataInBlocks=Int16ul
)

BLDALPHAData = Struct(
    BackupOfDISPCNT_NonGameplay=Int16ul,
    BackupOfBLDCNT_NonGameplay=Int16ul,
    BackupOfBLDALPHA_NonGameplay=Int16ul,
    BackupOfWININ_H_NonGameplay=Int8ul,
    BackupOfWINOUT_L_NonGameplay=Int8ul,
    BackupOfBG0CNT_WriteOnly=Int16ul,
    BackupOfBG1CNT=Int16ul,
    BackupOfBG2CNT=Int16ul,
    BackupOfBG3CNT=Int16ul,
    BackupOfBG0CNT=Int16ul,
)

BombChainData = Struct(
    CurrBlockOffset=Int8ul,
    StartingXPosition=Int8ul,
    StartingYPosition=Int8ul,
    Status=Int8ul
)

BossMapIcon = Struct(
    EventNum=data_enums.Event,
    BossIconNum=Int8ul,
    MapXCoordinate=Int8ul,
    MapYCoordinate=Int8ul,
    PixelOffset=Int8ul
)

BossWork = Struct(
    Work1=Int16ul,
    Work2=Int16ul,
    Work3=Int16ul,
    Work4=Int16ul,
    Work5=Int16ul,
    Work6=Int16ul,
    Work7=Int16ul,
    Work8=Int16ul,
    Work9=Int16ul,
    Work10=Int16ul,
    Work11=Int16ul,
)

BoxBounds = Struct(
    LeftOffset=Int16ul,
    TopOffset=Int16ul,
    RightOffset=Int16ul,
    BottomOffset=Int16ul
)

BreakingOrReformingBlock = Struct(
    ExistsFlag=Int8ul,
    Stage=Int8ul,
    BlockType=Int8ul,
    XPosition=Int8ul,
    YPosition=Int8ul,
    Timer=Int16ul
)

### NOTE there are like a hundred of these im just going to do the ones i need
###      for parse/build since a lot of these are RAM values i think

SoundDataEntry = Struct(
    SoundHeaderPtr=Pointer,
    TrackGroupNum1=Int16ul,
    TrackGroupNum2=Int16ul
)