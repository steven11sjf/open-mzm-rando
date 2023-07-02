from construct import (Enum, Int8ul, Int16ul, Int32ul)

AreaBitFlags = Enum(
    Int8ul,
    BRINSTAR=0x1,
    KRAID=0x2,
    NORFAIR=0x4,
    RIDLEY=0x8,
    TOURIAN=0x10,
    CRATERIA=0x20,
    CHOZODIA=0x40
)

AreaID = Enum(
    Int8ul,
    BRINSTAR=0,
    KRAID=1,
    NORFAIR=2,
    RIDLEY=3,
    TOURIAN=4,
    CRATERIA=5,
    CHOZODIA=6,
)

ArmCannonDirection = Enum(
    Int8ul,
    FORWARD=0,
    DIAGONAL_UP=1,
    DIAGONAL_DOWN=2,
    UP=3,
    DOWN=4,
    NONE=5
)

BGProperty = Enum(
    Int8ul,
    NONE=0,
    RLE_COMPRESSED=0x10,
    MOVING_BG2=0x31,
    LZ77_COMPRESSED=0x40,
    DARK_ROOM=0x45,
    BG3_STARTS_FROM_BOTTOM=0x46
)

BackgroundFade = Enum(
    Int8ul,
    NOTHING=0,
    FADE_TO_BLACK=1,
    FADE_TO_WHITE=2
)

BeamBombStatus = Enum(
    Int8ul,
    LONG_BEAM=0x1,
    ICE_BEAM=0x2,
    WAVE_BEAM=0x4,
    PLASMA_BEAM=0x8,
    CHARGE_BEAM=0x10,
    BOMBS=0x80
)

BeforeAfterEventFlag = Enum(
    Int8ul,
    AFTER=0,
    BEFORE=1
)

BlockReformType = Enum(
    Int8ul,
    NONE=0,
    NO_OR_NEVER_REFORM=1,
    REFORM=2,
    BOMB_CHAIN=3,
    TANK=4
)

BlockWeaknessFlags = Enum(
    Int8ul,
    NONE=0x0,
    BEAM=0x1,
    BOMB_OR_PISTOL=0x2,
    MISSILE=0x4,
    SUPER_MISSILE=0x8,
    POWER_BOMB=0x10,
    SPEEDBOOST=0x20,
    SPEEDBOOST_GROUND=0x40,
    SCREW_ATTACK=0x80,
    BOMB_CHAIN=0x1000 # seems to not fit in 1B? NOTE
)

BombChainType = Enum(
    Int8ul,
    VERTICAL1=0,
    VERTICAL2=1,
    VERTICAL3=2,
    VERTICAL4=3,
    HORIZONTAL1=4,
    HORIZONTAL2=5,
    HORIZONTAL3=6,
    HORIZONTAL4=7
)

BreakableBlockType = Enum(
    Int8ul,
    NONE=0,
    SHOT_BLOCK_REFORM=0x1,
    BOMB_BLOCK_REFORM=0x2,
    SPEEDBOOSTER_REFORM=0x3,
    CRUMBLE=0x4,
    SLOW_CRUMBLE=0x5,
    MISSILE_NEVERREFORM=0x6,
    MISSILE_NOREFORM=0x7,
    SUPERMISSILE_NEVERREFORM=0x8,
    SUPERMISSILE_NOREFORM=0x9,
    POWERBOMB_NEVERREFORM=0xA,
    SCREWATTACK_NOREFORM=0xB,
    SPEEDBOOSTER_NOREFORM=0xC,
    BOMB_NEVERREFORM=0xD,
    VERTICALBOMBCHAIN1=0xE,
    VERTICALBOMBCHAIN2=0xF,
    VERTICALBOMBCHAIN3=0x10,
    VERTICALBOMBCHAIN4=0x11,
    HORIZONTALBOMBCHAIN1=0x12,
    HORIZONTALBOMBCHAIN2=0x13,
    HORIZONTALBOMBCHAIN3=0x14,
    HORIZONTALBOMBCHAIN4=0x15,
)

ButtonInput = Enum(
    Int16ul,
    A=0x1,
    B=0x2,
    SELECT=0x4,
    START=0x8,
    RIGHT=0x10,
    LEFT=0x20,
    UP=0x40,
    DOWN=0x80,
    R=0x100,
    L=0x200
)

ChozoHintCheckType = Enum(
    Int8ul,
    BEAM_BOMBS=0,
    SUIT_MISC=1,
    EVENT=2
)

ChozoHintIcon = Enum(
    Int8ul,
    TARGET=0x1,
    UP_ELEVATOR=0x2,
    DOWN_ELEVATOR=0x3,
    GREEN_FLAME=0x8,
    GREEN_FLAME_MOVESUPDOWN=0xA,
    PINK_FLAME=0xC,
    PINK_FLAME_MOVESUPDOWN=0xE
)

ChozoHintLocation = Enum(
    Int16ul,
    LONG_BEAM=0x1,
    BOMBS=0x2,
    ICE_BEAM=0x4,
    SPEED_BOOSTER=0x8,
    HI_JUMP=0x10,
    VARIA_SUIT=0x20,
    WAVE_BEAM=0x40,
    SCREW_ATTACK=0x80,
    KRAID_FLAME=0x100,
    RIDLEY_FLAME=0x200
)

ClipdataAffectingAction = Enum(
    Int8ul,
    REMOVE_SOLID=0x1,
    MAKE_SOLID=0x2,
    MAKE_STOP_ENEMY=0x3,
    MAKE_NON_POWERGRIP=0x4,
    BOMBCHAIN_UNUSED=0x5,
    UNUSED=0x6,
    BEAM=0x7,
    BOMB_PISTOL=0x8,
    MISSILE=0x9,
    SUPER_MISSILE=0xA,
    POWER_BOMB=0xB,
    SPEEDBOOST=0xC,
    SPEEDBOOST_GROUND=0xD,
    SCREW_ATTACK=0xE,
    BOMB_CHAIN=0xF
)

