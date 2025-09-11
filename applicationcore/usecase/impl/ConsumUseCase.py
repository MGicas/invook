from co.edu.uco.invook.applicationcore.domain.resource.Consum import Consum
from co.edu.uco.invook.applicationcore.usecase.GeneralUsecase import GeneralUseCase
from co.edu.uco.invook.crosscutting.exception.impl.BusinessException import ConsumNotFoundException, MissingFieldException
from co.edu.uco.invook.crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from co.edu.uco.invook.services.resource.ConsumService import ConsumService


class ConsumUseCase():
    def create(self, **kwargs) -> Consum:
        idLender = kwargs.get("idLender")
        idMonitor = kwargs.get("idMonitor")
        
        if not idLender:
            raise MissingFieldException("idLender")
        if not idMonitor:
            raise MissingFieldException("idMonitor")        
        try:
            return ConsumService.create_consum(**kwargs)
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