from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from flies.domain.flies import Flies
from flies.infra.ai.detection import FlyDetectionService
fly = APIRouter()

@fly.post("")
async def detect_fly(image: UploadFile = File(...), fly_detection_service: FlyDetectionService = Depends()):
    return fly_detection_service.detect(image)