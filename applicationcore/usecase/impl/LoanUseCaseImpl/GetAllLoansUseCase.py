from typing import List
from co.edu.uco.invook.applicationcore.domain.resource.Loan import Loan
from co.edu.uco.invook.applicationcore.usecase.loan.IGetAllLoansUseCase import IGetAllLoansUseCase 
from co.edu.uco.invook.infrastructure.data.impl.LoanRepository import LoanRepository

class GetAllLoansUseCase(IGetAllLoansUseCase):
    def __init__(self, repository: LoanRepository):
        self._repository = repository

    def execute(self) -> List[Loan]:
        return self._repository.find_all()
