from django.db import models
import UtilNumber
from co.edu.uco.invook.applicationcore.domain.resource import Consum, Supply

class ConsumSupply(models.Model):
    consum = models.ForeignKey('Consum', on_delete=models.CASCADE)  
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE)  
    quantity = models.IntegerField() 

    class Meta:
        unique_together = ('consum', 'supply') 

    def save(self, *args, **kwargs):
        self.quantity = UtilNumber.ensure_positive(self.quantity)
        super().save(*args, **kwargs)






