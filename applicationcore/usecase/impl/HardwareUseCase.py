from co.edu.uco.invook.applicationcore.domain.inventory.Hardware import Hardware
from co.edu.uco.invook.applicationcore.usecase.GeneralUsecase import GeneralUseCase
from co.edu.uco.invook.crosscutting.exception.impl.BusinessException import DuplicateSerialException, HardwareNotFoundException, MissingFieldException
from co.edu.uco.invook.crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from co.edu.uco.invook.services.inventory.HardwareService import HardwareService

class HardwareUseCase(GeneralUseCase):

    def create(self, **kwargs) -> Hardware:
        
        serial = kwargs.get("serial")
        name = kwargs.get("name")

        if not serial:
            raise MissingFieldException("serial")
        if not name:
            raise MissingFieldException("name")        
        try:
            return HardwareService.create_hardware(**kwargs)
        except DuplicateSerialException:
            raise
        except DatabaseOperationException:
            raise

    def get(self, serial: str) -> Hardware:
        hw = HardwareService.get(serial)
        if not hw:
            raise HardwareNotFoundException(serial)
        return hw

    def patch(self, serial: str, **kwargs) -> Hardware:
        hw = HardwareService.get(serial)
        if not hw:
            raise HardwareNotFoundException(serial)

        return HardwareService.patch_hardware(serial, **kwargs)

    def delete(self, serial: str) -> None:
        hw = HardwareService.get(serial)
        if not hw:
            raise HardwareNotFoundException(serial)

        HardwareService.delete_hardware(hw)

    def list_all(self) -> list[Hardware]:
        return HardwareService.list_all()
