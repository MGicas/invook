from co.edu.uco.invook.applicationcore.domain.resource.Loan import Loan
from co.edu.uco.invook.applicationcore.usecase.loan.ICreateLoanUseCase import ICreateLoanUseCase
from co.edu.uco.invook.infrastructure.data.impl.LoanRepository import LoanRepository

class CreateLoanUseCase(ICreateLoanUseCase):
    def __init__(self, repository: LoanRepository):
        self._repository = repository

    def execute(self, loan: Loan) -> None:
        self._repository.save(loan)

