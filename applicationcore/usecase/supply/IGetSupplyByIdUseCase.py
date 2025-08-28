from abc import ABC, abstractmethod
from typing import Optional
from co.edu.uco.invook.applicationcore.domain.inventory.Supply import Supply

class IGetSupplyByIdUseCase(ABC):
    @abstractmethod
    def execute(self, supply_id: str) -> Optional[Supply]:
        pass