ClipdataBehaviorType = Enum(
    Int8ul,
    AIRORSOLID=0x0,
	ELEVATORDOWNBLOCK=0x1,
	ELEVATORUPBLOCK=0x2,
	DOORTRANSITIONBLOCK=0x3,
	VERTICALUPTRANSITIONBLOCK=0x4,
	VERTICALDOWNTRANSITIONBLOCK=0x5,
	NONPOWERGRIP=0x6,
	STOPENEMYBLOCK_SOLID=0x7,
	SPACEPIRATEZONELINE=0x8,
	SPACEPIRATEWALLJUMPPOINT=0x9,
	SHOTBLOCK_NEVERREFORM=0x10,
	TOPLEFTSHOTBLOCK_NEVERREFORM=0x11,
	TOPRIGHTSHOTBLOCK_NEVERREFORM=0x12,
	BOTTOMLEFTSHOTBLOCK_NEVERREFORM=0x13,
	BOTTOMRIGHTSHOTBLOCK_NEVERREFORM=0x14,
	SHOTBLOCK_NOREFORM=0x15,
	TOPLEFTSHOTBLOCK_NOREFORM=0x16,
	TOPRIGHTSHOTBLOCK_NOREFORM=0x17,
	BOTTOMLEFTSHOTBLOCK_NOREFORM=0x18,
	BOTTOMRIGHTSHOTBLOCK_NOREFORM=0x19,
	SHOTBLOCK_REFORM=0x1A,
	BOMBBLOCK_NEVERREFORM=0x1B,
	BOMBBLOCK_REFORM=0x1C,
	MISSILEBLOCK_NEVERREFORM=0x1D,
	MISSILEBLOCK_NOREFORM=0x1E,
	SUPERMISSILEBLOCK_NEVERREFORM=0x1F,
	SUPERMISSILEBLOCK_NOREFORM=0x20,
	SPEEDBOOSTBLOCK_NOREFORM=0x21,
	SPEEDBOOSTBLOCK_REFORM=0x22,
	CRUMBLEBLOCK=0x23,
	POWERBOMBBLOCK_NEVERREFORM=0x24,
	SCREWATTACKBLOCK_NOREFORM=0x25,
	VERTICALBOMBCHAIN1=0x26,
	VERTICALBOMBCHAIN2=0x27,
	VERTICALBOMBCHAIN3=0x28,
	VERTICALBOMBCHAIN4=0x29,
	HORIZONTALBOMBCHAIN1=0x2A,
	HORIZONTALBOMBCHAIN2=0x2B,
	HORIZONTALBOMBCHAIN3=0x2C,
	HORIZONTALBOMBCHAIN4=0x2D,
	SLOWCRUMBLEBLOCK=0x2E,
	HIDDENENERGYTANK=0x34,
	HIDDENMISSLETANK=0x35,
	HIDDENSUPERMISSLETANK=0x36,
	HIDDENPOWERBOMBTANK=0x37,
	ENERGYTANK=0x38,
	MISSLETANK=0x39,
	SUPERMISSLETANK=0x3A,
	POWERBOMBTANK=0x3B,
	UNDERWATERENERGYTANK=0x3C,
	UNDERWATERMISSILETANK=0x3D,
	UNDERWATERSUPERMISSILETANK=0x3E,
	UNDERWATERPOWERBOMBTANK=0x3F,
	WATER=0x40,
	STRONGLAVA=0x41,
	WEAKLAVA=0x42,
	ACID=0x43,
	BG0TRIGGEROPAQUE=0x44,
	BG0TRIGGERTRANSPARENTLEVEL1=0x45,
	BG0TRIGGERTRANSPARENTLEVEL2=0x46,
	BG0TRIGGERTRANSPARENTLEVEL3=0x47,
	BG0TRIGGERTRANSPARENTLEVEL4=0x48,
	BG0TRIGGERTRANSPARENTLEVEL5=0x49,
	BG0TRIGGER100TRANSPARENT=0x4A,
	BG0TRIGGERBRIGHTER1=0x4B,
	BG0TRIGGERBRIGHTER2=0x4C,
	BG0TRIGGERBRIGHTER3=0x4D,
	BG0TRIGGERBRIGHTER4=0x4E,
	BG0TRIGGERDEFAULTTRANSPARENCY=0x4F,
	WETGROUND=0x50,
	DUSTYGROUND=0x51,
	UNUSEDSOLID_1E=0x52,
	BUBBLYGROUND=0x53,
	VERYDUSTYGROUND=0x54,
	GRAYDOOR=0x80,
	REGULARDOOR=0x81,
	MISSILEDOOR=0x82,
	SUPERMISSILEDOOR=0x83,
	POWERBOMBDOOR=0x84
)

ClipdataCollisionType = Enum(
    Int8ul,
    AIR=0x0,
	SOLID=0x1,
	LEFTSTEEPFLOORSLOPE=0x2,
	RIGHTSTEEPFLOORSLOPE=0x3,
	LEFTUPPERSLIGHTFLOORSLOPE=0x4,
	LEFTLOWERSLIGHTFLOORSLOPE=0x5,
	RIGHTLOWERSLIGHTFLOORSLOPE=0x6,
	RIGHTUPPERSLIGHTFLOORSLOPE=0x7,
	ENEMYONLY=0x8,
	STOPENEMYBLOCK=0x9,
	TANK=0xA,
	DOOR=0xB,
	PASSTHROUGHBOTTOM=0xC
)

CollisionCheck = Enum(
    Int8ul,
	AIRORNOCOLLISION=0x0,
	LEFTSLIGHTFLOORSLOPE=0x2,
	RIGHTSLIGHTFLOORSLOPE=0x3,
	LEFTSTEEPFLOORSLOPE=0x4,
	RIGHTSTEEPFLOORSLOPE=0x5,
	PASSTHROUGHBOTTOM=0x10,
	SOLIDORCOLLISION=0x11
)

Cutscene = Enum(
    Int8ul,
	NONE=0x0,
	SAMUSINTROTEXT=0x1,
	SAMUSZEBESESCAPETEXT=0x2,
	SAMUSZEBESESCAPEFINALTEXT=0x3,
	MOTHERBRAINCLOSEUP=0x4,
	KRAIDFIGHTSTART=0x5,
	TOURIANELEVATORSTATUEACTIVATING=0x6,
	RIDLEYINSPACE=0x7,
	RIDLEYLANDING=0x8,
	RIDLEYFIGHTSTART=0x9,
	TOURIANMETROIDS=0xA,
	BEFORERUINSTESTFIGHT=0xB,
	OBTAININGFULLYPOWEREDSUIT=0xC,
	MECHARIDLEYSEESSAMUS=0xD,
	ACTIVATINGESCAPESHIP=0xE
)

CutsceneRequest = Enum(
    Int8ul,
	NONE=0x0,
	ESCAPINGCHOZODIA=0x1,
	ESCAPEDFAILED=0x2,
	ESCAPINGZEBES=0x3,
	OBTAININGFULLYPOWEREDSUIT=0x4,
	RIDLEYFIGHTSTART=0x5,
	TOURIANELEVATORSTATUEACTIVATING=0x6,
	SAMUSINTROTEXT=0x7,
	ACTIVATINGESCAPESHIP=0x8
)

CutsceneSpecialEffectStatus = Enum(
    Int8ul,
	NONE=0x0,
	ONOBJ=0x1,
	OBJEFFECTENDED=0x2,
	ONBG=0x4,
	BGEFFECTENDED=0x8
)

# TODO undocumented
DebrisCloudType = Enum(
    Int8ul,
    TODO=0
)

DemoStatus = Enum(
    Int8ul,
    NONE=0,
    PLAYING=1,
    LOADING=16
)

DiagonalAim = Enum(
    Int8ul,
    NONE=0,
    DIAGONALLYUP=1,
    DIAGONALLYDOWN=2
)

Difficulty = Enum(
    EASY=0,
    NORMAL=1,
    HARD=2
)

Direction = Enum(
    Int8ul,
    RIGHT=0x10,
    LEFT=0x20,
    UP=0x40,
    DOWN=0x80
)

DoorType = Enum(
    Int8ul,
    AREA_CONNECTION=1,
    NO_HATCH=2,
    OPEN_HATCH=3,
    CLOSED_HATCH=4,
    REMOVE_MOTHERSHIP=5,
    SET_MOTHERSHIP=6,
    LOADS_EVENT_BASED_ROOM=32,
    DISPLAYS_LOCATION_NAME=64
)

Elevator = Enum(
    Int8ul,
    NONE=0,
    CRATERIA_TO_BRINSTAR_UNUSED=1,
    BRINSTAR_TO_NORFAIR=2,
    NORFAIR_TO_RIDLEY=4,
    BRINSTAR_TO_TOURIAN=5,
    CRATERIA_TO_TOURIAN=6,
    CRATERIA_TO_NORFAIR=7
)

