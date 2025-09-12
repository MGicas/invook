from rest_framework import serializers

class HardwareSerializer(serializers.Serializer):
    serial = serializers.CharField(max_length=100, read_only=True)
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=500)
    comment = serializers.CharField(max_length=300, allow_blank=True, required=False)
    hardwaretype = serializers.CharField(max_length=100)
