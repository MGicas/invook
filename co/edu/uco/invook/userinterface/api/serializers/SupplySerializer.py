from rest_framework import serializers
from ....applicationcore.domain.inventory.Supply import Supply
from ....applicationcore.usecase.impl.SupplyUseCase import SupplyUseCase

class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = ["code", "name", "description", "supply_type", "count", "quantity", "stock"]
        read_only_fields = ["stock"]  
