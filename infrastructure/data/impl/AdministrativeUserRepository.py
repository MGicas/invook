from abc import ABC, abstractmethod
from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.user.AdministrativeUser import AdministrativeUser

class AdministrativeUserRepository(ABC):

    @abstractmethod
    def find_all(self) -> List[AdministrativeUser]:
        pass

    @abstractmethod
    def save(self, user: AdministrativeUser) -> None:
        pass

    @abstractmethod
    def find_by_username(self, username: str) -> Optional[AdministrativeUser]:
        pass

    @abstractmethod
    def delete(self, username: str) -> None:
        pass
