from django.db import models
from .LoanStatus import LoanStatus
from ....crosscutting.util.UtilText import UtilText
from ..user.Lender import Lender
from ..user.AdministrativeUser import AdministrativeUser

class Loan(models.Model): 
    id = models.CharField(max_length = 40, primary_key = True, editable = False)
    id_lender = models.ForeignKey(Lender, on_delete = models.CASCADE)
    id_monitor = models.ForeignKey(AdministrativeUser, on_delete = models.CASCADE)
    loan_date = models.DateTimeField(auto_now_add = True)
    return_date = models.DateTimeField()
    status = models.CharField(
        max_length = 20,
        choices = [(status.name, status.value) for status in LoanStatus],
        default = LoanStatus.ABIERTO.value
    )

    hardware = models.ManyToManyField('invook.Hardware', through = 'LoanHardware', related_name = 'loans')

    def save(self, *args, **kwargs):
        self.id = UtilText.apply_trim(self.id)
        self.id_lender = UtilText.apply_trim(self.id_lender)
        self.id_monitor = UtilText.apply_trim(self.id_monitor)
        
        super().save(*args, **kwargs)

    class Meta:
        app_label = "invook"
        
    def __str__(self):
        return f"Loan {self.id} - {self.status}"
    