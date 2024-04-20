from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from datetime import datetime

from modules.detection.domain.model.color import FlowerClass, LeafClass

T = TypeVar("T")

class AbstractResponseFactory(ABC,Generic[T]):
    @classmethod
    def from_type(self, response_type: T):
        pass

class Response(ABC):
    ...

class ColorDetectionResponse(Response):
    @abstractmethod
    def serialize(self):
        pass
    
class FlyResponse(Response):
    @abstractmethod
    def serialize(self):
        pass

class TotalFlyResponseMobile(FlyResponse):
    def __init__(self, flies_count):
        self.flies_count = flies_count
        self.device = "mobile"
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def serialize(self):
        return {
            "device": self.device,
            "date": self.date,
            "flies_count": self.flies_count
        }
    
class ColorDetectionResponseMobile(ColorDetectionResponse):
    def __init__(self, detection_list, coordinates):
        self.coordinates = coordinates
        self.detection_list = detection_list
    

    def serialize(self):

        if len(self.detection_list) == 0:
            return {
                "device": "mobile",
                "detections": [],
                "coordinates": "[]",
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        id = self.detection_list[0].to_dict()["id"]
        greenhouse_id = self.detection_list[0].to_dict()["greenhouse_id"]
        sector_id = self.detection_list[0].to_dict()["sector_id"]
        return {
            "device": "mobile",
            "id": id,
            "greenhouse_id": greenhouse_id,
            "sector_id": sector_id,
            "detections": [self.detection_to_json(detection.to_dict()) for detection in self.detection_list],
            "coordinates": self.coordinates,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def __get_tomatou_class(self, cls):
        if cls == None:
            return None
        return cls.name

    def __get_leaf_class(self, cls):
        if cls == None:
            return None
        if cls == LeafClass.leaf_light_color.value:
            return LeafClass.leaf_light_color.name
        return LeafClass.leaf_dark_color.name
    
    def __get_flower_class(self, cls):
        if cls == None:
            return None
        if cls == FlowerClass.flower_light_color.value:
            return FlowerClass.flower_light_color.name
        return FlowerClass.flower_dark.name
    
    def detection_to_json(self, detection):
        return {
            "tomatous_class": self.__get_tomatou_class(detection["tomatous_class"]),
            "flower_class": self.__get_flower_class(detection["flower_class"]),
            "leaf_class": self.__get_leaf_class(detection["leaf_class"]),
        }
class ResponseFactory(AbstractResponseFactory[Response]):
    @classmethod
    def from_type(self, response_type: Response):
        if response_type == TotalFlyResponseMobile:
            return TotalFlyResponseMobile
        elif response_type == ColorDetectionResponseMobile:
            return ColorDetectionResponseMobile
        else:
            raise Exception("Invalid response type")