from abc import ABC, abstractmethod
from typing import List
from co.edu.uco.invook.applicationcore.domain.user.User import User

class IGetAllUsersUseCase(ABC):
    @abstractmethod
    def execute(self) -> List[User]:
        pass
