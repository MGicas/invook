from abc import ABC, abstractmethod
from co.edu.uco.invook.applicationcore.domain.resource.Loan import Loan

class ICreateLoanUseCase(ABC):
    @abstractmethod
    def execute(self, count, rfidLender, idLender, idMonitor, serialHardware, loanDate, returnDate, status):
        pass
