from typing import Optional
from UtilPatch import UtilPatch
from co.edu.uco.invook.applicationcore.domain.user.AdministrativeUserState import AdministrativeUserState
from co.edu.uco.invook.applicationcore.domain.user.User import User
from co.edu.uco.invook.crosscutting.util import UtilNumber, UtilText
from co.edu.uco.invook.applicationcore.domain.user.AdministrativeUser import AdministrativeUser
from django.contrib.auth.hashers import make_password, check_password

class AdministrativeUserService:

    @staticmethod
    def create_administrative_user(username, password, state, role):
        admin_user = AdministrativeUser.objects.create(
            username = username,
            password = password,
            state = state,
            role = role
        )

        admin_user.save()
        return admin_user
    
    @staticmethod
    def get(username: str) -> Optional[AdministrativeUser]:
        try:
            return AdministrativeUser.objects.get(username = username)
        except AdministrativeUser.DoesNotExist:
            return None
        
    @staticmethod
    def patch_administrative_user(username: str, **kwargs) -> AdministrativeUser:
        try:
            admin_user = AdministrativeUser.objects.get(username = username)
        except AdministrativeUser.DoesNotExist:
            raise ValueError(f"AdministrativeUser con username '{username}' no existe.")
        return UtilPatch.patch_model(admin_user, kwargs)
    
    @staticmethod
    def update_administrative_user(admin_user: AdministrativeUser, **kwargs) -> AdministrativeUser:
        for key, value in kwargs.items():
            if hasattr(admin_user, key):
                if isinstance(value, str):
                    value = UtilText.apply_trim(value)
                setattr(admin_user, key, value)
        admin_user.save()
        return admin_user
    
    @staticmethod
    def delete_administrative_user(admin_user: AdministrativeUser) -> None:
        admin_user.delete()
        
    @staticmethod
    def list_all() -> list[AdministrativeUser]:
        return list(AdministrativeUser.objects.all())
    
    @staticmethod
    def mark_unactive(admin_user: AdministrativeUser) -> AdministrativeUser:
        admin_user.state = AdministrativeUserState.INACTIVO.value
        admin_user.save()
        return admin_user

    @staticmethod
    def mark_active(admin_user: AdministrativeUser) -> AdministrativeUser:
        admin_user.state = AdministrativeUserState.ACTIVO.value
        admin_user.save()
        return admin_user

    @staticmethod
    def change_password(user: User, old_password: str, new_password: str) -> bool:
        if not check_password(old_password, user.password):
            return False
        
        user.password = make_password(new_password)
        user.save()
        return True