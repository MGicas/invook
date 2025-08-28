from abc import ABC, abstractmethod
from co.edu.uco.invook.applicationcore.domain.user.AdministrativeUser import AdministrativeUser

class ICreateAdministrativeUserUseCase(ABC):
    @abstractmethod
    def execute(self, user: AdministrativeUser) -> None:
        pass
