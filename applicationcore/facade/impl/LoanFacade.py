from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.resource.Loan import Loan
from co.edu.uco.invook.applicationcore.usecase.loan.IDeleteLoanUseCase import IDeleteLoanUseCase
from co.edu.uco.invook.applicationcore.usecase.loan.ICreateLoanUseCase import ICreateLoanUseCase
from co.edu.uco.invook.applicationcore.usecase.loan.IGetAllLoansUseCase import IGetAllLoansUseCase
from co.edu.uco.invook.applicationcore.usecase.loan.IGetLoanByIdUseCase import IGetLoanByIdUseCase

class LoanFacade:
    def __init__(
        self,
        create_loan_uc: ICreateLoanUseCase,
        get_all_loans_uc: IGetAllLoansUseCase,
        get_loan_by_id_uc: IGetLoanByIdUseCase,
        delete_loan_uc: IDeleteLoanUseCase
    ):
        self._create_loan_uc = create_loan_uc
        self._get_all_loans_uc = get_all_loans_uc
        self._get_loan_by_id_uc = get_loan_by_id_uc
        self._delete_loan_uc = delete_loan_uc

    def create_loan(self, loan: Loan) -> None:
        self._create_loan_uc.execute(loan)

    def get_all_loans(self) -> List[Loan]:
        return self._get_all_loans_uc.execute()

    def get_loan_by_id(self, loan_id: str) -> Optional[Loan]:
        return self._get_loan_by_id_uc.execute(loan_id)

    def delete_loan(self, loan_id: str) -> None:
        self._delete_loan_uc.execute(loan_id)
