from django.db import models
from django.core.validators import RegexValidator
from .AdministrativeUser import AdministrativeUser
from ....crosscutting.util.UtilText import UtilText

class AdministrativeProfile(models.Model):
    
    user = models.OneToOneField(
        AdministrativeUser, on_delete=models.CASCADE, related_name="profile"
    )

    rfid = models.CharField(max_length=50, unique=True)
    names = models.CharField(max_length=100)
    surnames = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=20,
        validators=[RegexValidator(r"^\+?1?\d{9,15}$")],
    )
    document_id = models.CharField(max_length=20, unique=True)

    def clean(self):
        if self.document_id:
            self.document_id = UtilText.apply_trim(self.document_id)
        if self.rfid:
            self.rfid = UtilText.apply_trim(self.rfid)
        if self.names:
            self.names = UtilText.apply_trim(self.names)
        if self.surnames:
            self.surnames = UtilText.apply_trim(self.surnames)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "administrative_profile"
        verbose_name = "Administrative Profile"
        verbose_name_plural = "Administrative Profiles"

    def __str__(self):
        return f"{self.document_id} - {self.names} {self.surnames}"