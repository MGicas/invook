from rest_framework import serializers

from ....applicationcore.domain.resource.Consum import Consum
from .ConsumSupplySerializer import ConsumSupplySerializer
from .LenderSerializer import LenderSerializer
from ....applicationcore.facade.impl.InventoryFacadeImpl import InventoryFacadeImpl

class ConsumSerializer(serializers.ModelSerializer):

    id_lender = serializers.CharField()
    id_monitor = serializers.CharField()
    supplies = ConsumSupplySerializer(many=True, write_only=True)
    supplies_detail = ConsumSupplySerializer(source="consumsupply_set", many=True, read_only=True)

    class Meta:
        model = Consum
        fields = ['id', 'id_lender', 'id_monitor', 'supplies', 'supplies_detail']

    facade = InventoryFacadeImpl()

    def create(self, validated_data):
        supplies_data = validated_data.pop('supplies')
        lender = validated_data.pop('id_lender')
        monitor = validated_data.pop('id_monitor')

        try:
            return self.facade.create_consum(lender, monitor, supplies_data)
        except Exception as e:
            raise serializers.ValidationError({"error": str(e)})