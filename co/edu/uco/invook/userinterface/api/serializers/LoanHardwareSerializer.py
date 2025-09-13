from ....applicationcore.domain.resource import LoanHardware
from .HardwareSerializer import HardwareSerializer
from .HardwareSerializer import HardwareSerializer
from rest_framework import serializers

class LoanHardwareSerializer(serializers.ModelSerializer):
    hardware = HardwareSerializer()
    class Meta:
        model = LoanHardware
        fields = ['hardware']