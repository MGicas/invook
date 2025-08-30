from django.db import models
from co.edu.uco.invook.crosscutting.util import UtilNumber, UtilText
from co.edu.uco.invook.applicationcore.domain.resource import LoanStatus

class Loan(models.Model):
    id = models.CharField(max_length = 40)
    rfidLender = models.CharField(max_length = 100)
    idLender = models.CharField(max_length = 100)
    idMonitor = models.CharField(max_length = 100)
    serialHardware = models.CharField(max_length = 100)
    loanDate = models.DateTimeField(auto_now_add = True)
    returnDate = models.DateTimeField()
    status = models.CharField(
        max_length = 20,
        choices = [(status.name, status.value) for status in LoanStatus],
        default = LoanStatus.ABIERTO.name
    )

    def save(self, *args, **kwargs):
        self._id = UtilText.apply_trim(self.id)
        self._rfidLender = UtilText.apply_trim(self.rfidLender)
        self._idLender = UtilText.apply_trim(self.idLender)
        self._idMonitor = UtilText.apply_trim(self.idMonitor)
        self._serialHardware = UtilText.apply_trim(self.serialHardware)
        self._count = UtilNumber.ensure_positive(self.count)
        
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Loan {self._id} - {self._status}"
    