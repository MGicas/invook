from ...domain.resource.Consum import Consum
from ...usecase.GeneralUsecase import GeneralUseCase
from ....crosscutting.exception.impl.BusinessException import ConsumNotFoundException, MissingFieldException
from ....crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from ....services.resource.ConsumService import ConsumService


class ConsumUseCase():
    
    def __init__(self):
        self.service = ConsumService()

    def create(self, id_lender: str, id_monitor: str, supplies: list) -> Consum:       
        try:
            return self.service.create_consum(id_lender, id_monitor, supplies)
        except DatabaseOperationException:
            raise  
    
    def get(self, id: str) -> Consum:
        consum = ConsumService.get(id)
        if not consum:
            raise ConsumNotFoundException(id)
        return consum
    
    def patch(self, id: str, **kwargs) -> Consum:
        Consum = ConsumService.get(id)
        if not Consum:
            raise ConsumNotFoundException(id)
        return ConsumService.patch_consum(id, **kwargs)
    
    def update(self, id: str, **kwargs) -> Consum:
        consum = ConsumService.get(id)
        if not consum:
            raise ConsumNotFoundException(id)
        return ConsumService.update_consum(consum, **kwargs)
    
    def list_all(self) -> list[Consum]:
        return ConsumService.list_all()