from co.edu.uco.invook.applicationcore.domain.user.User import User
from co.edu.uco.invook.infrastructure.data.impl.UserRepository import UserRepository
from co.edu.uco.invook.applicationcore.usecase.user.ICreateUserUseCase import ICreateUserUseCase

class CreateUserUseCase(ICreateUserUseCase):
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, user: User) -> None:
        self.repository.save(user)
