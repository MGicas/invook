from co.edu.uco.invook.applicationcore.domain.resource import Loan, LoanStatus
from co.edu.uco.invook.crosscutting.util import UtilNumber, UtilText
from co.edu.uco.invook.applicationcore.domain.resource.Consum import Consum

class ConsumService:
    def create_consum(self, count, rfidLender, idLender, idMonitor, codeSupply, quantity):
        rfidLender = UtilText.apply_trim(rfidLender)
        idLender = UtilText.apply_trim(idLender)
        idMonitor = UtilText.apply_trim(idMonitor)
        codeSupply = UtilText.apply_trim(codeSupply)
        count = UtilNumber.ensure_positive(count)
        quantity = UtilNumber.ensure_positive(quantity)
        
        consum = Consum.objects.create(
            _count = count,
            _rfidLender = rfidLender,
            _idLender = idLender,
            _idMonitor = idMonitor,
            _codeSupply = codeSupply,
            _quantity = quantity
        )
        return consum