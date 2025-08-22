from typing import Optional
from co.edu.uco.invook.applicationcore.domain.inventory.Hardware import Hardware
from co.edu.uco.invook.applicationcore.usecase.hardware.IGetHardwareBySerialUseCase import IGetHardwareBySerialUseCase
from co.edu.uco.invook.infrastructure.data.impl.HardwareRepository import HardwareRepository

class GetHardwareBySerialUseCase(IGetHardwareBySerialUseCase):
    def __init__(self, repository: HardwareRepository):
        self._repository = repository

    def execute(self, serial: str) -> Optional[Hardware]:
        return self._repository.find_by_serial(serial)
