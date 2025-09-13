from rest_framework import serializers

class AdministrativeUserSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=15)
    rfid = serializers.CharField(max_length=100)
    names = serializers.CharField(max_length=100)
    surnames = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    
