from abc import ABC, abstractmethod

class IDeleteHardwareUseCase(ABC):
    @abstractmethod
    def execute(self, serial: str) -> None:
        pass
