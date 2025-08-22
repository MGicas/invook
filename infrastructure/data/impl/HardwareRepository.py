from abc import ABC, abstractmethod
from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.inventory.Hardware import Hardware


class HardwareRepository(ABC):

    @abstractmethod
    def find_all(self) -> List[Hardware]:
        pass

    @abstractmethod
    def save(self, hardware: Hardware) -> None:
        pass

    @abstractmethod
    def find_by_serial(self, serial: str) -> Optional[Hardware]:
        pass

    @abstractmethod
    def delete(self, serial: str) -> None:
        pass
