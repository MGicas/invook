from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from .AdministrativeUserState import AdministrativeUserState
from .AdministrativeUserRole import AdministrativeUserRole
from ....crosscutting.util.UtilText import UtilText
from .User import User

class AdministrativeUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("El usuario debe tener un nombre de usuario")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, password, **extra_fields)


class AdministrativeUser(User, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    state = models.CharField(
        max_length=20,
        choices=[(state.name, state.value) for state in AdministrativeUserState],
        default=AdministrativeUserState.ACTIVO.name
    )
    role = models.CharField(
        max_length=20,
        choices=[(role.name, role.value) for role in AdministrativeUserRole],
        default=AdministrativeUserRole.MONITOR.name
    )
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS: list[str] = [] 

    objects = AdministrativeUserManager()

    def save(self, *args, **kwargs):
        self.username = UtilText.apply_trim(self.username)
        self.password = UtilText.apply_trim(self.password)
        super().save(*args, **kwargs)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return f"AdministrativeUser {self.username} - {self.state} - {self.role}"
