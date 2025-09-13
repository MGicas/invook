from ...domain.inventory.Hardware import Hardware
from ...usecase.GeneralUsecase import GeneralUseCase
from ....crosscutting.exception.impl.BusinessException import DuplicateSerialException, HardwareNotFoundException, MissingFieldException
from ....crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from ....services.inventory.HardwareService import HardwareService

class HardwareUseCase(GeneralUseCase):
    service = HardwareService()

    def create(self, **kwargs) -> Hardware:
        
        serial = kwargs.get("serial")
        name = kwargs.get("name")

        if not serial:
            raise MissingFieldException("serial")
        if not name:
            raise MissingFieldException("name")        
        try:
            return self.service.create_hardware(**kwargs)
        except DuplicateSerialException:
            raise
        except DatabaseOperationException:
            raise

    def get(self, serial: str) -> Hardware:
        hw = self.service.get(serial)
        if not hw:
            raise HardwareNotFoundException(serial)
        return hw

    def patch(self, serial: str, **kwargs) -> Hardware:
        hw = HardwareService.get(serial)
        if not hw:
            raise HardwareNotFoundException(serial)

        return self.service.patch_hardware(serial, **kwargs)

    def delete(self, serial: str) -> None:
        hw = self.service.get(serial)
        if not hw:
            raise HardwareNotFoundException(serial)

        self.service.delete_hardware(hw)

    def list_all(self) -> list[Hardware]:
        return HardwareService.list_all()
    
    def toggle_availability(self, serial: str) -> Hardware:
        hw = self.service.get(serial)
        return self.service.toggle_availability(hw)
