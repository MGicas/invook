from rest_framework import serializers

class AdministrativeUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    state = serializers.CharField(max_length=50)
    role = serializers.CharField(max_length=50)
