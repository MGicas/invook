from rest_framework import serializers

class SupplySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=100, read_only=True)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=500)
    stock = serializers.IntegerField()
