from django.core.exceptions import ObjectDoesNotExist
from ...applicationcore.domain.inventory.SupplyType import SupplyType
from ....crosscutting.exception.impl.BusinessException import (
    BusinessException,
    DuplicateSerialException,
    HardwareNotFoundException
)
from ....crosscutting.util.UtilText import UtilText

class SupplyTypeService:

    def create_supply_type(self, **kwargs) -> SupplyType:
        try:
            id = UtilText.apply_trim(kwargs.get("id"))
            name = UtilText.apply_trim(kwargs.get("name"))
            description = UtilText.apply_trim(kwargs.get("description"))

            if SupplyType.objects.filter(name__iexact=name).exists():
                raise BusinessException(f"Ya existe un tipo de insumo con el nombre '{name}'")

            supply_type = SupplyType.objects.create(
                id=id,
                name=name,
                description=description,
                active=True
            )
            return supply_type
        except Exception as e:
            raise BusinessException(f"Error creando SupplyType: {str(e)}")

    def get(self, identifier: str) -> SupplyType:
        try:
            return SupplyType.objects.get(pk=identifier)
        except ObjectDoesNotExist:
            raise BusinessException(f"SupplyType con id {identifier} no existe")

    def patch_supply_type(self, identifier: str, **kwargs) -> SupplyType:
        try:
            supply_type = SupplyType.objects.get(pk=identifier)
            for field, value in kwargs.items():
                if hasattr(supply_type, field):
                    setattr(supply_type, field, UtilText.apply_trim(value))
                else:
                    raise BusinessException(f"Campo inválido para actualizar: {field}")
            supply_type.save()
            return supply_type
        except ObjectDoesNotExist:
            raise BusinessException(f"SupplyType con id {identifier} no existe")

    def list_all(self) -> list[SupplyType]:
        return SupplyType.objects.all()

    def search_by_name(self, name: str) -> list[SupplyType]:
        return SupplyType.objects.filter(name__icontains=name)

    def deactivate(self, identifier: str) -> SupplyType:
        try:
            supply_type = SupplyType.objects.get(pk=identifier)
            supply_type.active = False
            supply_type.save()
            return supply_type
        except ObjectDoesNotExist:
            raise BusinessException(f"SupplyType con id {identifier} no existe")
