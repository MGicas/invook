from django.db import models
from django.contrib.auth.hashers import make_password
from .AdministrativeUserState import AdministrativeUserState
from .AdministrativeUserRole import AdministrativeUserRole
from ....crosscutting.util.UtilText import UtilText
from .User import User
from django.core.validators import RegexValidator

class AdministrativeUser(User, models.Model):
    username = models.CharField(max_length = 100, unique = True)
    password = models.CharField(max_length = 100)  
    state = models.CharField(
        max_length = 20,
        choices = [(state.name, state.value) for state in AdministrativeUserState],
        default = AdministrativeUserState.ACTIVO.name
    )
    role = models.CharField(
        max_length = 20,
        choices = [(role.name, role.value) for role in AdministrativeUserRole],
        default = AdministrativeUserRole.MONITOR.name
    )

    class Meta:
        indexes = [
            models.Index(fields =['username']),
        ]
    
    def save(self, *args, **kwargs):
        self._username = UtilText.apply_trim(self._username)
        self._password = UtilText.apply_trim(self._password)
        
        super().save(*args, **kwargs)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        
    def __str__(self):
        return f"AdministrativeUser {self._username} - {self._state}"

    def __str__(self):
        return f"AdministrativeUser: {self._username} ({self._role})"    

