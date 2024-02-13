import datetime
from modules.detection.domain.model.flies import Flies
from seedwork.infra.model_mapper import ModelMapper
from seedwork.utils.base_model import BaseModel

from modules.base.infra.db.model.greenhouse_model import GreenhouseModel

from sqlalchemy import Integer, DateTime, ForeignKey

from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship


class FliesModel(BaseModel):
    __tablename__ = 'flies'

    id: Mapped[int] = mapped_column('id', Integer, primary_key=True)
    flies_count: Mapped[int] = mapped_column('flies_count', Integer)
    created_at: Mapped[datetime.datetime] = mapped_column('created_at', DateTime)
    greenhouse_id: Mapped[int] = mapped_column('greenhouse_id', Integer, ForeignKey('greenhouses.id'))
    greenhouse = relationship("GreenhouseModel", back_populates="flies")
    sector_id: Mapped[int] = mapped_column('sector_id', Integer, ForeignKey('sectors.id'))
    sector = relationship("SectorModel", back_populates="flies")

class FliesModelMapper(ModelMapper):
    @staticmethod
    def to_domain(flies_model: FliesModel) -> Flies:
        flies = Flies(
            id = flies_model.id,
            flies_count=flies_model.flies_count,
            created_at=flies_model.created_at,
            greenhouse_id= flies_model.greenhouse_id,
            sector_id=flies_model.sector_id
            )
       
        return flies

    @staticmethod
    def to_model(flies: Flies) -> FliesModel:
        flies_model = FliesModel(flies_count=flies.flies_count, created_at=flies.created_at, greenhouse_id=flies.greenhouse_id, sector_id=flies.sector_id)
        flies_model.id = flies.id
        return flies_model