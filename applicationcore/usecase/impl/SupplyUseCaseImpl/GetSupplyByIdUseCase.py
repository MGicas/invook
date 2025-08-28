from typing import Optional
from co.edu.uco.invook.applicationcore.domain.inventory.Supply import Supply
from co.edu.uco.invook.applicationcore.usecase.supply.IGetSupplyByIdUseCase import IGetSupplyByIdUseCase
from co.edu.uco.invook.infrastructure.data.impl.SupplyRepository import SupplyRepository


class GetSupplyByIdUseCase(IGetSupplyByIdUseCase):
    def __init__(self, repository: SupplyRepository):
        self._repository = repository

    def execute(self, supply_id: str) -> Optional[Supply]:
        return self._repository.find_by_id(supply_id)
