from django.db import models
from .Consum import Consum
from ....crosscutting.util.UtilNumber import UtilNumber
from ..inventory.Supply import Supply

class ConsumSupply(models.Model):
    consum = models.ForeignKey(Consum, on_delete=models.CASCADE)  
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE)  
    quantity = models.IntegerField(default=1) 

    class Meta:
        unique_together = ('consum', 'supply')
        app_label = "invook" 
