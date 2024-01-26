import datetime
from modules.detection.infra.db.model.flies_model import FliesModel
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:perhap5gell@localhost:3306/ai4agriculture', echo=True, future=True)

with Session(engine) as session:
    flies_model = FliesModel(flies_count=1, created_at= datetime.datetime.now().strftime("%Y-%m-%d"), greenhouse_id=2, sector_id=1)
    session.add(flies_model)
    session.commit()