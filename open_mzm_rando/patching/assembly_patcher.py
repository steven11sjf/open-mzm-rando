import os
import shutil
from pathlib import Path
from typing import Any

from open_mzm_rando.logger import LOG
from open_mzm_rando.patching.tempdir_manager import MZM_TempDir


def apply_asm_patches(tempdir: MZM_TempDir, config: dict[str, Any]):
    LOG.info("Applying armips to temp rom %s", tempdir.get_temp_rom())
    initial_cwd = os.getcwd()
    asm_dir = Path((Path(os.path.realpath(os.path.dirname(__file__))).parent), "asm")

    config["InitialRom"] = f'\"{tempdir.get_temp_rom().absolute().as_posix()}\"'
    config["FinalRom"] = f'\"{tempdir.temp_dir.joinpath("MZM_PATCHED.gba").absolute().as_posix()}\"'
    asm_main = replace_main_asm(config)
    
    shutil.copyfile(Path(asm_dir, "armips", "armips.exe"), Path(tempdir.temp_dir, "armips.exe"))
    shutil.copytree(Path(asm_dir, "patches"), Path(tempdir.temp_dir, "patches"))
    asm_main_file = tempdir.temp_dir.joinpath("main.asm")
    with open(asm_main_file, "w") as f:
        f.write(asm_main)

    # todo patch
    os.chdir(asm_dir)
    print(os.getcwd())
    os.system(f"{Path(asm_dir, 'armips', 'armips.exe')} {asm_main_file.as_posix()}")
    
    tempdir.update_temp_rom(Path(tempdir.temp_dir, "MZM_PATCHED.gba"))

    os.chdir(initial_cwd)

def replace_main_asm(asm_config: dict[str, Any]):
    """replaces keys in asm/patches/main.asm"""
    main_asm_path = Path(__file__).parent.parent.joinpath("asm", "patches", "main.asm")
    main_asm = main_asm_path.read_text()

    for key,content in asm_config.items():
        print(f"{key}: {content}")
        main_asm = main_asm.replace(f'TEMPLATE("{key}")', str(content))

    return main_asm
