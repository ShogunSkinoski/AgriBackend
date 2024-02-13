import datetime
from seedwork.utils.base_model import BaseModel
from seedwork.infra.model_mapper import ModelMapper

from modules.base.infra.db.model.sector_model import SectorModel
from modules.base.domain.greenhouse import Greenhouse
from sqlalchemy import Integer, String, DateTime, ForeignKey

from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

class GreenhouseModel(BaseModel):
    __tablename__ = 'greenhouses'

    id: Mapped[int] = mapped_column('id', Integer, primary_key=True)
    uuid: Mapped[str] = mapped_column('uuid', String, unique=True, nullable=False)
    name: Mapped[str] = mapped_column('name', String)
    created_at: Mapped[datetime.datetime] = mapped_column('created_at', DateTime)

    sectors = relationship("SectorModel", back_populates="greenhouses")
    flies = relationship("FliesModel", back_populates="greenhouse")

class GreenHouseMapper(ModelMapper):
    @staticmethod
    def to_domain(model: GreenhouseModel):
        return Greenhouse(
            id=model.id,
            uuid=model.uuid,
            name=model.name,
            created_at=model.created_at
        )
    
    @staticmethod
    def to_model(domain: GreenhouseModel):
        return GreenhouseModel(
            id=domain.id,
            uuid=domain.uuid,
            name=domain.name,
            created_at=domain.created_at
        )