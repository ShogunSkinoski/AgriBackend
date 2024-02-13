from modules.base.domain.ports.sector_repository import SectorRepositoryPort
from modules.base.infra.db.model.sector_model import SectorModel
from seedwork.infra.uow import AbstractUnitOfWorkManager

class SectorRepositoryAdapter(SectorRepositoryPort):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add(self, sector, uow: AbstractUnitOfWorkManager):
        with uow as session:
            session.add(sector)

    def get(self, sector_id, uow: AbstractUnitOfWorkManager):
        with uow as session:
            return session.query(SectorModel).filter_by(id=sector_id).first()

    def get_all(self, uow: AbstractUnitOfWorkManager):
        with uow as session:
            return session.query(SectorModel).all()
        
    def get_all_by_greenhouse(self, greenhouse_id, uow: AbstractUnitOfWorkManager):
        with uow as session:
            return session.query(SectorModel).filter_by(greenhouse_id=greenhouse_id).all()

    def update(self, sector, uow: AbstractUnitOfWorkManager):
        with uow as session:
            session.add(sector)

    def delete(self, sector, uow: AbstractUnitOfWorkManager):
        with uow as session:
            session.delete(sector)