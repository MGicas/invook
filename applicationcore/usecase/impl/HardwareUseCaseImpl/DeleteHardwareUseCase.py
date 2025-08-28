from co.edu.uco.invook.applicationcore.usecase.hardware.IDeleteHardwareUseCase import IDeleteHardwareUseCase
from co.edu.uco.invook.infrastructure.data.impl.HardwareRepository import IHardwareRepository

class DeleteHardwareUseCase(IDeleteHardwareUseCase):
    def __init__(self, repository: IHardwareRepository):
        self._repository = repository

    def execute(self, serial: str) -> None:
        self._repository.delete(serial)
