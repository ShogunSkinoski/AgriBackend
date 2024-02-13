from .color_model import ColorDetectionPort
from abc import ABC, abstractmethod


class ColorDetectionInputBoundry(ABC):
    def __init__(self, fly_detection_port: ColorDetectionPort):
        self.fly_detection_port = fly_detection_port

    @abstractmethod
    def execute(self, image):
        pass

class AsyncColorDetectionInputBoundry(ABC):
 
    def __init__(self, fly_detection_port: ColorDetectionPort):
        self.fly_detection_port = fly_detection_port

    @abstractmethod
    async def execute(self, image):
        pass