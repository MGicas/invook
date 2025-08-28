from abc import ABC, abstractmethod

class IDeleteConsumUseCase(ABC):
    @abstractmethod
    def execute(self, consum_id: str) -> None:
        pass
