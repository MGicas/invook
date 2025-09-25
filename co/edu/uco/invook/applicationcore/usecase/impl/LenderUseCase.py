from ...domain.user.Lender import Lender
from ...usecase.GeneralUsecase import GeneralUseCase
from ....services.user.LenderService import LenderService
from ....crosscutting.exception.impl.BusinessException import LenderNotFoundException        
class LenderUseCase(GeneralUseCase):
    service = LenderService()
    
    def create(self, **kwargs) -> Lender:
        return LenderService.create_lender(**kwargs)

    def get(self, id: str) -> Lender:
        return LenderService.get(id)

    def patch(self, id: str, **kwargs) -> Lender:
        return LenderService.patch_lender(id, **kwargs)

    def delete(self, id: str) -> None:
        lender = self.service.get(id)
        if not lender:
            raise LenderNotFoundException(id) 
            
        self.service.delete_lender(lender)

    def list_all(self) -> list[Lender]:
        return LenderService.list_all()