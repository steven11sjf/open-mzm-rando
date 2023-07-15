import os
import shutil
import tempfile
from pathlib import Path

from open_mzm_rando.patching.tempdir_manager import MZM_TempDir


def apply_asm_patches(tempdir: MZM_TempDir):
    print(f"Applying armips to {tempdir.get_temp_rom()}")
    initial_cwd = os.getcwd()
    asm_dir = Path((Path(os.path.realpath(os.path.dirname(__file__))).parent), "asm")
    
    shutil.copyfile(Path(asm_dir, "armips", "armips.exe"), Path(tempdir.temp_dir, "armips.exe"))
    shutil.copytree(Path(asm_dir, "patches"), Path(tempdir.temp_dir, "patches"))
    os.chdir(tempdir.temp_dir)

    # todo patch
    os.system(f"armips.exe patches/main.asm")
    
    tempdir.update_temp_rom(Path(tempdir.temp_dir, "MZM_PATCHED.gba"))

    os.chdir(initial_cwd)