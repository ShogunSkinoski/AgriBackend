import datetime
from seedwork.utils.base_model import BaseModel

from modules.base.infra.db.model.greenhouse_model import GreenhouseModel

from sqlalchemy import Integer, String, DateTime, ForeignKey

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