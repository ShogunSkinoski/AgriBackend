import datetime
from modules.base.domain.sector import Sector
from seedwork.utils.base_model import BaseModel

from sqlalchemy import Integer, String, DateTime, ForeignKey
from seedwork.infra.model_mapper import ModelMapper
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

class SectorModel(BaseModel):
    __tablename__ = 'sectors'

    id: Mapped[int] = mapped_column('id', Integer, primary_key=True)
    uuid: Mapped[str] = mapped_column('uuid', String, unique=True, nullable=False)
    name: Mapped[str] = mapped_column('name', String)
    greenhouse_id: Mapped[int] = mapped_column('greenhouse_id', Integer, ForeignKey('greenhouses.id'))

    created_at: Mapped[datetime.datetime] = mapped_column('created_at', DateTime)

    greenhouses = relationship("GreenhouseModel", back_populates="sectors")
    flies = relationship("FliesModel", back_populates="sector")

class SectorMapper(ModelMapper):
    @staticmethod
    def to_domain(model: SectorModel) -> Sector:
        return Sector(
            id=model.id,
            uuid=model.uuid,
            name=model.name,
            greenhouse_id=model.greenhouse_id,
            created_at=model.created_at
        )
    
    @staticmethod
    def to_model(domain: Sector) -> SectorModel:
        return SectorModel(
            id=domain.id,
            uuid=domain.uuid,
            name=domain.name,
            greenhouse_id=domain.greenhouse_id,
            created_at=domain.created_at
        )