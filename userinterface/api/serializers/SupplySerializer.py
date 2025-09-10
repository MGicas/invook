from rest_framework import serializers

class SupplySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    supply_type = serializers.CharField()
    count = serializers.IntegerField()
    quantity = serializers.IntegerField()
    stock = serializers.IntegerField()
