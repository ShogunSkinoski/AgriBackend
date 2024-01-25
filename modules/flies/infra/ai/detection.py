from modules.flies.domain.flies import Flies

class FliesAI:
    
    def detect(self, image):
        return Flies.from_dict({"greenhouse_id": 1, "sector_id": 1, "total_flies": 1, "created_at": "2021-01-01"})