from co.edu.uco.invook.applicationcore.domain.resource import Loan, LoanStatus
from co.edu.uco.invook.crosscutting.util import UtilNumber, UtilText

class LoanService:
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
    
    def close_loan(self, loan_id):
        loan = Loan.objects.get(id = loan_id)
        loan._status = LoanStatus.CERRADO.name
        loan.save()
        return loan