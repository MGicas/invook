from typing import Optional
from django.db import IntegrityError, DatabaseError
from co.edu.uco.invook.applicationcore.domain.inventory.HardwareAvailable import HardwareAvailable
from co.edu.uco.invook.crosscutting.util import UtilPatch, UtilText
from co.edu.uco.invook.applicationcore.domain.inventory.Hardware import Hardware
from co.edu.uco.invook.crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from co.edu.uco.invook.crosscutting.exception.impl.BusinessException import DuplicateSerialException, HardwareNotFoundException

class HardwareService:

    @staticmethod
    def create_hardware(serial, name, description, comment, hardware_type, state=None, available=None) -> Hardware:
        
        try:
            hw = Hardware(
                serial = serial,
                name = name,
                description = description,
                comment = comment,
                hardware_type = hardware_type,
            )

            if state:
                hw.state = state
            if available:
                hw.available = available

            hw.save()
            return hw
        
        except IntegrityError as e:
            raise DuplicateSerialException(serial) from e
        except DatabaseError as e:
            raise DatabaseOperationException("Error al crear hardware en la base de datos") from e


    @staticmethod
    def get(serial: str) -> Optional[Hardware]:
        try:
            return Hardware.objects.get(serial = serial)
        except Hardware.DoesNotExist:
            return None
        except DatabaseError as e:
            raise DatabaseOperationException("Error al consultar hardware en la base de datos") from e

    @staticmethod
    def patch_hardware(serial: str, **kwargs) -> Hardware:
        try:
            hw = Hardware.objects.get(serial = serial)
        except Hardware.DoesNotExist:
            raise HardwareNotFoundException(serial)
        except DatabaseError as e:
            raise DatabaseOperationException("Error al actualizar hardware en la base de datos") from e
        return UtilPatch.patch_model(hw, kwargs)
    
    @staticmethod
    def update_hardware(hw: Hardware, **kwargs) -> Hardware:
        try:
            for key, value in kwargs.items():
                if hasattr(hw, key):
                    if isinstance(value, str):
                        value = UtilText.apply_trim(value)
                    setattr(hw, key, value)
            hw.save()
            return hw
        except DatabaseError as e:
            raise DatabaseOperationException("Error al actualizar hardware en la base de datos") from e

    @staticmethod
    def delete_hardware(hw: Hardware) -> None:
        try:
            hw.delete()
        except DatabaseError as e:
            raise DatabaseOperationException("Error al eliminar hardware en la base de datos") from e

    @staticmethod
    def mark_unavailable(hw: Hardware) -> Hardware:
        try:
            hw.available = HardwareAvailable.NO_DISPONIBLE.value
            hw.save()
            return hw
        except DatabaseError as e:
            raise DatabaseOperationException("Error al marcar hardware como no disponible") from e

    @staticmethod
    def mark_available(hw: Hardware) -> Hardware:
        try:
            hw.available = HardwareAvailable.DISPONIBLE.value
            hw.save()
            return hw
        except DatabaseError as e:
            raise DatabaseOperationException("Error al marcar hardware como disponible") from e
   
    @staticmethod
    def list_all() -> list[Hardware]:
        try:
            return list(Hardware.objects.all())
        except DatabaseError as e:
            raise DatabaseOperationException("Error al listar hardware en la base de datos") from e