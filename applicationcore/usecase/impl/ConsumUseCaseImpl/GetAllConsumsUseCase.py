from typing import List
from co.edu.uco.invook.applicationcore.domain.resource.Consum import Consum
from co.edu.uco.invook.applicationcore.usecase.consum.IGetAllConsumsUseCase import IGetAllConsumsUseCase
from co.edu.uco.invook.infrastructure.data.impl.ConsumRepository import ConsumRepository

class GetAllConsumsUseCase(IGetAllConsumsUseCase):
    def __init__(self, repository: ConsumRepository):
        self._repository = repository

    def execute(self) -> List[Consum]:
        return self._repository.find_all()