EndingFlags = Enum(
    Int8ul,
    NONE=0x0,
    NEW_TIME_ATTACK_RECORD=0x1,
    UNUSED=0x10,
    FIRST_TIME_ATTACK_CLEAR=0x20,
    FIRST_HARD_MODE_CLEAR=0X40,
    FIRST_CLEAR=0X80
)

ErrorFlags = Enum(
    Int32ul,
    NONE=0x0,
    UNK_03=0x3,
    UNK_1C=0x1C,
    UNK_20=0x20,
    UNK_40=0x40,
    UNK_E00=0xE00,
    HARDWARE_ERROR=0x10000,
    CHECKSUM_ERROR=0x20000,
    SEND_OVERFLOW=0x40000,
    RECEIVE_OVERFLOW=0x80000,
    SIO_INTERNAL_ERROR=0x100000,
    SIO_STOP_ERROR=0x2000000,
    ID_OVER_ERROR=0x4000000
)

EscapeTimerStatus = Enum(
    Int8ul,
    NONE=0,
    ESCAPE_HAPPENING=1,
    ESCAPE_FAILED=2
)

Event = Enum(
    Int8ul,
	NONE=0x0,
	EASYMODE=0x1,
	HARDMODE=0x2,
	ENTERNORFAIRDEMOPLAYED=0x3,
	EXITKRAIDDEMOPLAYED=0x4,
	ENTERRIDLEYDEMOPLAYED=0x5,
	ENTERMOTHERSHIPDEMOPLAYED=0x6,
	ENTERTOURIANDEMOPLAYED=0x7,
	GRABBEDBYCHOZOINBRINSTAR_SHOWSLONGBEAM=0x8,
	GRABBEDBYCHOZOINBRINSTAR_SHOWSBOMBS=0x9,
	GRABBEDBYCHOZOINBRINSTAR_SHOWSICEBEAM=0xA,
	GRABBEDBYCHOZOINNORFAIR_SHOWSSPEEDBOOSTER=0xB,
	GRABBEDBYCHOZOINBRINSTAR_SHOWSHIJUMP=0xC,
	GRABBEDBYCHOZOINNORFAIR_SHOWSVARIASUIT=0xD,
	GRABBEDBYCHOZOINBRINSTAR_SHOWSWAVE=0xE,
	GRABBEDBYCHOZO_SHOWSSCREWATTACK_UNUSED=0xF,
	POWERGRIPOBTAINED=0x10,
	CHOZOPILLARFULLYEXTENDED=0x11,
	HIJUMPOBTAINED=0x12,
	VARIASUITOBTAINED=0x13,
	CHARGEBEAMOBTAINED=0x14,
	SCREWATTACKOBTAINED=0x15,
	SPACEJUMPOBTAINED=0x16,
	GRAVITYSUITOBTAINED=0x17,
	PLASMABEAMOBTAINED=0x18,
	CHARGEBEAMBOSSENCOUNTEREDATFIRSTLOCATIONORKILLED=0x19,
	CHARGEBEAMBOSSENCOUNTEREDATSECONDLOCATIONORKILLED=0x1A,
	CHARGEBEAMBOSSKILLEDATSECONDLOCATION=0x1B,
	ACIDWORMKILLED=0x1C,
	KRAIDEYEDOORKILLED=0x1D,
	KRAIDKILLED=0x1E,
	KRAIDELEVATORSTATUEDESTROYED=0x1F,
	CATERPILLARKILLED=0x20,
	IMAGOTUNNELDISCOVERED=0x21,
	COCOONKILLED=0x22,
	IMAGOKILLED=0x23,
	RIDLEYEYEDOORKILLED=0x24,
	RIDLEYKILLED=0x25,
	RIDLEYELEVATORSTATUEDESTROYED=0x26,
	MOTHERBRAINKILLED=0x27,
	CROCOMIREKILLED_UNUSED=0x28,
	REPELMACHINEKILLED_UNUSED=0x29,
	VIEWEDSTATUEROOMAFTERLONGBEAM=0x2A,
	DESSGEEGAKILLEDAFTERSTATUEROOM=0x2B,
	ALLTHREEHIVESDESTROYED=0x2C,
	BUGSKILLEDAFTERBOMBS=0x2D,
	ZIPLINESACTIVATED=0x2E,
	PLANTDESTROYED_INLAVA=0x2F,
	PLANTDESTROYED_POSTVARIA=0x30,
	PLANTDESTROYED_VARIA2=0x31,
	PLANTDESTROYED_VARIA3=0x32,
	PLANTDESTROYED_VARIA1=0x33,
	KRAIDBARISTUTESDEAD=0x34,
	KRAIDSTATUEOPENED=0x35,
	RIDLEYSTATUEOPENED=0x36,
	METROIDROOM1CLEARED=0x37,
	METROIDROOM3CLEARED=0x38,
	METROIDROOM5CLEARED=0x39,
	METROIDROOM2CLEARED=0x3A,
	METROIDROOM6CLEARED=0x3B,
	METROIDROOM4CLEARED=0x3C,
	ZEBETITE1DESTROYED=0x3D,
	ZEBETITE2DESTROYED=0x3E,
	ZEBETITE3DESTROYED=0x3F,
	ZEBETITE4DESTROYED=0x40,
	ESCAPEDZEBES=0x41,
	MARKERBETWEENZEBESANDMOTHERSHIPEVENTS=0x42,
	FULLYPOWEREDSUITOBTAINED=0x43,
	SKIPPEDVARIASUIT=0x44,
	UNKNOWN_CHOZOBLOCK=0x45,
	POWERBOMBSTOLEN=0x46,
	SPACEPIRATEWITHPOWERBOMB1=0x47,
	SPACEPIRATEWITHPOWERBOMB2=0x48,
	GLASSTUBEBROKEN=0x49,
	MECHARIDLEYKILLED=0x4A,
	ESCAPEDCHOZODIA=0x4B,
	UNKNOWN_AKI=0x4C,
	UNKNOWN_BOMBGATE=0x4D,
	END_UNUSED=0x4E
)

FileSelectCursorState = Enum(
    Int8ul,
    DEFAULT=0,
    MOVING=1,
    OPENING_OPTIONS=2,
    SELECTING_FILE=5,
    DESELECTING_FILE=6,
    STARTING_GAME=7,
    UNK_08=8
)

FloatingPointClass = Enum(
    Int8ul,
    SIGNALING_NAN=0,
    QUIET_NAN=1,
    ZERO=2,
    NUM=3,
    INFINITY=4
)

ForcedMovement = Enum(
    Int8ul,
    NONE_SPARKING_UPWARDS=0x0,
    BOUNCING_WALLJUMPING_SPARKING_SIDEWAYS=0x1, # bouncing, walljumping or sparking sideways
    SPARKING_DIAGONALLY=0x2,
    HOLDING_JUMP_WHEN_BOUNCING_1=0x20, # first three frames holding jump when bouncing morph
    HOLDING_JUMP_WHEN_BOUNCING_2=0x21,
    HOLDING_JUMP_WHEN_BOUNCING_3=0x22,
)

