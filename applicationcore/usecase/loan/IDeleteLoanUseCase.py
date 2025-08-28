from abc import ABC, abstractmethod

class IDeleteLoanUseCase(ABC):
    @abstractmethod
    def execute(self, loan_id: str) -> None:
        pass
