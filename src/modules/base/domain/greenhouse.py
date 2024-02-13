from dataclasses import dataclass
import datetime

@dataclass
class Greenhouse:
    id: int
    uuid: str
    name: str
    created_at: datetime.datetime
    def to_dict(self):
        return {
            "id": self.id,
            "uuid": self.uuid,
            "name": self.name,
            "created_at": self.created_at.strftime("%Y-%m-%d")
        }