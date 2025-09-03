from django.db import models
from co.edu.uco.invook.applicationcore.domain.inventory import Hardware
from co.edu.uco.invook.crosscutting.util import UtilText
from co.edu.uco.invook.applicationcore.domain.resource import LoanStatus

class Loan(models.Model): 
    id = models.CharField(max_length = 40, primary_key = True, editable = False)
    id_lender = models.CharField(max_length = 100)
    id_monitor = models.CharField(max_length = 100)
    loan_date = models.DateTimeField(auto_now_add = True)
    return_date = models.DateTimeField()
    status = models.CharField(
        max_length = 20,
        choices = [(status.name, status.value) for status in LoanStatus],
        default = LoanStatus.ABIERTO.name
    )

    hardware = models.ManyToManyField(Hardware, through = 'LoanHardware', related_name = 'loans')

    def save(self, *args, **kwargs):
        self.id = UtilText.apply_trim(self.id)
        self.id_lender = UtilText.apply_trim(self.id_lender)
        self.id_monitor = UtilText.apply_trim(self.id_monitor)
        
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Loan {self.id} - {self.status}"
    