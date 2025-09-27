from django.db import models
from django.contrib.auth.models import AbstractUser
from .AdministrativeUserState import AdministrativeUserState
from ....crosscutting.util.UtilText import UtilText

ADMIN_GROUP = "ADMIN"
MONITOR_GROUP = "MONITOR"

class AdministrativeUser(AbstractUser):

    username = models.CharField(max_length=100, unique=True)

    state = models.CharField(
        max_length=20,
        choices=[(s.name, s.value) for s in AdministrativeUserState],
        default=AdministrativeUserState.ACTIVO.name,
    )

    @property
    def role(self) -> str:
        if self.groups.filter(name=ADMIN_GROUP).exists():
            return "ADMIN"
        if self.groups.filter(name=MONITOR_GROUP).exists():
            return "MONITOR"
        return "UNKNOWN"

    def clean(self):

        if self.username:
            self.username = UtilText.apply_trim(self.username)
        
        if self.email:
            self.email = UtilText.apply_trim(self.email)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "administrative_user"
        verbose_name = "Administrative User"
        verbose_name_plural = "Administrative Users"