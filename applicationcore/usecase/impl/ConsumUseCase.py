from co.edu.uco.invook.applicationcore.domain.resource.Consum import Consum
from co.edu.uco.invook.applicationcore.usecase.GeneralUsecase import GeneralUseCase
from co.edu.uco.invook.services.resource.ConsumService import ConsumService


class ConsumUseCase(GeneralUseCase):
    def create(self, **kwargs) -> Consum:
        return ConsumService.create_consum(**kwargs)
    
    def get(self, id: int) -> Consum:
        return ConsumService.get(id)
    
    def patch(self, id: int, **kwargs) -> Consum:
        return ConsumService.patch_consum(id, **kwargs)
    
    def update(self, id: int, **kwargs) -> Consum:
        return ConsumService.update_consum(self.get(id), **kwargs)
    
    def list_all(self) -> list[Consum]:
        return ConsumService.list_all()