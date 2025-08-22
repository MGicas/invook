from typing import Optional
from co.edu.uco.invook.applicationcore.domain.user.User import User
from co.edu.uco.invook.infrastructure.data.impl.UserRepository import UserRepository
from co.edu.uco.invook.applicationcore.usecase.impl import IGetUserByIdUseCase

class GetUserByIdUseCase(IGetUserByIdUseCase):
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, id: str) -> Optional[User]:
        return self.repository.find_by_id(id)
