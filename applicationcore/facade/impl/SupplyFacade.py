from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.inventory.Supply import Supply
from co.edu.uco.invook.applicationcore.usecase.supply.ICreateSupplyUseCase import ICreateSupplyUseCase
from co.edu.uco.invook.applicationcore.usecase.supply.IGetAllSuppliesUseCase import IGetAllSuppliesUseCase
from co.edu.uco.invook.applicationcore.usecase.supply.IGetSupplyByIdUseCase import IGetSupplyByIdUseCase
from co.edu.uco.invook.applicationcore.usecase.supply.IDeleteSupplyUseCase import IDeleteSupplyUseCase

class SupplyFacade:
    def __init__(
        self,
        create_supply_uc: ICreateSupplyUseCase,
        get_all_supplies_uc: IGetAllSuppliesUseCase,
        get_supply_by_id_uc: IGetSupplyByIdUseCase,
        delete_supply_uc: IDeleteSupplyUseCase
    ):
        self._create_supply_uc = create_supply_uc
        self._get_all_supplies_uc = get_all_supplies_uc
        self._get_supply_by_id_uc = get_supply_by_id_uc
        self._delete_supply_uc = delete_supply_uc

    def create_supply(self, supply: Supply) -> None:
        self._create_supply_uc.execute(supply)

    def get_all_supplies(self) -> List[Supply]:
        return self._get_all_supplies_uc.execute()

    def get_supply_by_id(self, supply_id: str) -> Optional[Supply]:
        return self._get_supply_by_id_uc.execute(supply_id)

    def delete_supply(self, supply_id: str) -> None:
        self._delete_supply_uc.execute(supply_id)
