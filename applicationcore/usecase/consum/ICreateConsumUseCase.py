from abc import ABC, abstractmethod
from co.edu.uco.invook.applicationcore.domain.resource.Consum import Consum

class ICreateConsumUseCase(ABC):
    @abstractmethod
    def execute(self, consum: Consum) -> None:
        pass