GameMode = Enum(
    Int8ul,
	SOFTRESET=0x0,
	INTRO=0x1,
	TITLE=0x2,
	FILESELECT=0x3,
	INGAME=0x4,
	MAPITEMSCREEN=0x5,
	GAMEOVER=0x6,
	CHOZODIAESCAPE=0x7,
	CREDITS=0x8,
	TOURIANESCAPE=0x9,
	CUTSCENES=0xA,
	DEMO=0xB,
	GALLERY=0xC,
	METROIDFUSIONGALLERY=0xD,
	SOFTRESETWITHINPUT=0xE,
	ERASESRAMMENU=0xF,
	DEBUGMENU_BETAONLY=0x10
)

GraphicsAnimType = Enum(
    Int8ul,
    NOT_ANIMATED=0,
    NORMAL=1,
    ALTERNATE=4
)

GroundTypeUnderSamus = Enum(
    Int8ul,
    NORMAL=0,
    WET_GROUND=1,
    DUSTY_GROUND=2,
    VERY_DUSTY_GROUND=3,
    BEHAVIOR_52=4,
    BUBBLY_GROUND=5
)

HatchStatus = Enum(
    Int8ul,
    OPENING=0x1,
    OPENED=0x2,
    LOCKED=0x4,
    UNK_08=0x8,
    FLASHING1=0x10,
    FLASHING2=0x20,
    FLASHING3=0x40
)

HatchType = Enum(
    Int8ul,
    NONE=0,
    UNUSED=1,
    NORMAL=2,
    MISSILE=3,
    SUPER_MISSILE=4,
    POWER_BOMB=5,
    LOCKED=6,
    LOCKED_NOTGRAY=7
)

HazardType = Enum(
    Int8ul,
    NONE=0,
    WATER=1,
    STRONG_LAVA=2,
    WEAK_LAVA=3,
    ACID=4,
    HEAT=5,
    COLD_KNOCKBACK=6,
    COLD=7
)

HazeType = Enum(
    Int8ul,
	NONE=0x0,
	GRADIENTRELATED=0x1,
	BG3=0x2,
	BG3_STRONGINEFFECT_WEAKOUTSIDE=0x3,
	BG3_NONEINEFFECT_WEAKOUTSIDE=0x4,
	BG3_BG2_STRONGINEFFECTWEAKOUTSIDEFORBG3=0x5,
	BG1_BG2_BG3=0x6,
	POWERBOMBEXPANDING=0x7,
	POWERBOMBRETRACTING=0x8,
	AFTERPOWERBOMB=0x9,
	COLDSNOWFLAKES_NOEFFECT=0xA
)

InGameCutscene = Enum(
    Int8ul,
    CLOSE_UP=0x4,
    GETTING_VARIA=0x9,
    GETTING_FULLY_POWERED=0xA
)

ItemType = Enum(
    Int8ul,
    MISSILE_TANK=1,
    ENERGY_TANK=2,
    SUPER_MISSILE_TANK=3,
    POWER_BOMB_TANK=4,
    ABILITY=0x80
)

LZ77BackgroundSize = Enum(
    Int8ul,
    SIZE_256_256=0,
    SIZE_512_256=1,
    SIZE_256_512=2
)

Language = Enum(
    Int8ul,
    JAPANESE_KANJI=0,
    JAPANESE_HIRAGANA=1,
    ENGLISH=2
)

LiquidType = Enum(
    Int8ul,
    NONE=0,
    WATER=1,
    STRONG_LAVA=2,
    WEAK_LAVA=3,
    ACID=4
)

MenuSoundId = Enum(
    Int8ul,
	SUBMENUCURSOR=0x0,
	ACCEPTCONFIRMMENU=0x1,
	MENUCUROSR=0x2,
	FILESELECT=0x3,
	STARTGAME=0x4,
	OPENSUBMENU=0x5,
	CLOSESUBMENU=0x6,
	CLOSESUBMENU=0x7,
	FILESELECTCOPYDELETE=0x8,
	FILESELECTCOPYDELETEMOVING=0x9,
	FILECOPYCONFIRM=0xA,
	MENUCURSOR=0xB,
	STARTGAME=0xC
)

MovementPreventingClipdata = Enum(
    Int8ul,
	NONE=0x0,
	ELEVATORDOWNBLOCK=0x1,
	ELEVATORUPBLOCK=0x2,
	PREVENTPOWERGRIP=0x6,
	SOLIDSTOPENEMYBLOCK=0x7,
	SPACEPIRATEZONELINE=0x8,
	SPACEPIRATEWALLJUMPPOINT=0x9
)

NewProjectileType = Enum(
    Int8ul,
	NONE=0x0,
	BEAM=0x1,
	MISSILE=0x2,
	SUPERMISSILE=0x3,
	BOMB=0x4,
	POWERBOMB=0x5,
	CHARGEDBEAM=0x6
)

OamPreAction = Enum(
    Int8ul,
	NONE=0x0,
	CHANGEFRAME=0x1,
	RESETFRAME=0x2,
	LOOPONLASTFRAME=0x3,
	DELETEAFTEREND=0x4,
	INCREMENTIDAFTEREND=0x5,
	UNK_06=0x6,
	UNK_07=0x7,
	SWITCHTOPREVFRAME=0x8,
	DECREMENTIDATBEGINNING=0x9
)

PaletteAnimType = Enum(
    Int8ul,
    NOT_ANIMATED=0,
    NORMAL=1,
    ALTERNATE=2
)

ParticleEffect = Enum(
    Int8ul,
	SPRITESPLASHWATERSMALL=0x0,
	SPRITESPLASHWATERBIG=0x1,
	SPRITESPLASHWATERHUGE=0x2,
	SPRITESPLASHLAVASMALL=0x3,
	SPRITESPLASHLAVABIG=0x4,
	SPRITESPLASHLAVAHUGE=0x5,
	SPRITESPLASHACIDSMALL=0x6,
	SPRITESPLASHACIDBIG=0x7,
	SPRITESPLASHACIDHUGE=0x8,
	SHOOTINGBEAMLEFT=0x9,
	SHOOTINGBEAMDIAGONALLYUPLEFT=0xA,
	SHOOTINGBEAMDIAGONALLYDOWNLEFT=0xB,
	SHOOTINGBEAMUPLEFT=0xC,
	SHOOTINGBEAMDOWNLEFT=0xD,
	SHOOTINGBEAMRIGHT=0xE,
	SHOOTINGBEAMDIAGONALLYUPRIGHT=0xF,
	SHOOTINGBEAMDIAGONALLYDOWNRIGHT=0x10,
	SHOOTINGBEAMUPRIGHT=0x11,
	SHOOTINGBEAMDOWNRIGHT=0x12,
	BOMB=0x13,
	MISSILETRAIL=0x14,
	SUPERMISSILETRAIL=0x15,
	BEAMTRAILINGRIGHT=0x16,
	BEAMTRAILINGLEFT=0x17,
	CHARGEDLONGBEAMTRAIL=0x18,
	CHARGEDICEBEAMTRAIL=0x19,
	CHARGEDWAVEBEAMTRAIL=0x1A,
	CHARGEDPLASMABEAM=0x1B,
	CHARGEDFULLBEAMTRAIL=0x1C,
	CHARGEDPISTOLTRAIL=0x1D,
	SPRITEEXPLOSIONHUGE=0x1E,
	SPRITEEXPLOSIONSMALL=0x1F,
	SPRITEEXPLOSIONMEDIUM=0x20,
	SPRITEEXPLOSIONBIG=0x21,
	SPRITEEXPLOSIONSINGLETHENBIG=0x22,
	SCREWATTACKDESTROYED=0x23,
	SHINESPARKDESTROYED=0x24,
	SUDOSCREWATTACKDESTROYED=0x25,
	SPEEDBOOSTERDESTROYED=0x26,
	MAINBOSSDEATH=0x27,
	FREEZINGSPRITEWITHICE=0x28,
	FREEZINGSPRITEWITHCHARGEDICE=0x29,
	HITTINGSOMETHINGWITHBASEBEAMORCHARGEDBASE=0x2A,
	HITTINGSOMETHINGWITHLONGBEAMORCHARGEDLONG=0x2B,
	HITTINGSOMETHINGWITHICEBEAM=0x2C,
	HITTINGSOMETHINGWITHWAVEBEAM=0x2D,
	HITTINGSOMETHINGWITHPLASMABEAM=0x2E,
	HITTINGSOMETHINGINVINCIBLE=0x2F,
	HITTINGSOMETHINGWITHMISSILE=0x30,
	HITTINGSOMETHINGWITHSUPERMISSILE=0x31,
	HITTINGSOMETHINGWITHFULLBEAMNOPLASMA=0x32,
	HITTINGSOMETHINGWITHFULLBEAM=0x33,
	SMALLDUST1=0x34,
	MEDIUMDUST1=0x35,
	TWOMEDIUMDUST1=0x36,
	SMALLDUST2=0x37,
	MEDIUMDUST2=0x38,
	TWOMEDIUMDUST2=0x39,
	SAMUSREFLECTION=0x3A,
	CHARGINGBEAM=0x3B,
	ESCAPE=0x3C
)

