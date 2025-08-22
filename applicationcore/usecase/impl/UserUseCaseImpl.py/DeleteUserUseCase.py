from co.edu.uco.invook.infrastructure.data.impl.UserRepository import UserRepository
from co.edu.uco.invook.applicationcore.usecase.user.IDeleteUserUseCase import IDeleteUserUseCase

class DeleteUserUseCase(IDeleteUserUseCase):
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, id: str) -> None:
        self.repository.delete(id)
