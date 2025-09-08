from co.edu.uco.invook.applicationcore.domain.resource.Loan import Loan
from co.edu.uco.invook.applicationcore.usecase.GeneralUsecase import GeneralUseCase
from co.edu.uco.invook.services.resource.LoanService import LoanService

class LoanUseCase(GeneralUseCase):
    
    def create(self, **kwargs) -> Loan:
        return LoanService.create_loan(**kwargs)
    
    def get(self, id: int) -> Loan:
        return LoanService.get(id)
    
    def patch(self, id: int, **kwargs) -> Loan:
        return LoanService.patch_loan(id, **kwargs)
    
    def close_loan(self, id: int) -> Loan:
        return LoanService.close_loan(id)
    
    def list_all(self) -> list[Loan]:
        return LoanService.list_all()