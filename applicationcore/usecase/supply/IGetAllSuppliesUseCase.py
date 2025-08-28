from abc import ABC, abstractmethod
from typing import List
from co.edu.uco.invook.applicationcore.domain.inventory.Supply import Supply

class IGetAllSuppliesUseCase(ABC):
    @abstractmethod
    def execute(self) -> List[Supply]:
        pass
