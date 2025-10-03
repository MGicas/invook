from ....applicationcore.domain.resource.ConsumSupply import ConsumSupply
from rest_framework import serializers

class ConsumSupplySerializer(serializers.ModelSerializer):
    supply_code = serializers.CharField(write_only=True)      
    supply = serializers.CharField(source="supply.code", read_only=True)
    supply_name = serializers.CharField(source="supply.name", read_only=True)  

    class Meta:
        model = ConsumSupply
        fields = ["supply_code", "supply", "supply_name", "quantity"]

