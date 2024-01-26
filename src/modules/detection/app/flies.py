from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from modules.detection.infra.ai.detection import FliesAI
fly = APIRouter()

@fly.post("")
async def detect_fly(image: UploadFile = File(...), fly_detection_service: FliesAI = Depends()):
    return fly_detection_service.detect(image)