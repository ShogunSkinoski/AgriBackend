import datetime
from seedwork.utils.base_model import BaseModel

from modules.base.infra.db.model.sector_model import SectorModel

from sqlalchemy import Integer, String, DateTime, ForeignKey

from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

class GreenhouseModel(BaseModel):
    __tablename__ = 'greenhouses'

    id: Mapped[int] = mapped_column('id', Integer, primary_key=True)
    name: Mapped[str] = mapped_column('name', String)
    created_at: Mapped[datetime.datetime] = mapped_column('created_at', DateTime)

    sectors = relationship("SectorModel", back_populates="greenhouses")
    flies = relationship("FliesModel", back_populates="greenhouse")