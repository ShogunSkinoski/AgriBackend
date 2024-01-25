from dataclasses import dataclass
from datetime import datetime

@dataclass
class Flies:
    greenhouse_id: int
    sector_id: int
    total_flies: int
    created_at: datetime = datetime.now().date()
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    
    def to_dict(self):
        return {
            "greenhouse_id": self.greenhouse_id,
            "sector_id": self.sector_id,
            "total_flies": self.total_flies,
            "created_at": self.created_at
        }