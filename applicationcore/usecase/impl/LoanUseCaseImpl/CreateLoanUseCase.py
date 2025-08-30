from co.edu.uco.invook.applicationcore.domain.resource.Loan import Loan
from co.edu.uco.invook.applicationcore.usecase.loan.ICreateLoanUseCase import ICreateLoanUseCase
from co.edu.uco.invook.services.resource import LoanService

class CreateLoanUseCase(ICreateLoanUseCase):
    def __init__(self, loan_service: LoanService):
        self.loan_service = loan_service

    def execute(self, count, rfidLender, idLender, idMonitor, serialHardware, loanDate, returnDate, status):
        if count <= 0:
            raise ValueError("La cantidad de ")

