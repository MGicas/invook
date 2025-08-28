from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.user.AdministrativeUser import AdministrativeUser
from co.edu.uco.invook.applicationcore.usecase.administrativeUser.ICreateAdministrativeUserUseCase import ICreateAdministrativeUserUseCase
from co.edu.uco.invook.applicationcore.usecase.administrativeUser.IGetAllAdministrativeUsersUseCase import IGetAllAdministrativeUsersUseCase
from co.edu.uco.invook.applicationcore.usecase.administrativeUser.IGetAdministrativeUserByUsernameUseCase import IGetAdministrativeUserByUsernameUseCase
from co.edu.uco.invook.applicationcore.usecase.administrativeUser.IDeleteAdministrativeUserUseCase import IDeleteAdministrativeUserUseCase

class AdministrativeUserFacade:
    def __init__(
        self,
        create_uc: ICreateAdministrativeUserUseCase,
        get_all_uc: IGetAllAdministrativeUsersUseCase,
        get_by_username_uc: IGetAdministrativeUserByUsernameUseCase,
        delete_uc: IDeleteAdministrativeUserUseCase
    ):
        self._create_uc = create_uc
        self._get_all_uc = get_all_uc
        self._get_by_username_uc = get_by_username_uc
        self._delete_uc = delete_uc

    def create_user(self, user: AdministrativeUser) -> None:
        self._create_uc.execute(user)

    def get_all_users(self) -> List[AdministrativeUser]:
        return self._get_all_uc.execute()

    def get_user_by_username(self, username: str) -> Optional[AdministrativeUser]:
        return self._get_by_username_uc.execute(username)

    def delete_user(self, username: str) -> None:
        self._delete_uc.execute(username)
