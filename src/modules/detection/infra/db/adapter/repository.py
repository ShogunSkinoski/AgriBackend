from modules.detection.domain.ports.repository import FliesRepositoryPort
from modules.detection.infra.db.model.flies_model import FliesModel
from seedwork.infra.uow import AbstractUnitOfWorkManager

class FliesRepositoryAdapter(FliesRepositoryPort):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add(self, flies, uow: AbstractUnitOfWorkManager):
        with uow as session:
            session.add(flies)

    def get(self, flies_id, uow: AbstractUnitOfWorkManager):
        with uow as session:
            return session.query(FliesModel).filter_by(id=flies_id).first()

    def get_all(self, uow: AbstractUnitOfWorkManager):
        with uow as session:
            return session.query(FliesModel).all()
    def get_all_by_sector(self, sector_id, uow: AbstractUnitOfWorkManager):
        with uow as session:
            return session.query(FliesModel).filter_by(sector_id=sector_id).all()
    def update(self, flies, uow: AbstractUnitOfWorkManager):
        with uow as session:
            session.add(flies)

    def delete(self, flies, uow: AbstractUnitOfWorkManager):
        with uow as session:
            session.delete(flies)