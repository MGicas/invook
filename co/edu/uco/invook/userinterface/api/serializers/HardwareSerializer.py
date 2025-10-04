from rest_framework import serializers
from ....applicationcore.domain.inventory.Hardware import Hardware
from ....applicationcore.domain.inventory.HardwareType import HardwareType

class HardwareSerializer(serializers.Serializer):
    serial = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=500)
    comment = serializers.CharField(max_length=300, allow_blank=True, required=False)
    hardware_type = serializers.CharField(max_length=100)
    state = serializers.CharField()
    available = serializers.CharField()
    hardware_type_name = serializers.CharField(source="hardware_type.name", read_only=True)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["hardware_type"] = instance.hardware_type.name  # muestra el nombre, no el id
        return rep
