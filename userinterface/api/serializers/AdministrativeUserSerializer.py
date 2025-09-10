from rest_framework import serializers

class AdministrativeUserSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=15)
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    
