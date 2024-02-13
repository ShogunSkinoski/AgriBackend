
from abc import ABC

from sqlalchemy.orm import sessionmaker

class AbstractUnitOfWorkManager(ABC):

    def __init__(self, *args, **kwargs):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class SQLAlchemyUnitOfWorkManager(AbstractUnitOfWorkManager):
    def __init__(self, db_engine, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_engine = db_engine
        self.session_factory = sessionmaker(bind=db_engine)

    def __enter__(self):
        self.session = self.session_factory()
        self.session.expire_on_commit = False
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()