from typing import Optional
from django.db import IntegrityError, DatabaseError
from ...applicationcore.domain.inventory.HardwareAvailable import HardwareAvailable
from ...crosscutting.util.UtilPatch import UtilPatch
from ...crosscutting.util.UtilText import UtilText
from ...applicationcore.domain.inventory.Hardware import Hardware
from ...applicationcore.domain.inventory.HardwareType import HardwareType
from ...crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from ...crosscutting.exception.impl.BusinessException import DuplicateSerialException, HardwareNotFoundException, InvalidPatchFieldException

class HardwareService:

    @staticmethod
    def create_hardware(serial, name, description, comment, hardware_type, state=None, available=None) -> Hardware:
        try:
            hw_type_instance = HardwareType.objects.get(name__iexact=hardware_type)
                        
            hw, created = Hardware.objects.get_or_create(
                serial=serial,
                defaults={
                    'name': name,
                    'description': description,
                    'comment': comment,
                    'hardware_type': hw_type_instance,
                    'state': state,
                    'available': available
                }
            )

            if not created:
                raise DuplicateSerialException(serial)

            return hw

        except HardwareType.DoesNotExist:
            raise HardwareNotFoundException(hardware_type)
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
        if "serial" in kwargs:
            raise InvalidPatchFieldException("No está permitido modificar el serial del hardware")

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
    def deactivate_hardware(serial: str) -> Hardware:
        try:
            hw = Hardware.objects.get(serial=serial)
            hw.active = False
            hw.available = HardwareAvailable.NO_DISPONIBLE.name  # también lo marcamos como no disponible
            hw.save()
            return hw
        except Hardware.DoesNotExist:
            raise HardwareNotFoundException(serial)
        except DatabaseError as e:
            raise DatabaseOperationException("Error al desactivar hardware en la base de datos") from e

    @staticmethod
    def toggle_availability(hw: Hardware) -> Hardware:
        try:
            if hw.available == HardwareAvailable.DISPONIBLE.value:
                hw.available = HardwareAvailable.NO_DISPONIBLE.value
            else:
                hw.available = HardwareAvailable.DISPONIBLE.value

            hw.save()
            return hw
        except DatabaseError as e:
            raise DatabaseOperationException("Error al marcar hardware como no disponible") from e

    @staticmethod
    def list_all() -> list[Hardware]:
        try:
            return list(Hardware.objects.all())
        except DatabaseError as e:
            raise DatabaseOperationException("Error al listar hardware en la base de datos") from e
        
    @staticmethod
    def list_by_type(hardware_type_id: str) -> list[Hardware]:
        try:
            return list(Hardware.objects.filter(hardware_type_id=hardware_type_id))
        except DatabaseError as e:
            raise DatabaseOperationException("Error al filtrar hardware por tipo en la base de datos") from e
    @staticmethod
    def list_by_type(hardware_type: str) -> list[Hardware]:
        try:
            
            if hardware_type.isdigit():
                return list(Hardware.objects.filter(hardware_type_id=hardware_type))
            return list(Hardware.objects.filter(hardware_type__name__icontains=hardware_type))
        except DatabaseError as e:
            raise DatabaseOperationException("Error al filtrar hardware por tipo en la base de datos") from e
