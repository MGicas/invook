from abc import ABC, abstractmethod
from co.edu.uco.invook.applicationcore.domain.user.User import User

class ICreateUserUseCase(ABC):
    @abstractmethod
    def execute(self, user: User) -> None:
        pass
