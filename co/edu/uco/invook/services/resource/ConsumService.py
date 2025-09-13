from typing import Optional
from ...crosscutting.exception.impl.BusinessException import ConsumNotFoundException
from ...crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from ...crosscutting.util import UtilNumber, UtilText, UtilPatch
from ...applicationcore.domain.resource.Consum import Consum

class ConsumService:
    @staticmethod
    def create_consum(self, count, rfidLender, idLender, idMonitor, codeSupply, quantity):
        try:
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
    
        except Exception as e:
            raise DatabaseOperationException("Error al crear el consum en la base de datos.") from e

    
    @staticmethod
    def get(id: int) -> Optional[Consum]:
        try:
            return Consum.objects.get(id = id)
        except Consum.DoesNotExist:
            return None
        except Exception as e:
            raise DatabaseOperationException("Error al consultar el consum en la base de datos.") from e

    @staticmethod
    def update_consum(consum: Consum, **kwargs) -> Consum:
        try:
            for key, value in kwargs.items():
                if hasattr(consum, key):
                    if isinstance(value, str):
                        value = UtilText.apply_trim(value)
                    elif isinstance(value, int):
                        value = UtilNumber.ensure_positive(value)
                    setattr(consum, key, value)
            consum.save()
            return consum   
        except Exception as e:
            raise DatabaseOperationException("Error al actualizar el consum en la base de datos.") from e

    @staticmethod
    def patch_consum(id: int, **kwargs) -> Consum:
        try:
            consum = Consum.objects.get(id = id)
        except Consum.DoesNotExist: 
            raise ConsumNotFoundException(id)    
        except Exception as e:
            raise DatabaseOperationException("Error al realizar la actualización en el consum en la base de datos.") from e
        return UtilPatch.patch_model(consum, kwargs) 
        
    @staticmethod
    def list_all() -> list[Consum]:
        try:
            return list(Consum.objects.all())
        except Exception as e:
            raise DatabaseOperationException("Error al listar los consum en la base de datos.") from e