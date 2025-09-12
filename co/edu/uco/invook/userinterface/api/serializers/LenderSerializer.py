from rest_framework import serializers

class LenderSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    rfid = serializers.CharField(max_length=100)
    names = serializers.CharField(max_length=100)
    surnames = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=20)
