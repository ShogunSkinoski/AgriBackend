from dataclasses import dataclass
import datetime

@dataclass
class Greenhouse:
    id: int
    name: str
    created_at: datetime.datetime