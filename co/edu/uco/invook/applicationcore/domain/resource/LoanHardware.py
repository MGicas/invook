from django.db import models
from ..inventory.Hardware import Hardware
from .Loan import Loan

class LoanHardware(models.Model):
    loan = models.ForeignKey(Loan, on_delete = models.CASCADE)
    hardware = models.ForeignKey(Hardware, on_delete = models.CASCADE)

    class Meta:
        unique_together = ('loan', 'hardware')
        app_label = "invook"

    def __str__(self):
        return f"Loan {self.loan.id} - Hardware {self.hardware.serial}"