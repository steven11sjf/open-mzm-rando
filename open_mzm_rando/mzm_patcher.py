from pathlib import Path

from open_mzm_rando.construct_patching.ROM import ROM

def test_parse():
    path = Path("'e:/Roms/GBA/Metroid - Zero Mission (U) [!].gba'")
    data = path.read_bytes()
    parsed = ROM().parse(data)
    print(parsed)