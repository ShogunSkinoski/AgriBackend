from dataclasses import dataclass
import datetime

@dataclass
class Sector:
    id: int
    uuid: str
    name: str
    greenhouse_id: int
    created_at: datetime.datetime

    def to_dict(self):
        return {
            "id": self.id,
            "uuid": self.uuid,
            "name": self.name,
            "greenhouse_id": self.greenhouse_id,
            "created_at": self.created_at.strftime("%Y-%m-%d")
        }