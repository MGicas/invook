from abc import ABC, abstractmethod
from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.user.Lender import Lender

class LenderRepository(ABC):

    @abstractmethod
    def find_all(self) -> List[Lender]:
        pass

    @abstractmethod
    def save(self, lender: Lender) -> None:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[Lender]:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass
