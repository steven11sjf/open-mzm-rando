from pathlib import Path

import os
import pytest

def get_env_or_skip(env_name):
    if env_name not in os.environ:
        pytest.skip(f"Skipped due to missing environment variable {env_name}")
    return os.environ[env_name]

@pytest.fixture
def mzmu_rom_path():
    return Path(get_env_or_skip("MZM_ROM_PATH"))