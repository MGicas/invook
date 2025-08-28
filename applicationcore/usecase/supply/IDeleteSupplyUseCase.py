from abc import ABC, abstractmethod

class IDeleteSupplyUseCase(ABC):
    @abstractmethod
    def execute(self, supply_id: str) -> None:
        pass
