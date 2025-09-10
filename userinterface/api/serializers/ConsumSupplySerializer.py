from co.edu.uco.invook.applicationcore.domain.resource.ConsumSupply import ConsumSupply
from co.edu.uco.invook.userinterface.api.serializers.SupplySerializer import SupplySerializer
from rest_framework import serializers

class ConsumSupplySerializer(serializers.ModelSerializer):
    supply = SupplySerializer() 
    class Meta:
        model = ConsumSupply
        fields = ['supply', 'quantity']