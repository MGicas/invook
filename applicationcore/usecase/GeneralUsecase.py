from abc import ABC, abstractmethod

class GeneralUseCase(ABC):
    
    @abstractmethod
    def create(self, **kwargs):
        pass

    @abstractmethod
    def get(self, identifier):
        pass

    @abstractmethod
    def patch(self, identifier, **kwargs):
        pass

    @abstractmethod
    def delete(self, identifier):
        pass

    @abstractmethod
    def list_all(self):
        pass
