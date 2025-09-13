from rest_framework import serializers

from ....applicationcore.domain.resource.Consum import Consum
from .AdministrativeUserSerializer import AdministrativeUserSerializer
from .ConsumSupplySerializer import ConsumSupplySerializer
from .LenderSerializer import LenderSerializer

class ConsumSerializer(serializers.ModelSerializer):
    id_lender = LenderSerializer(read_only=True)
    id_monitor = AdministrativeUserSerializer(read_only=True)
    supplies = ConsumSupplySerializer(source='consumsupply_set', many=True, read_only=True)

    class Meta:
        model = Consum
        fields = ['id', 'id_lender', 'id_monitor', 'supplies']