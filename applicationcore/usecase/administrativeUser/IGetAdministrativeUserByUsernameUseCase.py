from abc import ABC, abstractmethod
from typing import Optional
from co.edu.uco.invook.applicationcore.domain.user.AdministrativeUser import AdministrativeUser

class IGetAdministrativeUserByUsernameUseCase(ABC):
    @abstractmethod
    def execute(self, username: str) -> Optional[AdministrativeUser]:
        pass
