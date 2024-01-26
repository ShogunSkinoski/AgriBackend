import datetime
from seedwork.utils.base_model import BaseModel

from sqlalchemy import Integer, String, DateTime, ForeignKey

from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

class SectorModel(BaseModel):
    __tablename__ = 'sectors'

    id: Mapped[int] = mapped_column('id', Integer, primary_key=True)
    name: Mapped[str] = mapped_column('name', String)
    greenhouse_id: Mapped[int] = mapped_column('greenhouse_id', Integer, ForeignKey('greenhouses.id'))

    created_at: Mapped[datetime.datetime] = mapped_column('created_at', DateTime)

    greenhouses = relationship("GreenhouseModel", back_populates="sectors")
    flies = relationship("FliesModel", back_populates="sector")