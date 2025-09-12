from co.edu.uco.invook.applicationcore.domain.inventory.Supply import Supply
from co.edu.uco.invook.applicationcore.usecase.GeneralUsecase import GeneralUseCase
from co.edu.uco.invook.crosscutting.exception.impl.BusinessException import DuplicateSupplyCodeException, MissingFieldException, SupplyNotFoundException
from co.edu.uco.invook.crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from co.edu.uco.invook.services.inventory.SupplyService import SupplyService

class SupplyUseCase(GeneralUseCase):
    
    def create(self, **kwargs) -> Supply:
        
        code = kwargs.get("code")
        name = kwargs.get("name")
        
        if not code:
            raise MissingFieldException("code")
        if not name:
            raise MissingFieldException("name")
        try:
            return SupplyService.create_supply(**kwargs)
        except DuplicateSupplyCodeException:
            raise
        except DatabaseOperationException:
            raise

    def get(self, code: str) -> Supply:
        supply = SupplyService.get(code)
        if not supply:
            raise SupplyNotFoundException(code)
        return supply

    def patch(self, code: str, **kwargs) -> Supply:
        supply = SupplyService.get(code)
        if not supply:
            raise SupplyNotFoundException(code)

        return SupplyService.patch_supply(code, **kwargs)

    def delete(self, code: str) -> None:
        supply = SupplyService.get(code)
        if not supply:
            raise SupplyNotFoundException(code)

        SupplyService.delete_supply(supply)

    def list_all(self) -> list[Supply]:
        return SupplyService.list_all()
    
    def restock(self, code: str, stock: int) -> Supply:
        supply = SupplyService.get(code)
        if not supply:
            raise SupplyNotFoundException(code)

        return SupplyService.restock_supply(supply, stock)
    