from abc import ABC, abstractmethod
from typing import Generic, TypeVar

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
   
    def serialize(self):
        return {
            "device": "mobile",
            "total_fly": self.total_fly,
        }
    
class ResponseFactory(AbstractResponseFactory[FlyResponse]):
    @classmethod
    def from_type(self, response_type: FlyResponse):
        if response_type == TotalFlyResponseMobile:
            return TotalFlyResponseMobile
        else:
            raise Exception("Invalid response type")


        
        
     