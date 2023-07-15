import shutil
import tempfile
from pathlib import Path

from open_mzm_rando.logger import LOG

class MZM_TempDir:
    rom_input: Path
    rom_temp: Path
    rom_output: Path
    temp_dir: Path
    is_closed: bool

    def __init__(self, rom_input: Path, rom_output: Path):
        # setup temp dir
        self.rom_input = rom_input
        self.rom_output = rom_output
        self.temp_dir = Path(tempfile.mkdtemp())
        self.is_closed = False

        # copy rom into temp dir
        self.rom_temp = Path(self.temp_dir, "MZM.gba")
        shutil.copyfile(rom_input, self.rom_temp)

        LOG.info("Created temp dir %s", self.temp_dir)

    def get_temp_rom(self) -> Path:
        if self.is_closed is True:
            raise ValueError(f"Temporary directory {self.temp_dir} has already been closed!")
        
        return self.rom_temp
    
    def update_temp_rom(self, new_rom: Path):
        """Changes the location of the temp rom (i.e. after applying ASM patches)"""
        if self.is_closed is True:
            raise ValueError(f"Temporary directory {self.temp_dir} has already been closed!")
        
        LOG.info("Reassigned temp ROM from %s to %s", self.rom_temp, new_rom)
        self.rom_temp = new_rom

    def close(self):
        """Copies rom_temp to rom_output and removes the temp_dir"""
        if self.is_closed is True:
            raise ValueError(f"Temporary directory {self.temp_dir} has already been closed!")
        
        shutil.copyfile(self.rom_temp, self.rom_output)
        shutil.rmtree(self.temp_dir)
        self.is_closed = True
        LOG.info("Removed temp dir %s", self.temp_dir)