ParticleEffectStatus = Enum(
    Int8ul,
	EXISTS=0x1,
	ONSCREEN=0x2,
	ISEXPLOSION=0x4,
	NOTDRAWN=0x8,
	LIVEOFFSCREEN=0x10,
	LOWBGPRIORITY=0x20,
	ABSOLUTEPOSITION=0x40,
	XFLIP=0x80
)

PauseScreenFlag = Enum(
    Int8ul,
	UNK_01=0x1,
	PAUSESCREENCUTSCENES=0x2,
	UNK_03=0x3,
	CHOZOSTATUEHINT=0x4,
	MAPDOWNLOAD=0x5,
	ITEMACQUISITION=0x6,
	SUITLESSITEMS=0x7,
	FULLYPOWEREDSUITITEMS=0x8
)

PrimarySpriteID = Enum(
    Int8ul,
	UNUSED_00=0x0,
	UNUSED_01=0x1,
	UNUSED_02=0x2,
	UNUSED_03=0x3,
	UNUSED_04=0x4,
	UNUSED_05=0x5,
	UNUSED_06=0x6,
	UNUSED_07=0x7,
	UNUSED_08=0x8,
	UNUSED_09=0x9,
	UNUSED_0A=0xA,
	UNUSED_0B=0xB,
	UNUSED_0C=0xC,
	UNUSED_0D=0xD,
	UNUSED_0E=0xE,
	UNUSED_0F=0xF,
	UNUSED_10=0x10,
	ITEMBANNER=0x11,
	ZOOMER_YELLOW=0x12,
	ZOOMER_RED=0x13,
	ZEELA=0x14,
	ZEELA_RED=0x15,
	RIPPER_BROWN=0x16,
	RIPPER_PURPLE=0x17,
	ZEB=0x18,
	ZEB_BLUE=0x19,
	LARGEENERGY=0x1A,
	SMALLENERGY=0x1B,
	MISSILEDROP=0x1C,
	SUPERMISSILEDROP=0x1D,
	POWERBOMBDROP=0x1E,
	SKREE_GREEN=0x1F,
	SKREE_BLUE=0x20,
	MORPHBALL=0x21,
	CHOZOSTATUE_LONGBEAMHINT=0x22,
	LONGBEAMCHOZOSTATUE=0x23,
	CHOZOSTATUE_ICEBEAMHINT=0x24,
	ICEBEAMCHOZOSTATUE=0x25,
	CHOZOSTATUE_WAVEBEAMHINT=0x26,
	WAVEBEAMCHOZOSTATUE=0x27,
	CHOZOSTATUE_BOMBHINT=0x28,
	BOMBCHOZOSTATUE=0x29,
	CHOZOSTATUE_SPEEDBOOSTERHINT=0x2A,
	SPEEDBOOSTERCHOZOSTATUE=0x2B,
	CHOZOSTATUE_HIJUMPHINT=0x2C,
	HIJUMPCHOZOSTATUE=0x2D,
	CHOZOSTATUE_SCREWATTACKHINT=0x2E,
	SCREWATTACKCHOZOSTATUE=0x2F,
	CHOZOSTATUE_VARIASUITHINT=0x30,
	VARIASUITCHOZOSTATUE=0x31,
	SOVA_PURPLE=0x32,
	SOVA_ORANGE=0x33,
	MULTIVIOLA=0x34,
	MULTIPLELARGEENERGY=0x35,
	GERUTA_RED=0x36,
	GERUTA_GREEN=0x37,
	SQUEEPT=0x38,
	SQUEEPT_UNUSED=0x39,
	MAPSTATION=0x3A,
	DRAGON=0x3B,
	DRAGON_UNUSED=0x3C,
	ZIPLINE=0x3D,
	ZIPLINEBUTTON=0x3E,
	REO_GREENWINGS=0x3F,
	REO_PURPLEWINGS=0x40,
	GUNSHIP=0x41,
	DEOREM=0x42,
	DEOREM_SECONDLOCATION=0x43,
	CHARGEBEAM=0x44,
	SKULTERA=0x45,
	DESSGEEGA=0x46,
	DESSGEEGA_AFTERLONGBEAM=0x47,
	WAVER=0x48,
	WAVER_UNUSED=0x49,
	MELLOW=0x4A,
	HIVE=0x4B,
	POWERGRIP=0x4C,
	IMAGOLARVA_RIGHT=0x4D,
	MORPHBALLLAUNCHER=0x4E,
	IMAGOCOCOON=0x4F,
	ELEVATORPAD=0x50,
	SPACEPIRATE=0x51,
	SPACEPIRATE_WAITING=0x52,
	SPACEPIRATE_WAITING=0x53,
	SPACEPIRATE_WAITING=0x54,
	SPACEPIRATE=0x55,
	GAMET_BLUE_SINGLE=0x56,
	GAMET_RED_SINGLE=0x57,
	GRAVITYSUITCHOZOSTATUE=0x58,
	SPACEJUMPCHOZOSTATUE=0x59,
	SECURITYGATE_DEFAULTOPEN=0x5A,
	ZEBBO_GREEN=0x5B,
	ZEBBO_YELLOW=0x5C,
	WORKERROBOT=0x5D,
	PARASITE_MULTIPLE=0x5E,
	PARASITE=0x5F,
	PISTON=0x60,
	RIDLEY=0x61,
	SECURITYGATE_DEFAULTCLOSED=0x62,
	ZIPLINEGENERATOR=0x63,
	METROID=0x64,
	FROZENMETROID=0x65,
	RINKA_ORANGE=0x66,
	POLYP=0x67,
	VIOLA_BLUE=0x68,
	VIOLA_ORANGE=0x69,
	GERON_NORFAIR=0x6A,
	HOLTZ=0x6B,
	GEKITAIMACHINE=0x6C,
	RUINSTEST=0x6D,
	SAVEPLATFORM=0x6E,
	KRAID=0x6F,
	IMAGOCOCOON_AFTERFIGHT=0x70,
	RIPPER2=0x71,
	MELLA=0x72,
	ATOMIC=0x73,
	AREABANNER=0x74,
	MOTHERBRAIN=0x75,
	FAKEPOWERBOMBEVENTTRIGGER=0x76,
	ACIDWORM=0x77,
	ESCAPESHIP=0x78,
	SIDEHOPPER=0x79,
	GEEGA=0x7A,
	GEEGA_WHITE=0x7B,
	RINKA_MOTHERBRAIN=0x7C,
	ZEBETITE1AND3=0x7D,
	CANNON=0x7E,
	IMAGOLARVA_RIGHTSIDE=0x7F,
	TANGLEVINE_TALL=0x80,
	TANGLEVINE_MEDIUM=0x81,
	TANGLEVINE_CURVED=0x82,
	TANGLEVINE_SHORT=0x83,
	MELLOW_SWARM=0x84,
	MELLOW_SWARM_HEALTHBASED=0x85,
	IMAGO=0x86,
	ZEBETITE2AND4=0x87,
	CANNON=0x88,
	CANNON=0x89,
	CROCOMIRE=0x8A,
	IMAGOLARVA_LEFT=0x8B,
	GERON_BRINSTAR15=0x8C,
	GERON_BRINSTAR1C=0x8D,
	GERON_VARIA1=0x8E,
	GERON_VARIA2=0x8F,
	GERON_VARIA3=0x90,
	GLASSTUBE=0x91,
	SAVEPLATFORM_CHOZODIA=0x92,
	BARISTUTE=0x93,
	PLASMABEAMCHOZOSTATUE=0x94,
	KRAIDELEVATORSTATUE=0x95,
	RIDLEYELEVATORSTATUE=0x96,
	RISINGCHOZOPILLAR=0x97,
	SECURITYLASER_VERTICAL=0x98,
	SECURITYLASER_HORIZONTAL=0x99,
	SECURITYLASER_VERTICAL=0x9A,
	SECURITYLASER_HORIZONTAL=0x9B,
	LOCKUNLOCKMETROIDDOORS_UNUSED=0x9C,
	GAMET_BLUE_LEADER=0x9D,
	GAMET_BLUE_FOLLOWER=0x9E,
	GEEGA_LEADER=0x9F,
	GEEGA_FOLLOWER=0xA0,
	ZEBBO_GREEN_LEADER=0xA1,
	ZEBBO_GREEN_FOLLOWER=0xA2,
	KRAIDSTATUE=0xA3,
	RIDLEYSTATUE=0xA4,
	RINKA_GREEN=0xA5,
	SEARCHLIGHTEYE=0xA6,
	SEARCHLIGHTEYE=0xA7,
	STEAM_LARGE=0xA8,
	STEAM_SMALL=0xA9,
	PLASMABEAMBLOCK=0xAA,
	GRAVITYSUITBLOCK=0xAB,
	SPACEJUMPBLOCK=0xAC,
	GADORA_KRAID=0xAD,
	GADORA_RIDLEY=0xAE,
	SEARCHLIGHT=0xAF,
	SEARCHLIGHT=0xB0,
	SEARCHLIGHT=0xB1,
	SEARCHLIGHT=0xB2,
	SEARCHLIGHTTRIGGER=0xB3,
	EVENTTRIGGER_DISCOVEREDIMAGOPASSAGE=0xB4,
	FAKEPOWERBOMB=0xB5,
	SPACEPIRATECARRYINGPOWERBOMB=0xB6,
	TANGLEVINE_RED_GERUTA=0xB7,
	TANGLEVINE_GERUTA=0xB8,
	TANGLEVINE_LARVA_RIGHT=0xB9,
	TANGLEVINE_LARVA_LEFT=0xBA,
	WATERDROP=0xBB,
	FALLINGCHOZOPILLAR=0xBC,
	MECHARIDLEY=0xBD,
	EXPLOSIONS_ZEBESESCAPE=0xBE,
	STEAM_LARGE_DIAGONALUP=0xBF,
	STEAM_SMALL_DIAGONALUP=0xC0,
	STEAM_LARGE_DIAGONALDOWN=0xC1,
	STEAM_SMALL_DIAGONALDOWN=0xC2,
	BARISTUTE_KRAID_UPPER=0xC3,
	ESCAPEGATE1=0xC4,
	ESCAPEGATE2=0xC5,
	BLACKSPACEPIRATE=0xC6,
	ESCAPESHIPSPACEPIRATE=0xC7,
	BARISTUTE_KRAID_LOWER=0xC8,
	RINKA_MOTHERBRAIN=0xC9,
	RINKA_MOTHERBRAIN=0xCA,
	RINKA_MOTHERBRAIN=0xCB,
	RINKA_MOTHERBRAIN=0xCC,
	RINKA_MOTHERBRAIN=0xCD
)

