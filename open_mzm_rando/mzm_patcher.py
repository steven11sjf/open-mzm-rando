from pathlib import Path

from open_mzm_rando.patching.ROM import ROM

def test_parse():
    path = Path("e:/Roms/GBA/MZMU.gba")
    rom = ROM(path)

    print(f"Version: \"{rom.version}\"")
    print("Area headers:")
    for header in rom.area_header_offsets:
        print(f"\t{header}")