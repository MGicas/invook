from co.edu.uco.invook.applicationcore.domain.inventory.Hardware import Hardware
from co.edu.uco.invook.applicationcore.usecase.hardware.ICreateHardwareUseCase import ICreateHardwareUseCase
from co.edu.uco.invook.infrastructure.data.impl.HardwareRepository import HardwareRepository

class CreateHardwareUseCase(ICreateHardwareUseCase):
    def __init__(self, repository: HardwareRepository):
        self._repository = repository

    def execute(self, hardware: Hardware) -> None:
        self._repository.save(hardware)
