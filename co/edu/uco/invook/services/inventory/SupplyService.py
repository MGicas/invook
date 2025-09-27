from typing import Optional
from ...crosscutting.util.UtilPatch import UtilPatch
from django.db import IntegrityError, DatabaseError
from ...crosscutting.exception.impl.BusinessException import DuplicateSupplyCodeException, SupplyNotFoundException
from ...crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from ...crosscutting.util import UtilNumber, UtilText
from ...applicationcore.domain.inventory.Supply import Supply
from ...applicationcore.domain.inventory.SupplyType import SupplyType


class SupplyService:

    @staticmethod
    def create_supply(code, name, description, supply_type, count, quantity) -> Supply:
        try:
            supply_type_instance = SupplyType.objects.get(id=supply_type)  

            stock = count * quantity
            supply, created = Supply.objects.get_or_create(
                code=code,
                defaults={
                    'name':name,
                    'description':description,
                    'supply_type':supply_type_instance,
                    'count':count,
                    'quantity':quantity,
                    'stock': stock
                } 
            )

            if not created:
                raise DuplicateSupplyCodeException(code)
        
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
        except Supply.DoesNotExist as e:
            raise SupplyNotFoundException(supply)
        except DatabaseError as e:
            raise DatabaseOperationException("Error al eliminar supply en la base de datos") from e
        
    @staticmethod
    def list_all() -> list[Supply]:
        try:
            return list(Supply.objects.all())
        except DatabaseError as e:
            raise DatabaseOperationException("Error al listar supply en la base de datos") from e
    
    @staticmethod
    def list_by_type(supply_type: str) -> list[Supply]:
        try:

            if supply_type.isdigit():
                return list(Supply.objects.filter(supply_type_id=supply_type))

            return list(Supply.objects.filter(supply_type__name=supply_type))
        except DatabaseError as e:
            raise DatabaseOperationException("Error al filtrar supply por tipo en la base de datos") from e
    
    @staticmethod
    def restock_supply(code: str, count: int, quantity: int) -> Supply:
        try:
            supply = SupplyService.get(code=code)
        except Supply.DoesNotExist:
                raise ValueError(f"Consumible con código '{code}' no existe")
        supply.count += count
        supply.quantity += quantity
        supply.stock = supply.count * supply.quantity
        supply.save()
        return supply
        