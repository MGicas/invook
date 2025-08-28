from typing import Optional
from co.edu.uco.invook.infrastructure.data.impl.LenderRepository import LenderRepository
from co.edu.uco.invook.applicationcore.domain.user.Lender import Lender
from co.edu.uco.invook.applicationcore.usecase.lender.IGetLenderByIdUseCase import IGetLenderByIdUseCase


class GetLenderByIdUseCase(IGetLenderByIdUseCase):
    def __init__(self, repository: LenderRepository):
        self._repository = repository

    def execute(self, lender_id: str) -> Optional[Lender]:
        return self._repository.find_by_id(lender_id)
