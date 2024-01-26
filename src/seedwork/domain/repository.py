from typing import Generic

from seedwork.utils.generic_response import ResponseType

from abc import ABC, abstractmethod

class GenericRepository(ABC, Generic[ResponseType]):
    @abstractmethod
    def add(self, entity) -> int:
        pass

    @abstractmethod
    def get(self, id) -> ResponseType:
        pass

    @abstractmethod
    def get_all(self) -> list[ResponseType]:
        pass

    @abstractmethod
    def update(self, entity) -> int:
        pass