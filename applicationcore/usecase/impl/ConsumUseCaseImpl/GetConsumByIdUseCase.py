from typing import Optional
from co.edu.uco.invook.applicationcore.domain.resource.Consum import Consum
from co.edu.uco.invook.applicationcore.usecase.consum.IGetConsumByIdUseCase import IGetConsumByIdUseCase
from co.edu.uco.invook.infrastructure.data.impl.ConsumRepository import ConsumRepository

class GetConsumByIdUseCase(IGetConsumByIdUseCase):
    def __init__(self, repository: ConsumRepository):
        self._repository = repository

    def execute(self, consum_id: str) -> Optional[Consum]:
        return self._repository.find_by_id(consum_id)
