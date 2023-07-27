from enum import Enum

class Region(Enum):
    BRINSTAR=0
    KRAID=1
    NORFAIR=2
    RIDLEY=3
    TOURIAN=4
    CRATERIA=5
    CHOZODIA=6

    @staticmethod
    def get(region_name: str):
        for reg in Region:
            if reg.name == region_name.upper():
                return reg.value