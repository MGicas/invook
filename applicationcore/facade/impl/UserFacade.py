from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.user.User import User
from co.edu.uco.invook.applicationcore.usecase.user.ICreateUserUseCase import ICreateUserUseCase
from co.edu.uco.invook.applicationcore.usecase.user.IGetAllUsersUseCase import IGetAllUsersUseCase
from co.edu.uco.invook.applicationcore.usecase.user.IGetUserByIdUseCase import IGetUserByIdUseCase
from co.edu.uco.invook.applicationcore.usecase.user.IDeleteUserUseCase import IDeleteUserUseCase


class UserFacade:
    def __init__(
        self,
        create_user_uc: ICreateUserUseCase,
        get_all_users_uc: IGetAllUsersUseCase,
        get_user_by_id_uc: IGetUserByIdUseCase,
        delete_user_uc: IDeleteUserUseCase
    ):
        self._create_user_uc = create_user_uc
        self._get_all_users_uc = get_all_users_uc
        self._get_user_by_id_uc = get_user_by_id_uc
        self._delete_user_uc = delete_user_uc

    def create_user(self, user: User) -> None:
        self._create_user_uc.execute(user)

    def get_all_users(self) -> List[User]:
        return self._get_all_users_uc.execute()

    def get_user_by_id(self, id: str) -> Optional[User]:
        return self._get_user_by_id_uc.execute(id)

    def delete_user(self, id: str) -> None:
        self._delete_user_uc.execute(id)
