from abc import ABC, abstractmethod
from typing import Optional
from co.edu.uco.invook.applicationcore.domain.inventory.Hardware import Hardware

class IGetHardwareBySerialUseCase(ABC):
    @abstractmethod
    def execute(self, serial: str) -> Optional[Hardware]:
        pass
