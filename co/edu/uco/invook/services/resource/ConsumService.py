
from typing import Optional
from django.db import transaction
from django.core.exceptions import ValidationError
from ...crosscutting.exception.impl.BusinessException import ConsumNotFoundException, AdministrativeUserNotFoundException, LenderNotFoundException, SupplyNotFoundException
from ...crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from ...crosscutting.util.UtilNumber import UtilNumber
from ...crosscutting.util.UtilText import UtilText
from ...crosscutting.util.UtilPatch import UtilPatch
from ...applicationcore.domain.resource.Consum import Consum
from ...applicationcore.domain.inventory.Supply import Supply
from ...applicationcore.domain.resource.ConsumSupply import ConsumSupply
from ...applicationcore.domain.user.Lender import Lender
from ...applicationcore.domain.user.AdministrativeUser import AdministrativeUser
from ...services.inventory.SupplyService import SupplyService


class ConsumService:

    @staticmethod
    def _attach_supply(consum: Consum, supply: Supply, quantity: int) -> ConsumSupply:
        print(f"Creating ConsumSupply with quantity: {quantity}")
        if quantity is None or quantity <= 0:
            raise ValueError("La cantidad no puede ser nula o negativa.")
        consum_supply = ConsumSupply.objects.create(
            consum=consum,
            supply=supply,
            quantity=quantity
        )
        return consum_supply
    
    @staticmethod
    def create_consum(id_lender, id_monitor, supplies_data):
        try:
            with transaction.atomic():
                lender = Lender.objects.get(id=id_lender)
                monitor = AdministrativeUser.objects.get(id=id_monitor)

                consum = Consum.objects.create(
                    id_lender=lender,
                    id_monitor=monitor
                )

                for item in supplies_data:
                    supply_code= item['supply_code']

                    if isinstance(supply_code, dict):
                        supply_code = supply_code.get("code")

                    quantity = item['quantity']

                    try:
                        supply = Supply.objects.get(code=supply_code)
                    except Supply.DoesNotExist:
                        raise SupplyNotFoundException(f"Producto con ID {supply_code} no existe")

                    if supply.stock < quantity:
                        raise ValidationError(f"No hay suficiente stock para Supply con {supply_code}")
                    
                    supply.stock -= quantity
                    supply.save()

                    ConsumSupply.objects.create(
                        consum = consum,
                        supply = supply,
                        quantity=quantity
                    )
                    
                return consum
        except Lender.DoesNotExist:
            raise LenderNotFoundException(f"Lender con id {id_lender} no encontrado.")
        except AdministrativeUser.DoesNotExist:
            raise AdministrativeUserNotFoundException(f"Monitor con id {id_monitor} no encontrado.")
        except Supply.DoesNotExist:
            raise ValueError("Uno de los supplies con los seriales proporcionados no existe.")

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