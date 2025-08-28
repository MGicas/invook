from abc import ABC, abstractmethod
from typing import Optional
from co.edu.uco.invook.applicationcore.domain.user.Lender import Lender

class IGetLenderByIdUseCase(ABC):
    @abstractmethod
    def execute(self, lender_id: str) -> Optional[Lender]:
        pass
