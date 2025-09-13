from ....applicationcore.domain.resource.ConsumSupply import ConsumSupply
from .SupplySerializer import SupplySerializer
from rest_framework import serializers

class ConsumSupplySerializer(serializers.ModelSerializer):
    supply = SupplySerializer() 
    class Meta:
        model = ConsumSupply
        fields = ['supply', 'quantity']