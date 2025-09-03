from typing import Optional
from UtilPatch import UtilPatch
from UtilText import UtilText
from co.edu.uco.invook.applicationcore.domain.user.Lender import Lender

class LenderService:
    
    @staticmethod
    def create_lender(rfid, names, surnames, email, phone, state):
        lender = Lender.objects.create(
            rfid = rfid,
            names = names,
            surnames = surnames,
            email = email,
            phone = phone,
            state = state
        )

        lender.save()
        return lender
    
    @staticmethod
    def get(rfid: str) -> Optional[Lender]:
        try:
            return Lender.objects.get(rfid = rfid)
        except Lender.DoesNotExist:
            return None
        
    @staticmethod
    def update_lender(lender: Lender, **kwargs) -> Lender:
        for key, value in kwargs.items():
            if hasattr(lender, key):
                if isinstance(value, str):
                    value = UtilText.apply_trim(value)
                setattr(lender, key, value)
        lender.save()
        return lender
    
    @staticmethod
    def delete_lender(lender: Lender) -> None:
        lender.delete()
        
    @staticmethod
    def list_all() -> list[Lender]:
        return list(Lender.objects.all())
    
    @staticmethod
    def patch_lender(rfid: str, **kwargs) -> Lender:
        try:
            lender = Lender.objects.get(rfid = rfid)
        except Lender.DoesNotExist:
            raise ValueError(f"Lender con rfid '{rfid}' no existe.")
        return UtilPatch.patch_model(lender, kwargs)