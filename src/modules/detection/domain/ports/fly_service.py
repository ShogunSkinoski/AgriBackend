from .fly_model import FlyDetectionPort
from abc import ABC, abstractmethod


class FlyDetectionInputBoundry(ABC):
    def __init__(self, fly_detection_port: FlyDetectionPort):
        self.fly_detection_port = fly_detection_port

    @abstractmethod
    def execute(self, image):
        pass

class AsyncFlyDetectionInputBoundry(ABC):
    """
    Service class for asynchronous fly detection.

    Args:
        fly_detection_port (FlyDetectionPort): The port for fly detection.

    Attributes:
        fly_detection_port (FlyDetectionPort): The port for fly detection.

    """
    def __init__(self, fly_detection_port: FlyDetectionPort):
        self.fly_detection_port = fly_detection_port

    @abstractmethod
    async def execute(self, image):
        """
        Executes the fly detection on the given image.

        Args:
            image: The input image for fly detection.
            output_boundry: The output boundary for the fly detection.

        Returns:
            FlyResponse: The response containing the fly detection results.

        """
        pass