ProjectileDirection = Enum(
    Int8ul,
    FORWARD=1,
    DIAGONALLY_UP=2,
    DIAGONALLY_DOWN=3,
    UP=4,
    DOWN=5
)

ProjectileStatus = Enum(
    Int8ul,
    EXISTS=0x1,
    ON_SCREEN=0x2,
    NOT_DRAWN=0x4,
    IGNORE_COLLISION=0x8,
    CAN_AFFECT_ENVIRONMENT=0x10,
    YFLIP=0x20,
    XFLIP=0x40,
    DRAW_UNDER_SPRITES=0x80
)

ProjectileType = Enum(
    Int8ul,
	BEAM=0x0,
	LONGBEAM=0x1,
	ICEBEAM=0x2,
	WAVEBEAM=0x3,
	PLASMABEAM=0x4,
	PISTOL=0x5,
	CHARGEBEAM=0x6,
	CHARGEDLONGBEAM=0x7,
	CHARGEDICEBEAM=0x8,
	CHARGEDWAVEBEAM=0x9,
	CHARGEDPLASMABEAM=0xA,
	CHARGEDPISTOL=0xB,
	MISSILE=0xC,
	SUPERMISSILE=0xD,
	BOMB=0xE,
	POWERBOMB=0xF
)

RoomEffect = Enum(
    Int8ul,
	NONE=0x0,
	WATER=0x1,
	STRONGLAVA=0x2,
	WEAKLAVA=0x3,
	STRONGLAVA_HEATDAMAGE_BG3HAZE=0x4,
	ACID=0x5,
	SNOWFLAKES_COLDDAMAGE_KNOCKBACK=0x6,
	SNOWFLAKES_COLDDAMAGE=0x7,
	HEATHAZEBG3=0x8,
	HEATHAZE_BG2_BG3=0x9,
	GRADIENT_BG3=0xA,
	GRADIENT_BG2=0xB,
	HEATHAZE_BG1_BG2_BG3=0xC
)

SamusEnvironmentalEffect = Enum(
    Int8ul,
	NONE=0x0,
	RUNNINGONWETGROUND=0x1,
	RUNNINGONDUSTYGROUND=0x2,
	RUNNINGONVERYDUSTYGROUND=0x3,
	EXITINGWATER=0x4,
	RUNNINGINTOWATER=0x5,
	EXITINGLAVA=0x6,
	RUNNINGINTOLAVA=0x7,
	EXITINGACID=0x8,
	RUNNINGINTOACID=0x9,
	TAKINGDAMAGEINLAVA=0xA,
	TAKINGDAMAGEINACID=0xB,
	LANDINGONWETGROUND=0xC,
	LANDINGONBUBBLYGROUND=0xD,
	LANDINGONDUSTYGROUND=0xE,
	LANDINGONVERYDUSTYGROUND=0xF,
	SKIDDINGONWETGROUND=0x10,
	SKIDDINGONDUSTYGROUND=0x11,
	BREATHINGBUBBLES=0x12
)

