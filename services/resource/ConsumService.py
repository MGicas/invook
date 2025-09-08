from typing import Optional
from co.edu.uco.invook.crosscutting.util import UtilNumber, UtilText, UtilPatch
from co.edu.uco.invook.applicationcore.domain.resource.Consum import Consum

class ConsumService:
    @staticmethod
    def create_consum(self, count, rfidLender, idLender, idMonitor, codeSupply, quantity):
        rfidLender = UtilText.apply_trim(rfidLender)
        idLender = UtilText.apply_trim(idLender)
        idMonitor = UtilText.apply_trim(idMonitor)
        codeSupply = UtilText.apply_trim(codeSupply)
        count = UtilNumber.ensure_positive(count)
        quantity = UtilNumber.ensure_positive(quantity)
        
        consum = Consum.objects.create(
            count = count,
            rfidLender = rfidLender,
            idLender = idLender,
            idMonitor = idMonitor,
            codeSupply = codeSupply,
            quantity = quantity
        )
        return consum
    
    @staticmethod
    def get(id: int) -> Optional[Consum]:
        try:
            return Consum.objects.get(id = id)
        except Consum.DoesNotExist:
            return None
        
    @staticmethod
    def update_consum(consum: Consum, **kwargs) -> Consum:
        for key, value in kwargs.items():
            if hasattr(consum, key):
                if isinstance(value, str):
                    value = UtilText.apply_trim(value)
                elif isinstance(value, int):
                    value = UtilNumber.ensure_positive(value)
                setattr(consum, key, value)
        consum.save()
        return consum   
    
    @staticmethod
    def patch_consum(id: int, **kwargs) -> Consum:
        try:
            consum = Consum.objects.get(id = id)
        except Consum.DoesNotExist:
            raise ValueError(f"Consum con id '{id}' no existe.")
        return UtilPatch.patch_model(consum, kwargs) 
        
    @staticmethod
    def list_all() -> list[Consum]:
        return list(Consum.objects.all())