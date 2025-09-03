from typing import Optional
from UtilPatch import UtilPatch
from co.edu.uco.invook.crosscutting.util import UtilNumber, UtilText
from co.edu.uco.invook.applicationcore.domain.inventory.Supply import Supply

class SupplyService:

    @staticmethod
    def create_supply(code, name, description, supply_type, count, quantity):
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

    @staticmethod
    def get(code: str) -> Optional[Supply]:
        try:
            return Supply.objects.get(code = code)
        except Supply.DoesNotExist:
            return None

    @staticmethod
    def patch_hardware(code: str, **kwargs) -> Supply:
        try:
            supply = Supply.objects.get(code = code)
        except Supply.DoesNotExist:
            raise ValueError(f"Supply con codigo '{code}' no existe.")
        return UtilPatch.patch_model(supply, kwargs)

    @staticmethod
    def update_supply(supply: Supply, **kwargs) -> Supply:
        for key, value in kwargs.items():
            if hasattr(supply, key):
                if isinstance(value, str):
                    value = UtilText.apply_trim(value)
                elif isinstance(value, int):
                    value = UtilNumber.ensure_positive(value)
                setattr(supply, key, value)
        supply.save()
        return supply
    
    @staticmethod
    def delete_supply(supply: Supply) -> None:
        supply.delete()
        
    @staticmethod
    def list_all() -> list[Supply]:
        return list(Supply.objects.all())
    
    @staticmethod
    def restock_supply(supply: Supply, additional_count: int) -> Supply:
        additional_count = UtilNumber.ensure_positive(additional_count)
        supply.count += additional_count
        supply.stock = supply.count * supply.quantity
        supply.save()
        return supply
