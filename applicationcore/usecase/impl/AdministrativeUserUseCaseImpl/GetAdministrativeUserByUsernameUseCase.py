from typing import Optional
from co.edu.uco.invook.applicationcore.domain.user.AdministrativeUser import AdministrativeUser
from co.edu.uco.invook.applicationcore.usecase.administrativeUser.IGetAdministrativeUserByUsernameUseCase import IGetAdministrativeUserByUsernameUseCase
from co.edu.uco.invook.infrastructure.data.impl.AdministrativeUserRepository import AdministrativeUserRepository

class GetAdministrativeUserByUsernameUseCase(IGetAdministrativeUserByUsernameUseCase):
    def __init__(self, repository: AdministrativeUserRepository):
        self._repository = repository

    def execute(self, username: str) -> Optional[AdministrativeUser]:
        return self._repository.find_by_username(username)
