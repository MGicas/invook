from abc import ABC, abstractmethod

class IDeleteAdministrativeUserUseCase(ABC):
    @abstractmethod
    def execute(self, username: str) -> None:
        pass
