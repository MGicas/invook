from typing import Optional
from ...crosscutting.util.UtilPatch import UtilPatch
from django.db import IntegrityError, DatabaseError
from ...crosscutting.exception.impl.BusinessException import DuplicateSupplyCodeException, SupplyNotFoundException
from ...crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from ...crosscutting.util import UtilNumber, UtilText
from ...applicationcore.domain.inventory.Supply import Supply

class SupplyService:

    @staticmethod
    def create_supply(code, name, description, supply_type, count, quantity):
        try:
            supply = Supply(
                code = code,
                name = name,
                description = description,
                supply_type = supply_type,
                count = count,
                quantity = quantity
            )
            
            supply.save()
            return supply
        except IntegrityError as e:
            raise DuplicateSupplyCodeException(code) from e
        except DatabaseError as e:
            raise DatabaseOperationException("Error al crear supply en la base de datos") from e


    @staticmethod
    def get(code: str) -> Optional[Supply]:
        try:
            return Supply.objects.get(code = code)
        except Supply.DoesNotExist:
            return None
        except DatabaseError as e:
            raise DatabaseOperationException("Error al consultar supply en la base de datos") from e

    @staticmethod
    def patch_supply(code: str, **kwargs) -> Supply:
        try:
            supply = Supply.objects.get(code = code)
        except Supply.DoesNotExist:
            raise SupplyNotFoundException(code)
        except DatabaseError as e:
            raise DatabaseOperationException("Error al actualizar supply en la base de datos") from e
        return UtilPatch.patch_model(supply, kwargs)

    @staticmethod
    def update_supply(supply: Supply, **kwargs) -> Supply:
        try:
            for key, value in kwargs.items():
                if hasattr(supply, key):
                    if isinstance(value, str):
                        value = UtilText.apply_trim(value)
                    elif isinstance(value, int):
                        value = UtilNumber.ensure_positive(value)
                    setattr(supply, key, value)
            supply.save()
            return supply
        except DatabaseError as e:
            raise DatabaseOperationException("Error al actualizar supply en la base de datos") from e

    
    @staticmethod
    def delete_supply(supply: Supply) -> None:
        try:
            supply.delete()
        except DatabaseError as e:
            raise DatabaseOperationException("Error al eliminar supply en la base de datos") from e
        
    @staticmethod
    def list_all() -> list[Supply]:
        try:
            return list(Supply.objects.all())
        except DatabaseError as e:
            raise DatabaseOperationException("Error al listar supply en la base de datos") from e
    
    @staticmethod
    def restock_supply(supply: Supply, additional_count: int) -> Supply:
        try:
            additional_count = UtilNumber.ensure_positive(additional_count)
            supply.count += additional_count
            supply.stock = supply.count * supply.quantity
            supply.save()
            return supply
        except DatabaseError as e:
            raise DatabaseOperationException("Error al reabastecer supply en la base de datos") from e
