from abc import ABC, abstractmethod
from co.edu.uco.invook.applicationcore.domain.resource.Loan import Loan

class ICreateLoanUseCase(ABC):
    @abstractmethod
    def execute(self, loan: Loan) -> None:
        pass
