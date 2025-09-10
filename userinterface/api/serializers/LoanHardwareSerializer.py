from co.edu.uco.invook.applicationcore.domain.resource import LoanHardware
from .HardwareSerializer import HardwareSerializer
from co.edu.uco.invook.userinterface.api.serializers.HardwareSerializer import HardwareSerializer
from rest_framework import serializers

class LoanHardwareSerializer(serializers.ModelSerializer):
    hardware = HardwareSerializer()
    class Meta:
        model = LoanHardware
        fields = ['hardware']