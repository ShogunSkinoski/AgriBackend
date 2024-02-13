import asyncio
from typing import TypeVar, Generic
import cv2
import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO

from modules.detection.domain.model.color import Color, TomatousClass, FlowerClass, LeafClass
from modules.detection.domain.ports.color_service import ColorDetectionInputBoundry, AsyncColorDetectionInputBoundry
from modules.detection.domain.ports.color_model import ColorDetectionPort
from modules.detection.app.response import ColorDetectionResponse,ColorDetectionResponseMobile, ResponseFactory
from modules.detection.utils.detection_const import DetectionConstants
from ultralytics.utils.plotting import Annotator
import matplotlib.pyplot as plt

ResponseType = TypeVar("ResponseType", bound=ColorDetectionResponse)


    
model = YOLO(r'src\modules\detection\ai_models\color_best.pt', verbose=False)

service = AsyncColorDetectionService[ColorDetectionResponseMobile](AsyncColorDetectionAdapter(model))

async def main():
    image = cv2.imread(r"C:\Users\die_l\OneDrive\Masaüstü\Tarım\data\images\train\IMG_3188.JPG")
    response = await service.execute(image, ColorDetectionResponseMobile)
    print(response.serialize())


asyncio.run(main())