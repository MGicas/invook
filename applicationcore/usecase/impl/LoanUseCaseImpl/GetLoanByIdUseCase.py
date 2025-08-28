from typing import Optional
from co.edu.uco.invook.applicationcore.domain.resource.Loan import Loan
from co.edu.uco.invook.applicationcore.usecase.loan.IGetLoanByIdUseCase import IGetLoanByIdUseCase 
from co.edu.uco.invook.infrastructure.data.impl.LoanRepository import LoanRepository


class GetLoanByIdUseCase(IGetLoanByIdUseCase):
    def __init__(self, repository: LoanRepository):
        self._repository = repository

    def execute(self, loan_id: str) -> Optional[Loan]:
        return self._repository.find_by_id(loan_id)
