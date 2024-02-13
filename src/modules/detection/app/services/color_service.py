import asyncio
from typing import TypeVar, Generic
import cv2
import numpy as np
import matplotlib.pyplot as plt
from modules.detection.domain.model.color import Color, FlowerClass, LeafClass, TomatousClass
from modules.detection.domain.ports.color_service import ColorDetectionInputBoundry, AsyncColorDetectionInputBoundry
from modules.detection.domain.ports.color_model import ColorDetectionPort
from modules.detection.app.response import ColorDetectionResponse,ColorDetectionResponseMobile, ResponseFactory
from modules.detection.utils.detection_const import DetectionConstants

ResponseType = TypeVar("ResponseType", bound=ColorDetectionResponse)
class AsyncColorDetectionAdapter(ColorDetectionPort):
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

class AsyncColorDetectionService(AsyncColorDetectionInputBoundry, Generic[ResponseType]):
    def __init__(self, color_detection_port: ColorDetectionPort):
        self.color_detection_port = color_detection_port

    async def execute(self, image, output_boundry: ResponseType) -> ResponseType:
        
        image = image[:, :, ::-1]

        results = await self.color_detection_port.predict(image)
        color_list : list[Color] = []
        box_list = []

        for result in results:
            boxes = result.boxes
            for box in boxes:
                box_list.append(box.xyxy[0].tolist())
                c = int(box.cls)
                color = Color(id = 1, greenhouse_id = 1, sector_id = 1)
                if self.__is_tomatou(c):
                    color.tomatous_class = TomatousClass(c)
                elif self.__is_leaf(c):
                    color.leaf_class = self.__get_leaf_class(c)
                else:
                    color.leaf_class = self.__get_flower_class(c)
                color_list.append(color)

        response = ResponseFactory.from_type(output_boundry)
        return response(color_list, box_list)
    
    def __get_flower_class(self, cls):
        if self.color_detection_port.model.names[cls] == DetectionConstants.FLOWER_LIGHT_COLOR:
            return FlowerClass.flower_light_color
        return FlowerClass.flower_dark_color
    
    def __get_leaf_class(self, cls):
        if self.color_detection_port.model.names[cls] == DetectionConstants.LEAF_LIGHT_COLOR:
            return LeafClass.leaf_light_color
        return LeafClass.leaf_dark_color
    
    def __is_tomatou(self, cls):
        return self.color_detection_port.model.names[cls].find(DetectionConstants.TOMATOUS) != -1
    def __is_leaf(self, cls):
        return self.color_detection_port.model.names[cls].find(DetectionConstants.LEAF) != -1