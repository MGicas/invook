from co.edu.uco.invook.applicationcore.usecase.consum.IDeleteConsumUseCase import IDeleteConsumUseCase
from co.edu.uco.invook.infrastructure.data.impl.ConsumRepository import ConsumRepository

class DeleteConsumUseCase(IDeleteConsumUseCase):
    def __init__(self, repository: ConsumRepository):
        self._repository = repository

    def execute(self, consum_id: str) -> None:
        self._repository.delete(consum_id)
