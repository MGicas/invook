from co.edu.uco.invook.applicationcore.domain.resource.Consum import Consum
from co.edu.uco.invook.applicationcore.usecase.consum.ICreateConsumUseCase import ICreateConsumUseCase
from co.edu.uco.invook.infrastructure.data.impl.ConsumRepository import ConsumRepository

class CreateConsumUseCase(ICreateConsumUseCase):
    def __init__(self, repository: ConsumRepository):
        self._repository = repository

    def execute(self, consum: Consum) -> None:
        self._repository.save(consum)
