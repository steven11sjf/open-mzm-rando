import pytest

from pathlib import Path
from open_mzm_rando.patching.LZ77 import compress_LZ77, decompress_LZ77

LZ77_COMPRESSED = [
    "open_mzm_rando/files/item_gfx/Bomb.bin",
    "open_mzm_rando/files/item_gfx/Charge.bin",
    "open_mzm_rando/files/item_gfx/ChozoStatue.bin",
    "open_mzm_rando/files/item_gfx/EnergyTank.bin",
    "open_mzm_rando/files/item_gfx/Gravity.bin",
    "open_mzm_rando/files/item_gfx/Grip.bin",
    "open_mzm_rando/files/item_gfx/HiJump.bin",
    "open_mzm_rando/files/item_gfx/Ice.bin",
    "open_mzm_rando/files/item_gfx/Long.bin",
    "open_mzm_rando/files/item_gfx/Missile.bin",
    "open_mzm_rando/files/item_gfx/Morph.bin",
    "open_mzm_rando/files/item_gfx/None.bin",
    "open_mzm_rando/files/item_gfx/Plasma.bin",
    "open_mzm_rando/files/item_gfx/PowerBomb.bin",
    "open_mzm_rando/files/item_gfx/Screw.bin",
    "open_mzm_rando/files/item_gfx/Space.bin",
    "open_mzm_rando/files/item_gfx/Speed.bin",
    "open_mzm_rando/files/item_gfx/SuperMissile.bin",
    "open_mzm_rando/files/item_gfx/Varia.bin",
    "open_mzm_rando/files/item_gfx/Wave.bin",
]

@pytest.mark.parametrize("lz77_compressed_file", LZ77_COMPRESSED)
def test_files(lz77_compressed_file: str):
    file = Path(__file__).parent.parent.joinpath(lz77_compressed_file)

    orig = file.read_bytes()
    comp = compress_LZ77(orig)
    decomp = decompress_LZ77(comp, 0)
    assert orig == decomp
