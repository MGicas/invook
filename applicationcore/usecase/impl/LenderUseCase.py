from co.edu.uco.invook.applicationcore.domain.user.Lender import Lender
from co.edu.uco.invook.applicationcore.usecase.GeneralUsecase import GeneralUseCase
from co.edu.uco.invook.services.user.LenderService import LenderService
        
class LenderUseCase(GeneralUseCase):
    def create(self, **kwargs) -> Lender:
        return LenderService.create_lender(**kwargs)

    def get(self, rfid: str) -> Lender:
        return LenderService.get(rfid)

    def patch(self, rfid: str, **kwargs) -> Lender:
        return LenderService.patch_lender(rfid, **kwargs)

    def delete(self, rfid: str) -> None:
        lender = LenderService.get(rfid)
        if lender:
            LenderService.delete_lender(lender)

    def list_all(self) -> list[Lender]:
        return LenderService.list_all()