SamusPose = Enum(
    Int8ul,
	RUNNING=0x0,
	STANDING=0x1,
	TURNINGAROUND=0x2,
	SHOOTING=0x3,
	CROUCHING=0x4,
	TURNINGAROUNDANDCROUCHING=0x5,
	SHOOTINGANDCROUCHING=0x6,
	SKIDDING=0x7,
	JUMPINGFALLING=0x8,
	TURNINGAROUNDANDJUMPINGFALLING=0x9,
	LANDING=0xA,
	STARTINGSPINJUMP=0xB,
	SPINNING=0xC,
	STARTINGWALLJUMP=0xD,
	SPACEJUMPING=0xE,
	SCREWATTACKING=0xF,
	MORPHING=0x10,
	MORPHBALL=0x11,
	ROLLING=0x12,
	UNMORPHING=0x13,
	JUMPINGFALLINGINMORPHBALL=0x14,
	HANGINGONLEDGE=0x15,
	TURNINGTOAIMWHILEHANGING=0x16,
	HIDINGARMCANONWHILEHANGING=0x17,
	AIMINGWHILEHANGING=0x18,
	SHOOTINGWHILEHANGING=0x19,
	PULLINGSELFUPFROMHANGING=0x1A,
	PULLINGSELFFORWARDFROMHANGING=0x1B,
	PULLINGSELFINTOMORPHBALLTUNNEL=0x1C,
	USINGELEVATOR=0x1D,
	FACINGTHEFOREGROUND=0x1E,
	TURNINGFROMFACINGFOREGROUND=0x1F,
	GRABBEDBYCHOZOSTATUE=0x20,
	DELAYBEFORESHINESPARKING=0x21,
	SHINESPARKING=0x22,
	SHINESPARKCOLLISION=0x23,
	DELAYAFTERSHINESPARKING=0x24,
	DELAYBEFOREBALLSPARKING=0x25,
	BALLSPARKING=0x26,
	BALLSPARKCOLLISION=0x27,
	ONZIPLINE=0x28,
	SHOOTINGONZIPLINE=0x29,
	TURNINGONZIPLINE=0x2A,
	MORPHBALLONZIPLINE=0x2B,
	SAVINGLOADINGGAME=0x2C,
	DOWNLOADINGMAPDATA=0x2D,
	TURNINGAROUNDTODOWNLOADMAPDATA=0x2E,
	GETTINGHURT=0x2F,
	GETTINGKNOCKEDBACK=0x30,
	GETTINGHURTINMORPHBALL=0x31,
	GETTINGKNOCKEDBACKINMORPHBALL=0x32,
	DYING=0x33,
	CROUCHINGTOCRAWLSUITLESS=0x34,
	CRAWLINGSTOPPED=0x35,
	STARTINGTOCRAWL=0x36,
	CRAWLING=0x37,
	UNCROUCHINGFROMCRAWLING=0x38,
	TURNINGAROUNDWHILECRAWLING=0x39,
	SHOOTINGWHILECRAWLING=0x3A,
	UNCROUCHING_SUITLESS=0x3B,
	CROUCHING_SUITLESS=0x3C,
	GRABBINGLEDGE_SUITLESS=0x3D,
	FACINGTHEBG_SUITLESS=0x3E,
	TURINGFROMFACINGTHEBG_SUITLESS=0x3F,
	ACTIVATINGZIPLINES=0x40,
	INESCAPESHIP=0x41,
	TURNINGTOENTERESCAPESHIP=0x42,
	KNOCKBACKPOSEREQUEST=0xF9,
	HURTPOSEREQUEST=0xFA,
	LANDINGPOSEREQUEST=0xFD,
	UPDATEJUMPVELOCITYREQUEST=0xFE,
	NONE=0xFF
)

SamusSlopeType = Enum(
    Int8ul,
    STEEP=0x1,
    SLIGHT=0x2,
    RIGHT=0x10,
    LEFT=0x20
)

SamusStandingStatus = Enum(
    Int8ul,
	STANDINGONGROUND=0x0,
	STANDINGONENEMY=0x1,
	MIDAIR=0x2,
	NOTINCONTROLOFSAMUS=0x3,
	FORCEDPOSE=0x4,
	HANGING=0x5
)

ScrollsFlag = Enum(
    Int8ul,
    NO_SCROLLS=2,
    HAS_SCROLLS=3
)

SecondarySpriteID = Enum(
    Int8ul,
	CHOZOBALL=0x0,
	CHOZOSTATUEBODY=0x1,
	CHOZOSTATUEREFILL=0x2,
	KRAIDMOUTH=0x3,
	CHOZOSTATUEMOVEMENT=0x4,
	CHARGEBEAMGLOW=0x5,
	WINGEDRIPPER=0x6,
	UNUSEDMULTIVIOLASPRITE=0x7,
	DRAGONFIREBALL=0x8,
	DEOREMSEGMENT=0x9,
	DEOREMEYE=0xA,
	DEOREMTHORN=0xB,
	SKREE_GREEN_EXPLOSION=0xC,
	SAVEPLATFORMTOP=0xD,
	SAVEYESNOCURSOR=0xE,
	SKREE_BLUE_EXPLOSION=0xF,
	ZEELAEYES=0x10,
	HIVEROOTS=0x11,
	IMAGOLARVA_OUTSIDE=0x12,
	MORPHBALL_OUTSIDE=0x13,
	IMAGOCOCOONVINE=0x14,
	IMAGOCOCOONSPORE=0x15,
	SPACEPIRATELASER=0x16,
	RIDLEYBODY=0x17,
	RIDLEYTAIL=0x18,
	SEARCHLIGHTEYEBEAM=0x19,
	METROIDSHELL=0x1A,
	POLYPPROJECTILE=0x1B,
	KRAIDSPIKES=0x1C,
	KRAIDNAILS=0x1D,
	ZIPLINEGENERATORPART=0x1E,
	ATOMICELECTRICITY=0x1F,
	MOTHERBRAINEYE=0x20,
	RIDLEYFIREBALLSMALL=0x21,
	UNKNOWNITEMCHOZOSTATUEBODY=0x22,
	UNKNOWNITEMCHOZOSTATUEREFILLRELATED=0x23,
	MORPHBALLLAUNCHER_BACK=0x24,
	ACIDWORMBODY=0x25,
	ACIDWORMSPIT=0x26,
	CANNONBULLET=0x27,
	CROCOMIREBODY=0x28,
	IMAGOBODY=0x29,
	DEFEATEDIMAGOCOCOON_UNUSED=0x2A,
	IMAGOCOCOONROOT=0x2B,
	SEARCHLIGHTEYEBEAM=0x2C,
	GERUTA_TANGLEVINE=0x2D,
	SAVEPLATFORMTOP_CHOZODIA=0x2E,
	IMAGONEEDLE=0x2F,
	ELEVATORSTATUEDEBRIS=0x30,
	IMAGODAMAGEDSTINGER=0x31,
	GUNSHIPPART=0x32,
	IMAGOEGG=0x33,
	MAPSTATIONSCREEN=0x34,
	CHOZOPILLARPLATFORM=0x35,
	GADORAEYE=0x36,
	GADORABEAM=0x37,
	UNKNOWNITEMBLOCKLIGHT=0x38,
	SEARCHLIGHTEYEPROJECTILE=0x39,
	CHOZOPILLARPLATFORMSHADOW=0x3A,
	RUINSTESTSYMBOL=0x3B,
	RUINSTESTSAMUSREFLECTION_START=0x3C,
	RUINSTESTREFLECTIONCOVER=0x3D,
	RUINSTESTGHOSTOUTLINE=0x3E,
	RUINSTESTGHOST=0x3F,
	RUINSTESTSHOOTABLESYMBOL=0x40,
	RUINSTESTSAMUSREFLECTION_END=0x41,
	RUINSTESTLIGHTNING=0x42,
	RIDLEYFIREBALLLARGE=0x43,
	MECHARIDLEYPART=0x44,
	ESCAPESHIPPART=0x45,
	POWERGRIPGLOW=0x46,
	MECHARIDLEYLASER=0x47,
	MECHARIDLEYMISSILE=0x48,
	MECHARIDLEYFIREBALL=0x49,
	MOTHERBRAINBEAM=0x4A,
	MOTHERBRAINBLOCK=0x4B,
	MOTHERBRAINGLASSBREAKING=0x4C
)

