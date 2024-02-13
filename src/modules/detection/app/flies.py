from fastapi import APIRouter, Body, Depends, File, UploadFile
from fastapi.responses import JSONResponse
from ultralytics import YOLO

from modules.detection.app.services.fly_service import  AsyncFlyDetectionService
from modules.detection.app.services.fly_service import  AsyncFlyDetectionAdapter
from modules.detection.app.response import TotalFlyResponseMobile
from seedwork.infra.uow import SQLAlchemyUnitOfWorkManager
from modules.detection.infra.db.model.flies_model import FliesModel
from modules.detection.infra.db.adapter.repository import FliesRepositoryAdapter
from sqlalchemy import create_engine

import numpy as np
from PIL import Image

model = YOLO(r'src\modules\detection\ai_models\fly_best.pt', verbose=False)

fly_router = APIRouter()

def get_db():
    return create_engine("mysql+mysqlconnector://root:@localhost:3306/ai4agriculture")

def get_fly_detection_service():
    return AsyncFlyDetectionService(AsyncFlyDetectionAdapter(model))

def get_fly_repository():
    return FliesRepositoryAdapter()
def get_uow():
    return SQLAlchemyUnitOfWorkManager(get_db())

@fly_router.post("")
async def detect_fly(image: UploadFile = File(...),
                    sector_id: str = Body(...),
                    greenhouse_id: int = Body(...),
                    service : AsyncFlyDetectionService = Depends(get_fly_detection_service),
                    repository : FliesRepositoryAdapter = Depends(get_fly_repository),
                    uow : SQLAlchemyUnitOfWorkManager = Depends(get_uow)):
    image = Image.open(image.file)
    total_flies_response = await service.execute(np.array(image), TotalFlyResponseMobile)

    flies_model = FliesModel(
                            flies_count=total_flies_response.flies_count,
                            created_at= total_flies_response.date,
                            greenhouse_id=greenhouse_id,
                            sector_id=sector_id
                            )
    repository.add(flies_model, uow)
    return JSONResponse(total_flies_response.serialize(), status_code=200, media_type="application/json")

