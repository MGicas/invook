from django.db import models
from co.edu.uco.invook.applicationcore.domain.inventory.HardwareType import HardwareType
from co.edu.uco.invook.applicationcore.domain.inventory.HardwareState import HardwareState
from co.edu.uco.invook.applicationcore.domain.inventory.HardwareAvailable import HardwareAvailable
from co.edu.uco.invook.crosscutting.util.UtilText import UtilText

class Hardware(models.Model):

    serial = models.CharField(max_length = 50, primary_key = True, editable=False)
    name = models.CharField(max_length = 100)
    description = models.TextField()
    comment = models.TextField()
    state = models.CharField(
        max_length = 20,
        choices = [(state.name, state.value) for state in HardwareState],
        default = HardwareState.BUENO.name
    )
    hardware_type = models.ForeignKey(HardwareType, on_delete = models.CASCADE)
    available = models.CharField(
        max_length = 20,
        choices = [(available.name, available.value) for available in HardwareAvailable],
        default = HardwareAvailable.DISPONIBLE.name
    )
    
    def save(self, *args, **kwargs):
        self.serial = UtilText.apply_trim(self.serial)
        self.name = UtilText.apply_trim(self.name)
        self.description = UtilText.apply_trim(self.description)
        self.comment = UtilText.apply_trim(self.comment)
        
        super().save(*args, **kwargs)

    class Meta:
        app_label = "invook"
        
    def __str__(self):
        return f"Hardware {self.serial} - {self.name} - {self._state} - {self.available}"
