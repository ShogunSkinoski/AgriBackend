from fastapi import APIRouter, Body, Depends, File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO

from modules.detection.app.services.color_service import  AsyncColorDetectionService, AsyncColorDetectionAdapter
from modules.detection.app.response import ColorDetectionResponseMobile

import numpy as np
from PIL import Image

color_router = APIRouter()

model = YOLO(r'src\modules\detection\ai_models\color_best.pt', verbose=False)
def get_color_detection_service():
    return AsyncColorDetectionService(AsyncColorDetectionAdapter(model))

@color_router.post("")
async def detect_color(image: UploadFile = File(...),
                    service : AsyncColorDetectionService = Depends(get_color_detection_service)):
    image = Image.open(image.file)
    color_detection_response = await service.execute(np.array(image), ColorDetectionResponseMobile)

    return JSONResponse(color_detection_response.serialize(), status_code=200, media_type="application/json")