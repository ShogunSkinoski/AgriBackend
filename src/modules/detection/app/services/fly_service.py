import asyncio
from typing import TypeVar, Generic
import cv2
import numpy as np
import matplotlib.pyplot as plt
from modules.detection.domain.ports.fly_service import FlyDetectionInputBoundry, AsyncFlyDetectionInputBoundry
from modules.detection.domain.ports.fly_model import FlyDetectionPort
from modules.detection.app.response import FlyResponse, ResponseFactory
from modules.detection.utils.detection_const import DetectionConstants

ResponseType = TypeVar("ResponseType", bound=FlyResponse)

class AsyncFlyDetectionAdapter(FlyDetectionPort):
    def __init__(self, _model):
        self._model = _model

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, _model):
        self._model = _model

    async def predict(self, prediction_input):
        return self._model.predict(prediction_input)

class AsyncFlyDetectionService(AsyncFlyDetectionInputBoundry):
    def __init__(self, fly_detection_port: FlyDetectionPort):
        super().__init__(fly_detection_port)

    async def execute(self,
                     image,
                     output_boundry) -> FlyResponse:

        image = self._remove_background(image)
        piece_list = self._corp_image(image)
        response: FlyResponse = ResponseFactory.from_type(output_boundry)(await self._total_flies(piece_list))
        return response

    async def _total_flies(self, piece_list) -> int:
        """
        Calculates the total number of flies in the given list of image pieces.

        Args:
            piece_list: The list of image pieces.

        Returns:
            int: The total number of flies.

        """
        total_flies = 0
        tasks = [self.fly_detection_port.predict(piece) for piece in piece_list]
        task_results = await asyncio.gather(*tasks)
        task_results = [result[0] for result in task_results]
        for result in task_results:
            for box in result.boxes.data.tolist():
                score = box[4]
                if score > DetectionConstants.MIN_SCORE_THRESHOLD:
                    total_flies += 1
        return total_flies

    def _corp_image(self, image) -> list:
        """
        Divides the given image into multiple pieces.

        Args:
            image: The input image.

        Returns:
            list: The list of image pieces.

        """
        piece_width = image.shape[1] // 6
        piece_height = image.shape[0] // 3
        piece_list = []

        for height_piece_index in range(3):
            for width_piece_index in range(6):
                left = width_piece_index * piece_width
                upper = height_piece_index * piece_height
                right = (width_piece_index + 1) * piece_width
                lower = (height_piece_index + 1) * piece_height

                piece = image[upper:lower, left:right]
                piece_list.append(piece)
        return piece_list

    def _remove_background(self, image):
        """
        Removes the background from the given image.

        Args:
            image: The input image.

        Returns:
            The image with the background removed.

        """
        image = image[:, :, ::-1]
        hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        lower_yellow = DetectionConstants.LOWER_YELLOW_HSV_RANGE
        upper_yellow = DetectionConstants.UPPER_YELLOW_HSV_RANGE

        yellow_mask = cv2.inRange(hsv_frame, lower_yellow, upper_yellow)

        yellow_mask = cv2.dilate(yellow_mask, DetectionConstants.BOX_KERNEL)

        image[np.where(yellow_mask == 0)] = DetectionConstants.BLACK_COLOR
        return image
    
class FlyDetectionAdapter(FlyDetectionPort):
    def __init__(self, _model):
        self._model = _model

    def predict(self, prediction_input):
        return self._model.predict(prediction_input)

class FlyDetectionService(FlyDetectionInputBoundry):
    def __init__(self, fly_detection_port: FlyDetectionPort):
        super().__init__(fly_detection_port)

    def execute(self, image):
        image = self._remove_background(image)
        piece_list = self._corp_image(image)
        return self._total_flies(piece_list)

    def _total_flies(self, piece_list) -> int:
        total_flies = 0
        for piece in piece_list:
            prediction_results = self.fly_detection_port.predict(piece)[0]
            for prediction_result in prediction_results.boxes.data.tolist():
                if prediction_result[4] > 0.2:
                   total_flies += 1
        return total_flies
    
    def _corp_image(self, image) -> list:
        piece_width = image.shape[1] // 6
        piece_height = image.shape[0] // 3
        piece_list = []

        for height_piece_index in range(3):
            for width_piece_index in range(6):
                left = width_piece_index * piece_width
                upper = height_piece_index * piece_height
                right = (width_piece_index + 1) * piece_width
                lower = (height_piece_index + 1) * piece_height

                piece = image[upper:lower, left:right]
                piece_list.append(piece)
        return piece_list
    
    def _remove_background(self,image):
        image = image[:,:,::-1]
        hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_yellow = np.array([19, 150, 50], np.uint8)
        upper_yellow = np.array([29, 255, 255], np.uint8)
        yellow_mask = cv2.inRange(hsv_frame, lower_yellow, upper_yellow)

        kernel = np.ones((5, 5), "uint8")
        yellow_mask = cv2.dilate(yellow_mask, kernel)

        image[np.where(yellow_mask == 0)] = [0, 0, 0]
        return image