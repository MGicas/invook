from co.edu.uco.invook.applicationcore.domain.resource.Loan import Loan
from co.edu.uco.invook.applicationcore.usecase.GeneralUsecase import GeneralUseCase
from co.edu.uco.invook.crosscutting.exception.impl.BusinessException import LoanAlreadyClosedException, LoanNotFoundException, MissingFieldException
from co.edu.uco.invook.crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from co.edu.uco.invook.services.resource.ConsumService import ConsumService
from co.edu.uco.invook.services.resource.LoanService import LoanService

class LoanUseCase():
    
    def create(self, **kwargs) -> Loan:
        idLender = kwargs.get("idLender")
        idMonitor = kwargs.get("idMonitor")
        
        if not idLender:
            raise MissingFieldException("idLender")
        if not idMonitor:
            raise MissingFieldException("idMonitor")        
        try:
            return ConsumService.create_consum(**kwargs)
        except DatabaseOperationException:
            raise
    
    def get(self, id: str) -> Loan:
        loan = LoanService.get(id)
        if not loan:
            raise LoanNotFoundException(id)
        return loan
    
    def patch(self, id: str, **kwargs) -> Loan:
        loan = LoanService.get(id)
        if not loan:
            raise LoanNotFoundException(id)
        return LoanService.patch_loan(id, **kwargs)
    
    def close_loan(self, id: str) -> Loan:
        try:
            return LoanService.close_loan(id)
        except LoanNotFoundException:
            raise
        except LoanAlreadyClosedException:
            raise
        except DatabaseOperationException:
            raise
    
    def list_all(self) -> list[Loan]:
        return LoanService.list_all()

    def return_hardware_loan(self, loan: Loan, serials_to_return: list[str]) -> Loan:
        try:
            return LoanService.return_hardware(loan, serials_to_return)
        except LoanNotFoundException:
            raise
        except LoanAlreadyClosedException:
            raise
        except DatabaseOperationException:
            raise