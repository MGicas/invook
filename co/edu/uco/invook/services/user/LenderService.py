from typing import Optional

from django.db import DatabaseError
from ...crosscutting.util.UtilPatch import UtilPatch
from ...crosscutting.util.UtilText import UtilText
from ...crosscutting.exception.impl.BusinessException import BusinessException
from django.db import IntegrityError
from ...crosscutting.exception.impl.BusinessException import LenderNotFoundException
from ...applicationcore.domain.user.Lender import Lender
from ...crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from ...crosscutting.exception.impl.BusinessException import InvalidEmailException

class LenderService:
    
    @staticmethod
    def create_lender(id, rfid, names, surnames, email, phone):
        try:
            lender = Lender.objects.create(
                id = id,
                rfid = rfid,
                names = names,
                surnames = surnames,
                email = email,
                phone = phone
            )

            lender.save()
            return lender
        except IntegrityError as e:
                if "invook_lender.rfid" in str(e):
                    raise BusinessException(f"Ya existe un Lender con el RFID '{rfid}'.")
                elif "invook_lender.id" in str(e):
                    raise BusinessException(f"Ya existe un Lender con el ID '{id}'.")
                else:
                    raise BusinessException("Error de integridad al crear el Lender.") from e
    
    @staticmethod
    def get(id: str) -> Optional[Lender]:
        try:
            return Lender.objects.get(id = id)
        except Lender.DoesNotExist:
            return None
        
    @staticmethod
    def update_lender(lender: Lender, **kwargs) -> Lender:
        if 'id' in kwargs:
            raise ValueError("No se puede cambiar el ID de un Lender.")
        if 'rfid' in kwargs:
            raise ValueError("No se puede cambiar el RFID de un Lender.")

        for key, value in kwargs.items():
            if hasattr(lender, key):
                if isinstance(value, str):
                    value = UtilText.apply_trim(value)
                setattr(lender, key, value)
        lender.save()
        return lender

    
    @staticmethod
    def delete_lender(lender: Lender) -> None:
        try:
            LenderService.get(lender.id)
            lender.delete()
        except Lender.DoesNotExist:
            raise LenderNotFoundException(f"Lender con id '{id}' no existe.")        
        except DatabaseError as e:
            raise DatabaseOperationException("Error al eliminar hardware en la base de datos") from e

    @staticmethod
    def list_all() -> list[Lender]:
        return list(Lender.objects.all())
    
    @staticmethod
    def patch_lender(id: str, **kwargs) -> Lender:
        try:
            lender = Lender.objects.get(id = id)
        except Lender.DoesNotExist:
            raise LenderNotFoundException(f"Lender con id '{id}' no existe.")
        except DatabaseError as e:
            raise DatabaseOperationException("Error al actualizar parcialmente el usuario.") from e
        
        if 'id' in kwargs:
            raise ValueError("No se puede cambiar el ID de un usuario administrativo.")
        if 'rfid' in kwargs:
            raise ValueError("No se puede cambiar el RFID de un Lender.")
        if 'email' in kwargs and not UtilText.email_string_is_valid(kwargs['email']):
            raise InvalidEmailException("El correo electrónico proporcionado no tiene un formato válido.")
 
        
        return UtilPatch.patch_model(lender, kwargs)