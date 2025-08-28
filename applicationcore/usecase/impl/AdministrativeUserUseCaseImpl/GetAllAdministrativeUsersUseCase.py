from co.edu.uco.invook.applicationcore.domain.user.AdministrativeUser import AdministrativeUser
from co.edu.uco.invook.infrastructure.data.impl.AdministrativeUserRepository import AdministrativeUserRepository
from co.edu.uco.invook.applicationcore.usecase.administrativeUser.IGetAllAdministrativeUsersUseCase import IGetAllAdministrativeUsersUseCase

from typing import List

class GetAllAdministrativeUsersUseCase(IGetAllAdministrativeUsersUseCase):
    def __init__(self, repository: AdministrativeUserRepository):
        self._repository = repository

    def execute(self) -> List[AdministrativeUser]:
        return self._repository.find_all()
