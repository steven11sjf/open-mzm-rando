from pathlib import Path

from open_mzm_rando.logger import LOG
from open_mzm_rando.patching.ROM import ROM
from open_mzm_rando.patch_pickups import patch_pickup
from open_mzm_rando.patching.assembly_patcher import apply_asm_patches
from open_mzm_rando.patching.tempdir_manager import MZM_TempDir


def test_parse():
    path = Path("e:/Roms/GBA/MZMU.gba")
    modified = Path("e:/Roms/GBA/MZMU_Randomized.gba")

    temp_dir = MZM_TempDir(path, modified)

    apply_asm_patches(temp_dir)

    rom = ROM(temp_dir.get_temp_rom())

    # print(f"Version: \"{rom.version}\"")
    # print("Area headers:")
    # for header in rom.area_header_offsets:
    #     print(f"\t{header}")
    
    patch_pickup(rom, 9, "Power Bomb Tank")
    patch_pickup(rom, 2, "Super Missile Tank")
    patch_pickup(rom, 9, "Super Missile Tank")

    rom.close()
    temp_dir.close()

def patch_extracted(input_path: Path, output_path: Path, configuration: dict):
    LOG.info("Will patch files from %s", input_path)

    # TODO validate schema

    temp_dir = MZM_TempDir(input_path, output_path)

    apply_asm_patches(temp_dir, configuration["asm"])

    rom = ROM(temp_dir.get_temp_rom())

    for p in configuration["pickups"]:
        patch_pickup(rom, p["index"], p["item_name"])

    rom.close()
    temp_dir.close()

    LOG.info("Done")