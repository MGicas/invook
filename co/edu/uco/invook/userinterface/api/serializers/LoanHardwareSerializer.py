from ....applicationcore.domain.resource.LoanHardware import LoanHardware
from .AdministrativeUserSerializer import AdministrativeUserDetailSerializer
from .HardwareSerializer import HardwareSerializer
from rest_framework import serializers

class LoanHardwareSerializer(serializers.ModelSerializer):
    hardware = HardwareSerializer()
    returned_at = serializers.SerializerMethodField()
    return_state = serializers.SerializerMethodField()
    returned_by = AdministrativeUserDetailSerializer(read_only=True)
    
    class Meta:
        model = LoanHardware
        fields = ['hardware', 'returned_at', 'return_state', 'returned_by']
        
    def get_returned_at(self, obj):
        return obj.returned_at if obj.returned_at else None

    def get_return_state(self, obj):
        return obj.return_state if obj.return_state else None