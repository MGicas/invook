from abc import ABC, abstractmethod
from co.edu.uco.invook.applicationcore.domain.user.Lender import Lender

class ICreateLenderUseCase(ABC):
    @abstractmethod
    def execute(self, lender: Lender) -> None:
        pass
