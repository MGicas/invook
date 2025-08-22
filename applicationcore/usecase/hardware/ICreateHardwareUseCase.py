from abc import ABC, abstractmethod
from co.edu.uco.invook.applicationcore.domain.inventory.Hardware import Hardware

class ICreateHardwareUseCase(ABC):
    @abstractmethod
    def execute(self, hardware: Hardware) -> None:
        pass
