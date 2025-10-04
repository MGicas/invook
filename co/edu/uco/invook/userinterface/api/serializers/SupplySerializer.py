from rest_framework import serializers
from ....applicationcore.domain.inventory.Supply import Supply
from ....applicationcore.domain.inventory.SupplyType import SupplyType

class SupplySerializer(serializers.ModelSerializer):
    
    supply_type = serializers.SlugRelatedField(
        slug_field="name",
        queryset=SupplyType.objects.all()
    )
    
    class Meta:
        model = Supply
        fields = ["code", "name", "description", "supply_type", "count", "quantity", "stock"]
        read_only_fields = ["stock"]  