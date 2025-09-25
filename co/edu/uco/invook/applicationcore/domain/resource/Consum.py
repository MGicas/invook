import uuid
from django.db import models
from ...domain.user.Lender import Lender
from ...domain.user.AdministrativeUser import AdministrativeUser
from ....crosscutting.util.UtilText import UtilText

class Consum(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_lender = models.ForeignKey(Lender, on_delete = models.CASCADE)
    id_monitor = models.ForeignKey(AdministrativeUser, on_delete = models.CASCADE)
    
    supplies = models.ManyToManyField('invook.Supply', through = 'ConsumSupply')

    class Meta:
        app_label = "invook"


    def __str__(self):
        return f"Consum {self.id} - {self.id_lender} - {self.id_monitor}"
