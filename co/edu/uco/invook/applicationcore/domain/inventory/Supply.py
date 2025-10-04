from django.db import models
from .SupplyType import SupplyType
from ....crosscutting.util.UtilText import UtilText
from ....crosscutting.util.UtilNumber import UtilNumber

class Supply(models.Model):
    code = models.CharField(max_length = 100, primary_key = True)
    name = models.CharField(max_length = 100, unique = True)
    description = models.TextField()
    supply_type = models.ForeignKey(SupplyType, on_delete = models.CASCADE)
    count = models.IntegerField()
    quantity = models.IntegerField()
    stock = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    
    class Meta:
        app_label = "invook"
        
    def __str__(self):
        return f"Supply {self.code} - {self.name} - {self.stock}"
