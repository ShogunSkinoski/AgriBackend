from seedwork.domain.ai_port import AIPort
from abc import abstractmethod, abstractproperty

class ColorDetectionPort(AIPort):
    
    def __init__(self, _model):
        self._model = _model
    
    @abstractproperty
    def model(self):
        pass

    @model.setter
    def model(self, _model):
        pass

    @abstractmethod
    async def predict(self, prediction_input):
        pass
