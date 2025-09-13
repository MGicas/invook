from django.db import models
from ...domain.user.Lender import Lender
from ...domain.user.AdministrativeUser import AdministrativeUser
from ....crosscutting.util.UtilText import UtilText

class Consum(models.Model):
    id = models.CharField(max_length = 40, primary_key = True, editable=False)
    id_lender = models.ForeignKey(Lender, on_delete = models.CASCADE)
    id_monitor = models.ForeignKey(AdministrativeUser, on_delete = models.CASCADE)

    supplies = models.ManyToManyField('invook.Supply', through = 'ConsumSupply', related_name = 'consumed_supplies')

    def save(self, *args, **kwargs):
        self.id = UtilText.apply_trim(self.id)
        
        super().save(*args, **kwargs)

    class Meta:
        app_label = "invook"


    def __str__(self):
        return f"Consum {self.id} - {self.id_lender} - {self.id_monitor}"
