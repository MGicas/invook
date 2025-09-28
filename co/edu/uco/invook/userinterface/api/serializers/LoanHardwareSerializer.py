from ....applicationcore.domain.resource.LoanHardware import LoanHardware
from .HardwareSerializer import HardwareSerializer
from rest_framework import serializers

class LoanHardwareSerializer(serializers.ModelSerializer):
    hardware = HardwareSerializer()
    returned_at = serializers.SerializerMethodField()
    return_state = serializers.SerializerMethodField()
    class Meta:
        model = LoanHardware
        fields = ['hardware', 'returned_at', 'return_state']
        
    def get_returned_at(self, obj):
        return obj.returned_at if obj.returned_at else None

    def get_return_state(self, obj):
        return obj.return_state if obj.return_state else None