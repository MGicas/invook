from django.db import models
from co.edu.uco.invook.applicationcore.domain.inventory import Supply
from co.edu.uco.invook.applicationcore.domain.resource import ConsumSupply
from co.edu.uco.invook.applicationcore.domain.user import AdministrativeUser, Lender
from co.edu.uco.invook.crosscutting.util.UtilText import UtilText

class Consum(models.Model):
    id = models.CharField(max_length = 40, primary_key = True)
    id_lender = models.ForeignKey(Lender, on_delete = models.CASCADE)
    id_monitor = models.ForeignKey(AdministrativeUser, on_delete = models.CASCADE)

    supplies = models.ManyToManyField(Supply, through = 'ConsumSupply', related_name = 'consumed_supplies')

    def save(self, *args, **kwargs):
        self.id = UtilText.apply_trim(self.id)
        
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Consum {self.id} - {self.id_lender} - {self.id_monitor}"
