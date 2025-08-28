from typing import List
from co.edu.uco.invook.applicationcore.domain.inventory.Supply import Supply
from co.edu.uco.invook.applicationcore.usecase.supply.IGetAllSuppliesUseCase import IGetAllSuppliesUseCase
from co.edu.uco.invook.infrastructure.data.impl.SupplyRepository import SupplyRepository

class GetAllSuppliesUseCase(IGetAllSuppliesUseCase):
    def __init__(self, repository: SupplyRepository):
        self._repository = repository

    def execute(self) -> List[Supply]:
        return self._repository.find_all()
