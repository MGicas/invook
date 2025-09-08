from co.edu.uco.invook.applicationcore.domain.inventory.Hardware import Hardware
from co.edu.uco.invook.applicationcore.usecase.GeneralUsecase import GeneralUseCase
from co.edu.uco.invook.services.inventory.HardwareService import HardwareService

class HardwareUseCase(GeneralUseCase):

    def create(self, **kwargs) -> Hardware:
        #Logica de negocio
        return HardwareService.create_hardware(**kwargs)

    def get(self, serial: str) -> Hardware:
        return HardwareService.get(serial)

    def patch(self, serial: str, **kwargs) -> Hardware:
        return HardwareService.patch_hardware(serial, **kwargs)

    def delete(self, serial: str) -> None:
        hw = HardwareService.get(serial)
        if hw:
            HardwareService.delete_hardware(hw)

    def list_all(self) -> list[Hardware]:
        return HardwareService.list_all()
