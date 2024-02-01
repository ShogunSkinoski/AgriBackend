from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from datetime import datetime

T = TypeVar("T")

class AbstractResponseFactory(ABC,Generic[T]):
    @classmethod
    def from_type(self, response_type: T):
        pass
class FlyResponse(ABC):
    @abstractmethod
    def serialize(self):
        pass

class TotalFlyResponseMobile(FlyResponse):
    def __init__(self, total_fly):
        self.total_fly = total_fly
        self.device = "mobile"
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.total_fly = self.total_fly

    def serialize(self):
        return {
            "device": self.device,
            "date": self.date,
            "total_fly": self.total_fly
        }
    
class ResponseFactory(AbstractResponseFactory[FlyResponse]):
    @classmethod
    def from_type(self, response_type: FlyResponse):
        if response_type == TotalFlyResponseMobile:
            return TotalFlyResponseMobile
        else:
            raise Exception("Invalid response type")


        
        
     