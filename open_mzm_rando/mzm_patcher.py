from pathlib import Path

from open_mzm_rando.logger import LOG
from open_mzm_rando.patching.ROM import ROM
from open_mzm_rando.patch_pickups import patch_pickup
from open_mzm_rando.patching.assembly_patcher import apply_asm_patches
from open_mzm_rando.patching.tempdir_manager import MZM_TempDir
from open_mzm_rando.random_start import random_start_to_music


def create_asm_replacements(temp_dir: MZM_TempDir, config: dict) -> dict[str, str]:
    # default values
    replacements = {
        "InitialRom": f'"{temp_dir.rom_temp.absolute().as_posix()}"',
        "FinalRom": f'"{temp_dir.temp_dir.joinpath("MZM_PATCHED.gba").absolute().as_posix()}"',
        "RandomStartEnabled": "0",
        "StartingArea": "0x0",
        "StartingDoor": "0x0",
        "StartingMusic": "0x0"
    }

    if "starting_location" in config:
        replacements.update(random_start_to_music(config["starting_location"]))

    return replacements

def patch_extracted(input_path: Path, output_path: Path, configuration: dict):
    LOG.info("Will patch files from %s", input_path)

    # TODO validate schema

    temp_dir = MZM_TempDir(input_path, output_path)

    armips_replacements = create_asm_replacements(temp_dir, configuration)

    apply_asm_patches(temp_dir, armips_replacements)

    rom = ROM(temp_dir.get_temp_rom())

    for p in configuration["pickups"]:
        patch_pickup(rom, p["index"], p["item_name"])

    rom.close()
    temp_dir.close()

    LOG.info("Done")