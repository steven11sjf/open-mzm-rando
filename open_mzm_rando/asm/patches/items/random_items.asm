; RAM addresses
.definelabel Difficulty,0x300002C
.definelabel GettingTankFlag,0x3000044
.definelabel MessageInfo,0x3000C0C
.definelabel SamusData,0x30013D4
.definelabel Equipment,0x3001530

; ROM addresses
.definelabel PlaySound,0x8002A18
.definelabel _16BitFill,0x80032B4
.definelabel SpawnNewPrimarySprite,0x800E31C
.definelabel LoadBeamGfx,0x804F670
.definelabel SetBG1BlockValue,0x805A55C
.definelabel SetClipdataBlockValue,0x805A64C
.definelabel SetItemAsCollected,0x805B0A0
.definelabel EventFunctions,0x80608BC
.definelabel GetItemUpdateMinimap,0x806CBD8

.definelabel NumTanksPerArea,0x83459A0
.definelabel TankStartingAmounts,0x83459C0
.definelabel TankIncreaseAmounts,0x83459C4

; Item events
.definelabel LongEvent,     0x4F  ; new
.definelabel ChargeEvent,   0x14
.definelabel IceEvent,      0x50  ; new
.definelabel WaveEvent,     0x51  ; new
.definelabel PlasmaEvent,   0x18
.definelabel BombEvent,     0x52  ; new
.definelabel VariaEvent,    0x13
.definelabel GravityEvent,  0x17
.definelabel MorphEvent,    0x53  ; new
.definelabel SpeedEvent,    0x54  ; new
.definelabel HiEvent,       0x12
.definelabel ScrewEvent,    0x15
.definelabel SpaceEvent,    0x16
.definelabel GripEvent,     0x10


;------------------
; New Data (Tanks)
;------------------
.org 0x8760D38
; new (animated) tileset entries
.include "patches\items\tilesets_new.asm"

; new tables for clipdata behavior/collision
.include "patches\items\clipdata_new.asm"

; fix pointers for tilesets and clipdata
.include "patches\items\pointer_fixes.asm"

; add tile table lengths
.include "patches\items\tile_table_lengths.asm"
;----------
; New Code
;----------
.org 0x8304054      ; Crocomire graphics

; check item clipdata, spawn/assign items
.include "patches\items\items_new.asm"

; r0 = 1
; r1 = 43
SetEscapedZebesEvent:
    push    r14
    bl      EventFunctions
    mov     r0,1
    mov     r1,0x41
    bl      EventFunctions
    pop     r0
    bx      r0


; unknown items
.include "patches\bin\unk_items\unk_items_new.asm"

;---------------
; Modifications
;---------------

; modified portion of CheckTouchingTransitionOrTank
.include "patches\items\touching_tank.asm"

; unknown items
.include "patches\bin\unk_items\unk_items.asm"

; obtaining and checking abilities
.include "patches\items\abilities.asm"

; miscellaneous tweaks/fixes
.include "patches\items\misc.asm"

; room fixes
.include "patches\items\room_fixes.asm"