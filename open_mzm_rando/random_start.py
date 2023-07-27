import dataclasses
import json
from pathlib import Path

from open_mzm_rando.constants import Region

def _get_files() -> Path:
    return Path(__file__).parent.joinpath("files")

def random_start_to_music(config: dict[str, str]):
    json_data = _get_files().joinpath("door_to_music.json").read_text()
    music = json.loads(json_data)

    region = config["region"]
    door = config["door"]
    if type(door) == int:
        door = hex(door)
    region_hex = hex(Region.get(region))
    
    return {
        "RandomStartEnabled": "1",
        "StartingArea": region_hex,
        "StartingDoor": door,
        "StartingMusic": music[region][door]
    }