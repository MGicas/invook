from typing import Optional
from co.edu.uco.invook.applicationcore.domain.inventory.HardwareAvailable import HardwareAvailable
from co.edu.uco.invook.crosscutting.util import UtilPatch, UtilText
from co.edu.uco.invook.applicationcore.domain.inventory.Hardware import Hardware

class HardwareService:

    @staticmethod
    def create_hardware(serial, name, description, comment, hardware_type, state=None, available=None) -> Hardware:
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

    @staticmethod
    def get(serial: str) -> Optional[Hardware]:
        try:
            return Hardware.objects.get(serial = serial)
        except Hardware.DoesNotExist:
            return None

    @staticmethod
    def patch_hardware(serial: str, **kwargs) -> Hardware:
        try:
            hw = Hardware.objects.get(serial = serial)
        except Hardware.DoesNotExist:
            raise ValueError(f"Hardware con serial '{serial}' no existe.")
        return UtilPatch.patch_model(hw, kwargs)
    
    @staticmethod
    def update_hardware(hw: Hardware, **kwargs) -> Hardware:
        for key, value in kwargs.items():
            if hasattr(hw, key):
                if isinstance(value, str):
                    value = UtilText.apply_trim(value)
                setattr(hw, key, value)
        hw.save()
        return hw

    @staticmethod
    def delete_hardware(hw: Hardware) -> None:
        hw.delete()

    @staticmethod
    def mark_unavailable(hw: Hardware) -> Hardware:
        hw.available = HardwareAvailable.DISPONIBLE.value
        hw.save()
        return hw

    @staticmethod
    def mark_available(hw: Hardware) -> Hardware:
        hw.available = HardwareAvailable.DISPONIBLE.value
        hw.save()
        return hw   

    @staticmethod
    def list_all() -> list[Hardware]:
        return list(Hardware.objects.all())