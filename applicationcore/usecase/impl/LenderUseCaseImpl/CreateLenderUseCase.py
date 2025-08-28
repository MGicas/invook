from co.edu.uco.invook.infrastructure.data.impl.LenderRepository import LenderRepository
from co.edu.uco.invook.applicationcore.domain.user.Lender import Lender
from co.edu.uco.invook.applicationcore.usecase.lender.ICreateLenderUseCase import ICreateLenderUseCase

class CreateLenderUseCase(ICreateLenderUseCase):
    def __init__(self, repository: LenderRepository):
        self._repository = repository

    def execute(self, lender: Lender) -> None:
        self._repository.save(lender)
