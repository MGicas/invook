from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.user.Lender import Lender
from co.edu.uco.invook.applicationcore.usecase.lender.ICreateLenderUseCase import ICreateLenderUseCase
from co.edu.uco.invook.applicationcore.usecase.lender.IGetAllLendersUseCase import IGetAllLendersUseCase
from co.edu.uco.invook.applicationcore.usecase.lender.IGetLenderByIdUseCase import IGetLenderByIdUseCase
from co.edu.uco.invook.applicationcore.usecase.lender.IDeleteLenderUseCase import IDeleteLenderUseCase

class LenderFacade:
    def __init__(
        self,
        create_uc: ICreateLenderUseCase,
        get_all_uc: IGetAllLendersUseCase,
        get_by_id_uc: IGetLenderByIdUseCase,
        delete_uc: IDeleteLenderUseCase
    ):
        self._create_uc = create_uc
        self._get_all_uc = get_all_uc
        self._get_by_id_uc = get_by_id_uc
        self._delete_uc = delete_uc

    def create_lender(self, lender: Lender) -> None:
        self._create_uc.execute(lender)

    def get_all_lenders(self) -> List[Lender]:
        return self._get_all_uc.execute()

    def get_lender_by_id(self, lender_id: str) -> Optional[Lender]:
        return self._get_by_id_uc.execute(lender_id)

    def delete_lender(self, lender_id: str) -> None:
        self._delete_uc.execute(lender_id)
