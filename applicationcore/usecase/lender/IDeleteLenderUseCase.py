from abc import ABC, abstractmethod

class IDeleteLenderUseCase(ABC):
    @abstractmethod
    def execute(self, lender_id: str) -> None:
        pass
