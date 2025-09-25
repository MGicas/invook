from typing import Optional
from ...domain.resource.Loan import Loan
from ...usecase.GeneralUsecase import GeneralUseCase
from ....crosscutting.exception.impl.BusinessException import LoanAlreadyClosedException, LoanNotFoundException, MissingFieldException
from ....crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from ....services.resource.ConsumService import ConsumService
from ....services.resource.LoanService import LoanService

class LoanUseCase():
    def __init__(self):
        self.service = LoanService()
    
    def create_loan(self, id_lender: str, id_monitor: str, serials_hardware: list[str], status: Optional[str] = None) -> Loan:
        return self.service.create_loan(id_lender, id_monitor, serials_hardware, status)

    
    def get(self, id: str) -> Loan:
        loan = self.service.get(id)
        if not loan:
            raise LoanNotFoundException(id)
        return loan
    
    def patch(self, id: str, **kwargs) -> Loan:
        loan = self.service.get(id)
        if not loan:
            raise LoanNotFoundException(id)
        return self.service.patch_loan(id, **kwargs)
    
    def close_loan(self, id: str) -> Loan:
        return self.service.close_loan(id)
        
    def list_all(self) -> list[Loan]:
        return self.service.list_all()

    def add_hardware(self, loan_id: str, serials_hardware: list[str]) -> Loan:
        if not isinstance(serials_hardware, list):
            raise MissingFieldException("Se espera una lista de seriales de hardware.")
        return self.service.add_hardware_to_loan(loan_id, serials_hardware)

    def return_hardware_loan(self, loan_id, serials_to_return: list[str]) -> Loan:
        loan = self.service.get(loan_id)
        if not loan:
            raise LoanNotFoundException(loan_id)
        return self.service.return_hardware(loan, serials_to_return)
        

