from co.edu.uco.invook.infrastructure.data.impl.LenderRepository import LenderRepository
from co.edu.uco.invook.applicationcore.usecase.lender.IDeleteLenderUseCase import IDeleteLenderUseCase

class DeleteLenderUseCase(IDeleteLenderUseCase):
    def __init__(self, repository: LenderRepository):
        self._repository = repository

    def execute(self, lender_id: str) -> None:
        self._repository.delete(lender_id)
