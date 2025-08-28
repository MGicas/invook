from co.edu.uco.invook.infrastructure.data.impl.AdministrativeUserRepository import AdministrativeUserRepository
from co.edu.uco.invook.applicationcore.usecase.administrativeUser.IDeleteAdministrativeUserUseCase import IDeleteAdministrativeUserUseCase

class DeleteAdministrativeUserUseCase(IDeleteAdministrativeUserUseCase):
    def __init__(self, repository: AdministrativeUserRepository):
        self._repository = repository

    def execute(self, username: str) -> None:
        self._repository.delete(username)
