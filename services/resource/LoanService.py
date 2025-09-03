from typing import Optional
from UtilPatch import UtilPatch
from co.edu.uco.invook.applicationcore.domain.resource.Loan import Loan, LoanStatus
from co.edu.uco.invook.applicationcore.domain.resource.LoanStatus import LoanStatus
from co.edu.uco.invook.crosscutting.util import UtilNumber, UtilText

class LoanService:
    @staticmethod
    def create_loan(self, count, rfidLender, idLender, idMonitor, serialHardware, loanDate, returnDate, status):
        rfidLender = UtilText.apply_trim(rfidLender)
        idLender = UtilText.apply_trim(idLender)
        idMonitor = UtilText.apply_trim(idMonitor)
        serialHardware = UtilText.apply_trim(serialHardware)
        count = UtilNumber.ensure_positive(count)
        
        loan = Loan.objects.create(
            _count = count,
            _rfidLender = rfidLender,
            _idLender = idLender,
            _idMonitor = idMonitor,
            _serialHardware = serialHardware,
            _loanDate = loanDate,
            _returnDate = returnDate,
            _status = status
        )
        return loan
    
    @staticmethod
    def close_loan(loan_id):
        loan = Loan.objects.get(id = loan_id)
        loan._status = LoanStatus.CERRADO.value
        loan.save()
        return loan
    
    @staticmethod
    def get(id: int) -> Optional[Loan]:
        try:
            return Loan.objects.get(id = id)
        except Loan.DoesNotExist:
            return None
        
    @staticmethod
    def update_loan(loan: Loan, **kwargs) -> Loan:
        for key, value in kwargs.items():
            if hasattr(loan, key):
                if isinstance(value, str):
                    value = UtilText.apply_trim(value)
                elif isinstance(value, int):
                    value = UtilNumber.ensure_positive(value)
                setattr(loan, key, value)
        loan.save()
        return loan
    
    @staticmethod
    def list_all() -> list[Loan]:
        return list(Loan.objects.all())
    
    @staticmethod
    def patch_loan(id: int, **kwargs) -> Loan:
        try:
            loan = Loan.objects.get(id = id)
        except Loan.DoesNotExist:
            raise ValueError(f"Loan con id '{id}' no existe.")
        return UtilPatch.patch_model(loan, kwargs)