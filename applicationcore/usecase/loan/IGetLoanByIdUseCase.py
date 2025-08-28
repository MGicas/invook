from abc import ABC, abstractmethod
from typing import Optional
from co.edu.uco.invook.applicationcore.domain.resource.Loan import Loan

class IGetLoanByIdUseCase(ABC):
    @abstractmethod
    def execute(self, loan_id: str) -> Optional[Loan]:
        pass
