
from abc import ABC, abstractmethod
from typing import Any

from seedwork.utils.base_model import BaseModel


class ModelMapper(ABC):
    @staticmethod
    @abstractmethod
    def to_domain(model: BaseModel) -> Any:
        pass

    @staticmethod
    @abstractmethod
    def to_model(domain: Any) -> BaseModel:
        pass