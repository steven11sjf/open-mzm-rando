import os
import re
import shutil
from pathlib import Path
from typing import Any

from open_mzm_rando.logger import LOG
from open_mzm_rando.patching.tempdir_manager import MZM_TempDir


def get_base_replacements() -> dict[str, Any]:
    return {

    }

def apply_asm_patches(tempdir: MZM_TempDir, replacements: dict[str, str]):
    LOG.info("Applying armips to temp rom %s", tempdir.get_temp_rom())
    initial_cwd = os.getcwd()
    asm_dir = Path((Path(os.path.realpath(os.path.dirname(__file__))).parent), "asm")

    # generate main.asm in tempdir
    asm_main = replace_main_asm(replacements)
    asm_main_file = tempdir.temp_dir.joinpath("main.asm")
    with open(asm_main_file, "w") as f:
        f.write(asm_main)

    # chdir to open_mzm_rando/asm and run armips
    os.chdir(asm_dir)
    print(os.getcwd())
    os.system(f"{Path(asm_dir, 'armips', 'armips.exe')} {asm_main_file.as_posix()}")
    
    # update temp rom to point to MZM_PATCHED.gba and chdir back
    tempdir.update_temp_rom(Path(tempdir.temp_dir, "MZM_PATCHED.gba"))
    os.chdir(initial_cwd)

def replace_main_asm(asm_config: dict[str, str]):
    """replaces keys in asm/patches/main.asm"""
    main_asm_path = Path(__file__).parent.parent.joinpath("asm", "patches", "main.asm")
    main_asm = main_asm_path.read_text()

    for key,content in asm_config.items():
        print(f"{key}: {content}")
        main_asm = main_asm.replace(f'TEMPLATE("{key}")', content)
    
    unknown_templates = re.findall(r'TEMPLATE\("([^"]+)"\)', main_asm)
    if unknown_templates:
        raise ValueError(f"The following templates were left unfilled: {str(unknown_templates)}")

    return main_asm
