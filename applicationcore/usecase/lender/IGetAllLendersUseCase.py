from abc import ABC, abstractmethod
from typing import List
from co.edu.uco.invook.applicationcore.domain.user.Lender import Lender

class IGetAllLendersUseCase(ABC):
    @abstractmethod
    def execute(self) -> List[Lender]:
        pass
