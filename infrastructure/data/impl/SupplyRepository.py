from abc import ABC, abstractmethod
from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.inventory.Supply import Supply


class SupplyRepository(ABC):
    
    @abstractmethod
    def find_all(self) -> List[Supply]:
        pass

    @abstractmethod
    def save(self, supply: Supply) -> None:
        pass

    @abstractmethod
    def find_by_code(self, code: str) -> Optional[Supply]:
        pass

    @abstractmethod
    def delete(self, code: str) -> None:
        pass