SpecialBGEffect = Enum(
    Int8ul,
	NONE=0x0,
	LIGHTNING=0x1,
	SLIGHTYELLOW=0x2,
	HEAVYYELLOW=0x3,
	TOURIANFADE=0x4,
	INTROTEXTFADE=0x5,
	QUICKFLASH=0x6,
	ALLBLACK=0x7,
	ALLWHITE=0x8
)

SpecialBGEffectBehavior = Enum(
    Int8ul,
	WAITFORTIMER_UNUSED=0x0,
	WAITFORTIMER_RNG=0x1,
	WAITFORTIMER=0x2,
	CHECKAPPLYFIRSTCOLOR=0x3,
	CHECKAPPLYSECONDCOLOR=0x4,
	PLAYSOUND=0x5,
	ENDANDCLEAR=0x6,
	END=0x7,
	ENDEXITZEBESEFFECT=0x8,
	ENDBEFOREINTROTEXTEFFECT=0x9
)

SpecialBGFadeType = Enum(
    Int8ul,
	NONE=0x0,
	FLASH=0x1,
	UNK_02=0x2,
	WHITE=0x3,
	DOORTRANSITION=0x4,
	FLASH2=0x5,
	NOTRANSITION=0x6,
	FLASHNOTRANSITION=0x7,
	NOTRANSITIONHUDHIDE=0x8,
	SLOWWHITEFADE=0x9,
	SLOWBLACKFADE=0xA,
	AFTERENTERMOTHERSHIPCUTSCENE=0xB,
	ESCAPEFAILEDFADE=0xC,
	DEMOENDINGAUTOMATICALLYFADE=0xD,
	DEMOENDINGFROMINPUTFADE=0xE,
	CHOZODIAESCAPEFADE=0xF,
	TOURIANESCAPEFADE=0x10,
	GETTINGFULLYPOWEREDFADE=0x11,
	BEFORERIDLEYFIGHTFADE=0x12,
	STATUECUTSCENEFADE=0x13,
	INTROTEXTFADE=0x14,
	LANDINGSHIPCUTSCENEFADE=0x15,
	BLUESHIPFADE=0x16,
	TOWHITE=0x17,
	TOBLACK=0x18
)

# TODO figure this out
SpriteDebrisType = Enum(
    Int8ul,
    TODO=0
)

SpriteProperties = Enum(
    Int8ul,
	ALWAYSACTIVE_IGNOREPREVENTMOVEMENTTIMER=0x1,
	UNK_02=0x2,
	KILLOFFSCREEN=0x4,
	SOLIDFORPROJECTILES=0x8,
	DESTROYED=0x10,
	ABSOLUTEPOSITION=0x20,
	IMMUNETOPROJECTILES=0x40,
	SECONDARYSPRITE=0x80
)

SpriteSamusCollision = Enum(
    Int8ul,
	SOLID=0x1,
	ESCAPESHIP=0x2,
	HURTSSAMUS_CANSTANDON=0x3,
	HURTSSAMUS=0x4,
	ATOMICDISCHARGE=0x5,
	HURTSSAMUS_STOPSWHENHIT=0x6,
	KNOCKSBACKSAMUS=0x7,
	HURTSSAMUS_NOKNOCKBACK=0x9,
	KRAID=0xA,
	HURTSSAMUS_CANNOTPASSTHROUGH=0xB,
	ZEBETITE=0xC,
	IMAGOSTINGER=0xD,
	HURTSSAMUS_BIGKNOCKBACK_STOPSWHENHIT=0xE,
	HURTSSAMUS_NOKNOCKBACK_STOPSWHENHIT=0x10,
	HURTSSAMUS_NOKNOCKBACK_IGNORECONTACTDAMAGE=0x11,
	MELLOW=0x12,
	SPACEPIRATELASER=0x13,
	SPACEPIRATE=0x14,
	ACIDWORM=0x15,
	ACIDWORMMOUTH=0x16,
	BUG=0x17,
	METROID=0x18,
	KRAIDSPIKE=0x19,
	ZIPLINE=0x1A,
	IMAGOEGG=0x1B,
	RIDLEYCLAW_CANBEGRABBED=0x1C,
	MECHARIDLEY=0x1D,
	ABILITY_SECURITYLASER_SEARCHLIGHT=0x1E,
	SMALLENERGYDROP=0x1F,
	LARGEENERGYDROP=0x20,
	MISSILEDROP=0x21,
	SUPERMISSILEDROP=0x22,
	POWERBOMBDROP=0x23,
	MULTIPLELARGEENERGYDROP=0x24
)

SpriteStatus = Enum(
    Int16ul,
	EXISTS=0x1,
	ONSCREEN=0x2,
	NOTDRAWN=0x4,
	ROTATIONSCALINGFLAG=0x8,
	MOSAICFLAG=0x20,
	XFLIP=0x40,
	YFLIP=0x80,
	FACINGDOWN=0x100,
	FACINGRIGHT=0x200,
	ALPHABLENDING=0x2000,
	IGNOREPROJECTILES=0x8000
)

SpriteWeakness = Enum(
    Int8ul,
	CHARGEBEAMPISTOL_NONORMALBEAM=0x1,
	BEAMANDBOMBS=0x2,
	SUPERMISSILES_NONORMALMISSILES=0x4,
	MISSILES=0x8,
	POWERBOMBS=0x10,
	SPEEDBOOSTERSCREWATTACK=0x20,
	CANBEFROZEN=0x40
)

SuitMiscStatus = Enum(
    Int8ul,
	HIJUMP=0x1,
	SPEEDBOOSTER=0x2,
	SPACEJUMP=0x4,
	SCREWATTACK=0x8,
	VARIASUIT=0x10,
	GRAVITYSUIT=0x20,
	MORPHBALL=0x40,
	POWERGRIP=0x80
)

SuitType = Enum(
    Int8ul,
    NORMAL=0,
    FULLY_POWERED=1,
    SUITLESS=2
)

UpdateMinimapFlag = Enum(
    Int8ul,
    NONE=0,
    UPDATE_TOP_LINE=1,
    UPDATE_MIDDLE_LINE=2,
    UPDATE_BOTTOM_LINE=3
)