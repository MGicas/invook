from co.edu.uco.invook.infrastructure.data.impl.AdministrativeUserRepository import AdministrativeUserRepository
from co.edu.uco.invook.applicationcore.domain.user.AdministrativeUser import AdministrativeUser
from co.edu.uco.invook.applicationcore.usecase.administrativeUser.ICreateAdministrativeUserUseCase import ICreateAdministrativeUserUseCase

class CreateAdministrativeUserUseCase(ICreateAdministrativeUserUseCase):
    def __init__(self, repository: AdministrativeUserRepository):
        self._repository = repository

    def execute(self, user: AdministrativeUser) -> None:
        self._repository.save(user)
