from abc import ABC, abstractmethod
from co.edu.uco.invook.applicationcore.domain.inventory.Supply import Supply

class ICreateSupplyUseCase(ABC):
    @abstractmethod
    def execute(self, supply: Supply) -> None:
        pass
