from datetime import datetime
from dataclasses import dataclass
from enum import Enum

class TomatousClass(Enum):
    tomatous_1 = 1
    tomatous_2 = 2
    tomatous_3 = 3
    tomatous_4 = 4
    tomatous_5 = 5
    tomatous_6 = 6
    tomatous_7 = 7
    tomatous_8 = 8

class FlowerClass(Enum):
    flower_light_color = "light"
    flower_dark_color = "dark"

class LeafClass(Enum):
    leaf_light_color = "light"
    leaf_dark_color = "dark"

@dataclass
class Color:
    id: int
    greenhouse_id: int
    sector_id: int
    tomatous_class: TomatousClass
    flower_class: FlowerClass
    leaf_class: LeafClass
    created_at: datetime = datetime.now().date()

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return {
            "id": self.id,
            "greenhouse_id": self.greenhouse_id,
            "sector_id": self.sector_id,
            "tomatous_class": self.tomatous_class,
            "flower_class": self.flower_class,
            "leaf_class": self.leaf_class,
            "created_at": self.created_at
        }

