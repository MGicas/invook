from typing import List
from  co.edu.uco.invook.applicationcore.domain.user.User import User
from co.edu.uco.invook.infrastructure.data.impl.UserRepository import UserRepository
from co.edu.uco.invook.applicationcore.usecase.user.IGetAllUsersUseCase import IGetAllUsersUseCase

class GetAllUsersUseCase(IGetAllUsersUseCase):
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self) -> List[User]:
        return self.repository.find_all()
