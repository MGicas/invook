from abc import ABC, abstractmethod
from typing import List
from co.edu.uco.invook.applicationcore.domain.resource.Loan import Loan

class IGetAllLoansUseCase(ABC):
    @abstractmethod
    def execute(self) -> List[Loan]:
        pass
