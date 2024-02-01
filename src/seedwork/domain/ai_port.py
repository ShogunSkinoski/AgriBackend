from abc import ABC, abstractmethod

class AIPort(ABC):

    @abstractmethod
    def predict(self, prediction_input):
        pass