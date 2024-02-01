import asyncio
import datetime

from fastapi import FastAPI
from modules.detection.infra.db.model.flies_model import FliesModel
from sqlalchemy.orm import Session

from sqlalchemy import create_engine
import torch
from ultralytics import YOLO
from PIL import Image
from modules.detection.app.services.fly_service import AsyncFlyDetectionService, AsyncFlyDetectionAdapter,FlyDetectionAdapter, FlyDetectionService
import numpy as np
import time
app = FastAPI()

app.include_router(fly, prefix="/fly", tags=["fly"])

# # #TODO: change the connection string to a .env variable
# # #TODO: change alembic version of detection module and move the greenhouses table and the sectors table to the base module
# # #TODO: integrate the ai to domain and create use cases for the detection module

# # engine = create_engine('mysql+mysqlconnector://root:perhap5gell@localhost:3306/ai4agriculture', echo=True, future=True)

# # with Session(engine) as session:
# #     flies_model = FliesModel(flies_count=1, created_at= datetime.datetime.now().strftime("%Y-%m-%d"), greenhouse_id=2, sector_id=1)
# #     session.add(flies_model)
# #     session.commit()

# async def main():
#     model = YOLO(r'src\utils\fly\model\runs\detect\train\weights\best.pt', verbose=False)

#     fly_detection_adapter = AsyncFlyDetectionAdapter(model)
#     fly_detection_service = AsyncFlyDetectionService(fly_detection_adapter)
#     sync_fly_detection_adapter = FlyDetectionAdapter(model)
#     sync_fly_detection_service = FlyDetectionService(sync_fly_detection_adapter)
#     print("empty")
#     image = Image.open(r'src\utils\fly\model\WhatsApp Image 2024-01-30 at 21.07.08.jpeg')
#     await fly_detection_service.execute(np.array(image))
    
#     avarage_async = 0
#     for i in range(100):
#         now = time.time()
#         await fly_detection_service.execute(np.array(image))
#         end = time.time()
#         avarage_async += end - now

#     avarage_sync = 0
#     for i in range(100):
#         now = time.time()
#         sync_fly_detection_service.execute(np.array(image))
#         end = time.time()
#         avarage_sync += end - now

#     print("async:", avarage_async/100)
#     print("sync:", avarage_sync/100)
    

# if __name__ == "__main__":
#     asyncio.run(main())