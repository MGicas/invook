from typing import Optional
from ...crosscutting.util.UtilPatch import UtilPatch
from ...applicationcore.domain.user.AdministrativeUserState import AdministrativeUserState
from ...applicationcore.domain.user.User import User
from ...crosscutting.exception.impl.BusinessException import AdministrativeUserNotFoundException, InvalidPasswordException
from ...crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from ...crosscutting.util.UtilText import UtilText
from ...applicationcore.domain.user.AdministrativeUser import AdministrativeUser
from django.contrib.auth.hashers import make_password, check_password

class AdministrativeUserService:

    @staticmethod
    def create_administrative_user(id, rfid, names, surnames, email, phone, username, password, state, role):
        
        try:
            id = UtilText.apply_trim(id)
            rfid = UtilText.apply_trim(rfid)
            names = UtilText.apply_trim(names)
            surnames = UtilText.apply_trim(surnames)
            email = UtilText.apply_trim(email)
            phone = UtilText.apply_trim(phone)
            username = UtilText.apply_trim(username)
            role = UtilText.apply_trim(role)
        
            admin_user = AdministrativeUser.objects.create(
                id = id,
                rfid = rfid,
                names = names,
                surnames = surnames,
                email = email,
                phone = phone,
                username = username,
                password=make_password(password),
                state = state,
                role = role
            )
            # 
            admin_user.save()
        except Exception as e:
            raise DatabaseOperationException("Error al crear el usuario administrativo en la base de datos.") from e
    
    @staticmethod
    def get(username: str) -> Optional[AdministrativeUser]:
        try:
            return AdministrativeUser.objects.get(username=username)
        except AdministrativeUser.DoesNotExist:
            return None
        except Exception as e:
            raise DatabaseOperationException("Error al consultar usuario administrativo.") from e
        
    @staticmethod
    def patch_administrative_user(username: str, **kwargs) -> AdministrativeUser:
        try:
            admin_user = AdministrativeUser.objects.get(username = username)
        except AdministrativeUser.DoesNotExist:
            raise AdministrativeUserNotFoundException(username)
        except Exception as e:
            raise DatabaseOperationException("Error al actualizar parcialmente el usuario administrativo.") from e
        return UtilPatch.patch_model(admin_user, kwargs)
    
    @staticmethod
    def update_administrative_user(admin_user: AdministrativeUser, **kwargs) -> AdministrativeUser:
        try:
            for key, value in kwargs.items():
                if hasattr(admin_user, key):
                    if isinstance(value, str):
                        value = UtilText.apply_trim(value)
                    setattr(admin_user, key, value)
            admin_user.save()
            return admin_user
        except Exception as e:
            raise DatabaseOperationException("Error al actualizar el usuario administrativo.") from e
    
    @staticmethod
    def delete_administrative_user(admin_user: AdministrativeUser) -> None:
        try:
            admin_user.delete()
        except Exception as e:
            raise DatabaseOperationException("Error al eliminar el usuario administrativo.") from e

    @staticmethod
    def list_all() -> list[AdministrativeUser]:
        try:
            return list(AdministrativeUser.objects.all())
        except Exception as e:
            raise DatabaseOperationException("Error al listar los usuarios administrativos.") from e
    
    @staticmethod
    def mark_unactive(admin_user: AdministrativeUser) -> AdministrativeUser:
        try:
            admin_user.state = AdministrativeUserState.INACTIVO.value
            admin_user.save()
            return admin_user
        except Exception as e:
            raise DatabaseOperationException("Error al marcar usuario como inactivo.") from e

    @staticmethod
    def mark_active(admin_user: AdministrativeUser) -> AdministrativeUser:
        try:
            admin_user.state = AdministrativeUserState.ACTIVO.value
            admin_user.save()
            return admin_user
        except Exception as e:
            raise DatabaseOperationException("Error al marcar usuario como activo.") from e

    @staticmethod
    def change_password(user: User, old_password: str, new_password: str) -> bool:
        try:
            if not check_password(old_password, user.password):
                raise InvalidPasswordException("La contraseña actual es incorrecta.")

            user.password = make_password(new_password)
            user.save()
            return True
        except InvalidPasswordException:
            raise
        except Exception as e:
            raise DatabaseOperationException("Error al cambiar la contraseña del usuario administrativo.") from e
