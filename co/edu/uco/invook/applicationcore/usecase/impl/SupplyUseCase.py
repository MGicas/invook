from ...domain.inventory.Supply import Supply
from ...usecase.GeneralUsecase import GeneralUseCase
from ....crosscutting.exception.impl.BusinessException import DuplicateSupplyCodeException, MissingFieldException, SupplyNotFoundException
from ....crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from ....services.inventory.SupplyService import SupplyService

class SupplyUseCase(GeneralUseCase):
    service = SupplyService()
    
    def create(self, **kwargs) -> Supply:
        return self.service.create_supply(**kwargs)
    
    def get(self, code: str) -> Supply:
        return self.service.get(code)

    def patch(self, code: str, **kwargs) -> Supply:
        return self.service.patch_supply(code, **kwargs)

    def delete(self, code: str) -> None:
        self.service.delete_supply(code)

    def list_all(self) -> list[Supply]:
        return self.service.list_all()
    
    def restock(self, code: str, count: int, quantity: int) -> Supply:
        return self.service.restock_supply(code, count, quantity)
    