from co.edu.uco.invook.applicationcore.domain.inventory.Supply import Supply
from co.edu.uco.invook.applicationcore.usecase.supply.ICreateSupplyUseCase import ICreateSupplyUseCase
from co.edu.uco.invook.infrastructure.data.impl.SupplyRepository import SupplyRepository

class CreateSupplyUseCase(ICreateSupplyUseCase):
    def __init__(self, repository: SupplyRepository):
        self._repository = repository

    def execute(self, supply: Supply) -> None:
        self._repository.save(supply)
