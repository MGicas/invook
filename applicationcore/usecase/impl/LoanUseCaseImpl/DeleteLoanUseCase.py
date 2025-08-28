from co.edu.uco.invook.applicationcore.usecase.loan.IDeleteLoanUseCase import IDeleteLoanUseCase
from co.edu.uco.invook.infrastructure.data.impl.LoanRepository import LoanRepository

class DeleteLoanUseCase(IDeleteLoanUseCase):
    def __init__(self, repository: LoanRepository):
        self._repository = repository

    def execute(self, loan_id: str) -> None:
        self._repository.delete(loan_id)
