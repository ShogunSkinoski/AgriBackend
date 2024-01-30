from datetime import datetime
from dataclasses import dataclass

@dataclass
class Colour:
    id: int
    greenhouse_id: int
    sector_id: int
    flower_light_colour: str
    flower_dark_colour: str
    tomatoes_1: int
    tomatoes_2: int
    tomatoes_3: int
    tomatoes_4: int
    tomatoes_5: int
    tomatoes_6: int
    tomatoes_7: int
    tomatoes_8: int
    leaf_light_colour: str
    leaf_dark_colour: str
    created_at: datetime = datetime.now().date()

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def to_dict(self):
        return {
            "id": self.id,
            "greenhouse_id": self.greenhouse_id,
            "sector_id": self.sector_id,
            "flower_light_colour": self.flower_light_colour,
            "flower_dark_colour": self.flower_dark_colour,
            "tomatoes_1": self.tomatoes_1,
            "tomatoes_2": self.tomatoes_2,
            "tomatoes_3": self.tomatoes_3,
            "tomatoes_4": self.tomatoes_4,
            "tomatoes_5": self.tomatoes_5,
            "tomatoes_6": self.tomatoes_6,
            "tomatoes_7": self.tomatoes_7,
            "tomatoes_8": self.tomatoes_8,
            "leaf_light_colour": self.leaf_light_colour,
            "leaf_dark_colour": self.leaf_dark_colour,
            "created_at": self.created_at
        }
