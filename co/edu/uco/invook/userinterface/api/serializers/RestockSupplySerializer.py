from rest_framework import serializers

class RestockSupplyInSerializer(serializers.Serializer):
    count = serializers.IntegerField(min_value=0, required=True)
    quantity = serializers.IntegerField(min_value=0, required=True)