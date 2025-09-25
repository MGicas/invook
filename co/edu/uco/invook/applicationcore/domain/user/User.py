from django.db import models
from django.core.validators import RegexValidator

from ....crosscutting.util.UtilText import UtilText

class User(models.Model):
    id = models.CharField(max_length = 15, primary_key = True, editable = False)
    rfid = models.CharField(max_length = 50, unique = True)
    names = models.CharField(max_length = 100)
    surnames = models.CharField(max_length = 100)
    email= models.EmailField(max_length = 70)
    phone = models.CharField(
        max_length = 20,
        validators = [RegexValidator(r'^\+?1?\d{9,15}$')])

    def save(self, *args, **kwargs):
        self.id = UtilText.apply_trim(self.id)
        self.rfid = UtilText.apply_trim(self.rfid)
        self.names = UtilText.apply_trim(self.names)
        self.surnames = UtilText.apply_trim(self.surnames)
        self.email = UtilText.apply_trim(self.email)
        self.phone = UtilText.apply_trim(self.phone)
        
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
        app_label = "invook"

    def __str__(self):
        return self.id