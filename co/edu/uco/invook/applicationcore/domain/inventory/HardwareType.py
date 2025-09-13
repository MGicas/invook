from django.db import models

from ....crosscutting.util.UtilText import UtilText

class HardwareType(models.Model):
    id = models.CharField(max_length = 40, primary_key = True)
    name = models.CharField(max_length = 100, unique = True)
    description = models.TextField()
    
    def save(self, *args, **kwargs):
        self.id = UtilText.apply_trim(self.id)
        self.name = UtilText.apply_trim(self.name)
        self.description = UtilText.apply_trim(self.description)
        
        super().save(*args, **kwargs)

    class Meta:
        app_label = "invook"

    def __str__(self):
        return self.name
    