from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from ultralytics import YOLO
from modules.detection.app.services.fly_service import  AsyncFlyDetectionService
from modules.detection.app.services.fly_service import  AsyncFlyDetectionAdapter
from modules.detection.app.response import TotalFlyResponseMobile
import numpy as np
from PIL import Image
model = YOLO(r'src\utils\fly\model\runs\detect\train\weights\best.pt', verbose=False)

fly = APIRouter()

def get_fly_detection_service():
    return AsyncFlyDetectionService(AsyncFlyDetectionAdapter(model))

@fly.post("")
async def detect_fly(image: UploadFile = File(...), service : AsyncFlyDetectionService = Depends(get_fly_detection_service)):
    image = Image.open(image.file)
    total_flies_response = await service.execute(np.array(image), TotalFlyResponseMobile)
    return total_flies_response.serialize()