from ...domain.resource.Loan import Loan
from ...usecase.GeneralUsecase import GeneralUseCase
from ....crosscutting.exception.impl.BusinessException import LoanAlreadyClosedException, LoanNotFoundException, MissingFieldException
from ....crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from ....services.resource.ConsumService import ConsumService
from ....services.resource.LoanService import LoanService

class LoanUseCase():
    service = LoanService()
    
    def create(self, **kwargs) -> Loan:
        serial = kwargs.get("serialHardware")
        lender_id = kwargs.get("idLender")
        monitor_id = kwargs.get("idMonitor")
        loan_date = kwargs.get("loanDate")
        return_date = kwargs.get("returnDate")
        status = kwargs.get("status")

        if not lender_id:
            raise MissingFieldException("Lender ID is required.")
        if not monitor_id:
            raise MissingFieldException("Monitor ID is required.")
        if not serial:
            raise MissingFieldException("Hardware serial is required.")
        if not loan_date:
            raise MissingFieldException("Loan date is required.")
        if not return_date:
            raise MissingFieldException("Return date is required.")

        try:
            return self.service.create_loan(
                idLender=lender_id,
                idMonitor=monitor_id,
                serialHardware=serial,
                loanDate=loan_date,
                returnDate=return_date,
                status=status
            )
        except DatabaseOperationException as e:
            raise e
    
    def get(self, id: str) -> Loan:
        loan = self.service.get(id)
        if not loan:
            raise LoanNotFoundException(id)
        return loan
    
    def patch(self, id: str, **kwargs) -> Loan:
        loan = LoanService.get(id)
        if not loan:
            raise LoanNotFoundException(id)
        return self.service.patch_loan(id, **kwargs)
    
    def close_loan(self, id: str) -> Loan:
        try:
            return self.service.close_loan(id)
        except LoanNotFoundException:
            raise
        except LoanAlreadyClosedException:
            raise
        except DatabaseOperationException:
            raise
    
    def list_all(self) -> list[Loan]:
        return LoanService.list_all()

    def add_hardware(self, loan_id: str, serialHardware: str) -> Loan:
        try:
            return self.service.add_hardware_to_loan(loan_id, serialHardware)
        except LoanNotFoundException as e:
            raise e

    def return_hardware_loan(self, loan: Loan, serials_to_return: list[str]) -> Loan:
        try:
            return self.service.return_hardware(loan, serials_to_return)
        except LoanNotFoundException:
            raise
        except LoanAlreadyClosedException:
            raise
        except DatabaseOperationException:
            raise

