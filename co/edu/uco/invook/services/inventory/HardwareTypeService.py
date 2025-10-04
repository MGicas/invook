from ...applicationcore.domain.inventory.HardwareType import HardwareType
from ...crosscutting.exception.impl.BusinessException import BusinessException

class HardwareTypeService:

    def create_hardware_type(self, **kwargs) -> HardwareType:
        try:
            return HardwareType.objects.create(**kwargs)
        except Exception as e:
            raise BusinessException(f"Error creating HardwareType: {str(e)}")

    def get(self, id: str) -> HardwareType:
        try:
            return HardwareType.objects.get(pk=id)
        except HardwareType.DoesNotExist:
            raise BusinessException(f"HardwareType with id {id} not found")

    def patch_hardware_type(self, id: str, **kwargs) -> HardwareType:
        hardware_type = self.get(id)
        for field, value in kwargs.items():
            setattr(hardware_type, field, value)
        hardware_type.save()
        return hardware_type

    def delete_hardware_type(self, id: str):
        hardware_type = self.get(id)
        hardware_type.delete()

    def list_all(self) -> list[HardwareType]:
        return list(HardwareType.objects.all())
    
    def search_by_name(self, name: str):
        return list(HardwareType.objects.filter(name__icontains=name))
    
    def deactivate(self, id: str):
        hardware_type = self.get(id)
        hardware_type.active = False
        hardware_type.save()
        return hardware_type
