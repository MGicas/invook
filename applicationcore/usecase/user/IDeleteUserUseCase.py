from abc import ABC, abstractmethod

class IDeleteUserUseCase(ABC):
    @abstractmethod
    def execute(self, id: str) -> None:
        pass
