
from seedwork.infra.uow import AbstractUnitOfWorkManager
from sqlalchemy.orm import sessionmaker


class SQLAlchemyUnitOfWorkManager(AbstractUnitOfWorkManager):
    def __init__(self, db_engine, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_engine = db_engine
        self.session_factory = sessionmaker(bind=db_engine)

    def __enter__(self):
        self.session = self.session_factory()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()
