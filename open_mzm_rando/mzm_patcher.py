from pathlib import Path

from open_mzm_rando.construct_patching.ROM import ROM

def test_parse():
    path = Path("e:/Roms/GBA/MZMU.gba")
    data = path.read_bytes()
    parsed = ROM().parse(data)
    print(parsed)

    new_path = Path("e:/Roms/GBA/MZMU_REBUILT.gba")
    new_bytes = ROM().build(parsed)
    new_path.write_bytes(new_bytes)