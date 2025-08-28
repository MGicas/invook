from abc import ABC, abstractmethod
from typing import Optional
from co.edu.uco.invook.applicationcore.domain.resource.Consum import Consum

class IGetConsumByIdUseCase(ABC):
    @abstractmethod
    def execute(self, consum_id: str) -> Optional[Consum]:
        pass
