from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.resource.Consum import Consum
from co.edu.uco.invook.applicationcore.usecase.consum.ICreateConsumUseCase import ICreateConsumUseCase
from co.edu.uco.invook.applicationcore.usecase.consum.IGetAllConsumsUseCase import IGetAllConsumsUseCase
from co.edu.uco.invook.applicationcore.usecase.consum.IGetConsumByIdUseCase import IGetConsumByIdUseCase
from co.edu.uco.invook.applicationcore.usecase.consum.IDeleteConsumUseCase import IDeleteConsumUseCase

class ConsumFacade:
    def __init__(
        self,
        create_consum_uc: ICreateConsumUseCase,
        get_all_consums_uc: IGetAllConsumsUseCase,
        get_consum_by_id_uc: IGetConsumByIdUseCase,
        delete_consum_uc: IDeleteConsumUseCase
    ):
        self._create_consum_uc = create_consum_uc
        self._get_all_consums_uc = get_all_consums_uc
        self._get_consum_by_id_uc = get_consum_by_id_uc
        self._delete_consum_uc = delete_consum_uc

    def create_consum(self, consum: Consum) -> None:
        self._create_consum_uc.execute(consum)

    def get_all_consums(self) -> List[Consum]:
        return self._get_all_consums_uc.execute()

    def get_consum_by_id(self, consum_id: str) -> Optional[Consum]:
        return self._get_consum_by_id_uc.execute(consum_id)

    def delete_consum(self, consum_id: str) -> None:
        self._delete_consum_uc.execute(consum_id)
