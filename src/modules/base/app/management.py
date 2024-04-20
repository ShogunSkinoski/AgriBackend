import datetime
from fastapi import APIRouter,  Body, Request, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
import uuid
from modules.base.domain.sector import Sector

from modules.base.infra.db.adapter.greenhouse_repository import GreenhouseRepositoryAdapter
from modules.base.infra.db.adapter.sector_repository import SectorRepositoryAdapter
from modules.detection.infra.db.adapter.repository import FliesRepositoryAdapter
from modules.base.infra.db.model.greenhouse_model import GreenhouseModel, GreenHouseMapper
from modules.base.infra.db.model.sector_model import SectorModel, SectorMapper
from modules.base.domain.greenhouse import Greenhouse
from modules.detection.infra.db.model.flies_model import FliesModel, FliesModelMapper

from seedwork.infra.uow import SQLAlchemyUnitOfWorkManager


management_router = APIRouter()

def get_db():
    return create_engine("mysql+mysqlconnector://root:@localhost:3306/ai4agriculture")

def get_greenhose_repository():
    return GreenhouseRepositoryAdapter()

def get_sector_repository():
    return SectorRepositoryAdapter()

def get_fly_repository():
    return FliesRepositoryAdapter()

def get_uow():
    return SQLAlchemyUnitOfWorkManager(get_db())

@management_router.get("/greenhouse")
async def get_greenhouse(
    repository : GreenhouseRepositoryAdapter = Depends(get_greenhose_repository),
    uow : SQLAlchemyUnitOfWorkManager = Depends(get_uow) 
):
    greenhouses_db: list[GreenhouseModel] = repository.get_all(uow)
    greenhouses: list[dict[str,object]] = []

    for greenhouse in greenhouses_db:
        greenhouses.append(GreenHouseMapper.to_domain(greenhouse).to_dict())
    
    return JSONResponse(greenhouses, status_code=200, media_type="application/json")

@management_router.get("/greenhouse/{greenhouse_id}")
async def get_greenhouse_by_id(
                        greenhouse_id: int,
                        repository : GreenhouseRepositoryAdapter = Depends(get_greenhose_repository),
                        uow : SQLAlchemyUnitOfWorkManager = Depends(get_uow) 
):
    greenhouse_db: GreenhouseModel = repository.get(greenhouse_id, uow)
    greenhouse: Greenhouse = GreenHouseMapper.to_domain(greenhouse_db)
    return JSONResponse(greenhouse.to_dict(), status_code=200, media_type="application/json")
    

@management_router.post("/greenhouse")
async def create_greenhouse(
    body: dict[str, str] = Body(...),
    repository : GreenhouseRepositoryAdapter = Depends(get_greenhose_repository),
    uow : SQLAlchemyUnitOfWorkManager = Depends(get_uow) 
):
    print(body)
    greenhouse = GreenhouseModel(
        uuid = str(uuid.uuid4()),
        name= body["name"],
        created_at=datetime.datetime.now().strftime("%Y-%m-%d")
        )
    repository.add(greenhouse, uow)
    return JSONResponse({"message": "Greenhouse created"}, status_code=201, media_type="application/json")

    

@management_router.put("/greenhouse/{greenhouse_id}")
async def update_greenhouse(greenhouse_id: int):
    return {"message": "Hello World"}

@management_router.get("/sector")
async def get_sector(
    request: Request,
    repository : SectorRepositoryAdapter = Depends(get_sector_repository),
    uow : SQLAlchemyUnitOfWorkManager = Depends(get_uow) 
):
    if request.query_params.get("greenhouse_id"):
        greenhouse_id = request.query_params.get("greenhouse_id")
        sectors_db: list[SectorModel] = repository.get_all_by_greenhouse(greenhouse_id, uow)
        sectors: list[dict[str,object]] = []

        for sector in sectors_db:
            sectors.append(SectorMapper.to_domain(sector).to_dict())
        return JSONResponse(sectors, status_code=200, media_type="application/json")
    
    sectors_db: list[SectorModel] = repository.get_all(uow)
    sectors: list[dict[str,object]] = []

    for sector in sectors_db:
        sectors.append(SectorMapper.to_domain(sector).to_dict())
    
    return JSONResponse(sectors, status_code=200, media_type="application/json")


@management_router.get("/sector/{sector_id}")
async def get_sector_by_id(
    sector_id,
    repository : SectorRepositoryAdapter = Depends(get_sector_repository),
    uow : SQLAlchemyUnitOfWorkManager = Depends(get_uow)
):
    sector_db: SectorModel = repository.get(sector_id, uow)
    sector: Sector = SectorMapper.to_domain(sector_db)
    return JSONResponse(sector.to_dict(), status_code=200, media_type="application/json")

@management_router.get("/sector/{sector_id}/detections")
async def get_sector_detections(
    sector_id,
    repository : FliesRepositoryAdapter = Depends(get_fly_repository),
    uow : SQLAlchemyUnitOfWorkManager = Depends(get_uow)
):
    flies_db: list[FliesModel] = repository.get_all_by_sector(sector_id, uow)
    flies: list[dict[str,object]] = []

    for fly in flies_db:
        flies.append(FliesModelMapper.to_domain(fly).to_dict())

    response = {
        "message": "Sector detections",
        "sector_id": sector_id,
        "detections": flies
    }
    return JSONResponse(response, status_code=200, media_type="application/json")

@management_router.post("/sector")
async def create_sector(
    body: dict[str, str] = Body(...),
    repository : SectorRepositoryAdapter = Depends(get_sector_repository),
    uow : SQLAlchemyUnitOfWorkManager = Depends(get_uow) 
):
    
    sector = SectorModel(
        uuid = str(uuid.uuid4()),
        name= body["name"],
        greenhouse_id = body["greenhouse_id"],
        created_at=datetime.datetime.now().strftime("%Y-%m-%d")
        )
    repository.add(sector, uow)
    response = {
        "message": "Sector created successfully",
        "sector_id": sector.id,
        "greenhouse_id": sector.greenhouse_id
    }
    return JSONResponse(response, status_code=201, media_type="application/json")
    

@management_router.put("/sector/{sector_id}")
async def update_sector(sector_id: int):
    return {"message": "Hello World"}