from rest_framework import serializers

from co.edu.uco.invook.applicationcore.domain.resource.Consum import Consum
from co.edu.uco.invook.userinterface.api.serializers.AdministrativeUserSerializer import AdministrativeUserSerializer
from co.edu.uco.invook.userinterface.api.serializers.ConsumSupplySerializer import ConsumSupplySerializer
from co.edu.uco.invook.userinterface.api.serializers.LenderSerializer import LenderSerializer

class ConsumSerializer(serializers.ModelSerializer):
    id_lender = LenderSerializer(read_only=True)
    id_monitor = AdministrativeUserSerializer(read_only=True)
    supplies = ConsumSupplySerializer(source='consumsupply_set', many=True, read_only=True)

    class Meta:
        model = Consum
        fields = ['id', 'id_lender', 'id_monitor', 'quantity', 'supplies']