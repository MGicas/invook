from co.edu.uco.invook.applicationcore.domain.inventory.Supply import Supply
from co.edu.uco.invook.applicationcore.usecase.GeneralUsecase import GeneralUseCase
from co.edu.uco.invook.services.inventory.SupplyService import SupplyService

class SupplyUseCase(GeneralUseCase):
    
    def create(self, **kwargs) -> Supply:
        return SupplyService.create_supply(**kwargs)

    def get(self, code: str) -> Supply:
        return SupplyService.get(code)

    def patch(self, code: str, **kwargs) -> Supply:
        return SupplyService.patch_hardware(code, **kwargs)

    def delete(self, code: str) -> None:
        supply = SupplyService.get(code)
        if supply:
            SupplyService.delete_supply(supply)

    def list_all(self) -> list[Supply]:
        return SupplyService.list_all()
    