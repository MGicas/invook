from abc import ABC, abstractmethod
from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.resource.Consum import Consum


class ConsumRepository(ABC):

    @abstractmethod
    def find_all(self) -> List[Consum]:
        pass

    @abstractmethod
    def save(self, consum: Consum) -> None:
        pass

    @abstractmethod
    def find_by_id(self, consum_id: str) -> Optional[Consum]:
        pass

    @abstractmethod
    def delete(self, consum_id: str) -> None:
        pass
