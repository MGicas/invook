from typing import List
from co.edu.uco.invook.applicationcore.domain.inventory.Hardware import Hardware
from co.edu.uco.invook.applicationcore.usecase.hardware.IGetAllHardwareUseCase import IGetAllHardwareUseCase
from co.edu.uco.invook.infrastructure.data.impl.HardwareRepository import HardwareRepository

class GetAllHardwareUseCase(IGetAllHardwareUseCase):
    def __init__(self, repository: HardwareRepository):
        self._repository = repository

    def execute(self) -> List[Hardware]:
        return self._repository.find_all()
