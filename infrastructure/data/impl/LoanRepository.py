from abc import ABC, abstractmethod
from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.resource.Loan import Loan


class LoanRepository(ABC):

    @abstractmethod
    def find_all(self) -> List[Loan]:
        pass

    @abstractmethod
    def save(self, loan: Loan) -> None:
        pass

    @abstractmethod
    def find_by_id(self, loan_id: str) -> Optional[Loan]:
        pass

    @abstractmethod
    def delete(self, loan_id: str) -> None:
        pass
