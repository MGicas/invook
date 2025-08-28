from abc import ABC, abstractmethod
from typing import List
from co.edu.uco.invook.applicationcore.domain.user.AdministrativeUser import AdministrativeUser

class IGetAllAdministrativeUsersUseCase(ABC):
    @abstractmethod
    def execute(self) -> List[AdministrativeUser]:
        pass
