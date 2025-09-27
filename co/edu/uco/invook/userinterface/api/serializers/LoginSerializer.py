from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get("username", "").strip()
        password = attrs.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError({"detail": "Credenciales inválidas."})

        # Chequeo de estado propio (además de is_active si lo usas)
        if getattr(user, "state", None) == "INACTIVO" or not user.is_active:
            raise serializers.ValidationError({"detail": "Usuario inactivo."})

        attrs["user"] = user
        return attrs
