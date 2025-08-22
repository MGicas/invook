from abc import ABC, abstractmethod
from typing import Optional
from co.edu.uco.invook.applicationcore.domain.user.User import User

class IGetUserByIdUseCase(ABC):
    @abstractmethod
    def execute(self, id: str) -> Optional[User]:
        pass
