from dataclasses import dataclass
from datetime import datetime

@dataclass
class Flies:
    id: int
    greenhouse_id: int
    sector_id: str
    flies_count: int
    created_at: datetime = datetime.now().date()
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    
    def to_dict(self):
        return {
            "id": self.id,
            "greenhouse_id": self.greenhouse_id,
            "sector_id": self.sector_id,
            "flies_count": self.flies_count,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }