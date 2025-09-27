from django.db import models
from ..inventory.Hardware import Hardware
from ..inventory.HardwareState import HardwareState
from .Loan import Loan

class LoanHardware(models.Model):
    loan = models.ForeignKey(Loan, on_delete = models.CASCADE)
    hardware = models.ForeignKey(Hardware, on_delete = models.CASCADE)
    returned_at = models.DateTimeField(null=True, blank=True)
    
    return_state = models.CharField(
        max_length=20,
        choices=[(state.name, state.value) for state in HardwareState],
        null=True,
        blank=True
    )

    class Meta:
        unique_together = ('loan', 'hardware')
        app_label = "invook"

    def __str__(self):
        return f"Loan {self.loan.id} - Hardware {self.hardware.serial}"