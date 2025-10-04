from rest_framework import serializers

class HardwareTypeSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=40, read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    active = serializers.BooleanField(read_only=True)