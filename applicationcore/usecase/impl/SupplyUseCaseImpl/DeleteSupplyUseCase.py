from co.edu.uco.invook.applicationcore.usecase.supply.IDeleteSupplyUseCase import IDeleteSupplyUseCase
from co.edu.uco.invook.infrastructure.data.impl.SupplyRepository import SupplyRepository

class DeleteSupplyUseCase(IDeleteSupplyUseCase):
    def __init__(self, repository: SupplyRepository):
        self._repository = repository

    def execute(self, supply_id: str) -> None:
        self._repository.delete(supply_id)
