from abc import ABC, abstractmethod
from typing import List
from co.edu.uco.invook.applicationcore.domain.resource.Consum import Consum

class IGetAllConsumsUseCase(ABC):
    @abstractmethod
    def execute(self) -> List[Consum]:
        pass
