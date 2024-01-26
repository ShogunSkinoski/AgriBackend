from modules.detection.domain.ports.repository import FliesRepositoryPort
from modules.detection.domain.model.flies import Flies

class SQLAlchemyFliesAdapter(FliesRepositoryPort):
    def __init__(self, session):
        self.session = session
    
    def add(self, flies):
        self.session.add(flies)
    
    def get(self, flies_id):
        return self.session.query(Flies).filter_by(id=flies_id).first()
    
    def get_all(self):
        return self.session.query(Flies).all()
    
    def update(self, flies):
        self.session.add(flies)
    
    def delete(self, flies):
        self.session.delete(flies)
    
    def commit(self):
        self.session.commit()
    
    def rollback(self):
        self.session.rollback()