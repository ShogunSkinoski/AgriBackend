from modules.base.domain.ports.greenhouse_repository import GreenhouseRepositoryPort
from modules.base.infra.db.model.greenhouse_model import GreenhouseModel
from seedwork.infra.uow import AbstractUnitOfWorkManager

class GreenhouseRepositoryAdapter(GreenhouseRepositoryPort):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add(self, greenhouse, uow: AbstractUnitOfWorkManager):
        with uow as session:
            session.add(greenhouse)

    def get(self, greenhouse_id, uow: AbstractUnitOfWorkManager):
        with uow as session:
            return session.query(GreenhouseModel).filter_by(id=greenhouse_id).first()

    def get_all(self, uow: AbstractUnitOfWorkManager):
        with uow as session:
            return session.query(GreenhouseModel).all()
            
    def update(self, greenhouse, uow: AbstractUnitOfWorkManager):
        with uow as session:
            session.add(greenhouse)

    def delete(self, greenhouse, uow: AbstractUnitOfWorkManager):
        with uow as session:
            session.delete(greenhouse)