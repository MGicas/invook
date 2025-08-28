from co.edu.uco.invook.infrastructure.data.impl.LenderRepository import LenderRepository
from co.edu.uco.invook.applicationcore.domain.user.Lender import Lender
from typing import List
from co.edu.uco.invook.applicationcore.usecase.lender.IGetAllLendersUseCase import IGetAllLendersUseCase

class GetAllLendersUseCase(IGetAllLendersUseCase):
    def __init__(self, repository: LenderRepository):
        self._repository = repository

    def execute(self) -> List[Lender]:
        return self._repository.find_all()
