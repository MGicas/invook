from django.db import models
from co.edu.uco.invook.applicationcore.domain.inventory.SupplyType import SupplyType
from co.edu.uco.invook.crosscutting.util.UtilText import UtilText
from co.edu.uco.invook.crosscutting.util.UtilNumber import UtilNumber

class Supply(models.Model):
    code = models.CharField(max_length = 100, primary_key = True, editable=False)
    name = models.CharField(max_length = 100, unique = True)
    description = models.TextField()
    supply_type = models.ForeignKey(SupplyType, on_delete = models.CASCADE)
    count = models.IntegerField()
    quantity = models.IntegerField()
    stock = models.IntegerField()
    
    def save(self, *args, **kwargs):
        self.code = UtilText.apply_trim(self.code)
        self.name = UtilText.apply_trim(self.name)
        self.description = UtilText.apply_trim(self.description)
        self.count = UtilNumber.ensure_positive(self.count)
        self.quantity = UtilNumber.ensure_positive(self.quantity)
        self.stock = self.count * self.quantity
        
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Supply {self.code} - {self.name} - {self.stock}"
