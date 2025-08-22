from abc import ABC, abstractmethod
from typing import List
from co.edu.uco.invook.applicationcore.domain.inventory.Hardware import Hardware

class IGetAllHardwareUseCase(ABC):
    @abstractmethod
    def execute(self) -> List[Hardware]:
        pass
