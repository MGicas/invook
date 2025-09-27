from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class AdminTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # claims extras
        token["username"] = user.username
        token["role"] = getattr(user, "role", "UNKNOWN")
        token["state"] = getattr(user, "state", None)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)  # hace authenticate internamente
        # Validación adicional de estado
        if getattr(self.user, "state", None) == "INACTIVO" or not self.user.is_active:
            from rest_framework.exceptions import AuthenticationFailed
            raise AuthenticationFailed("Usuario inactivo.", code="user_inactive")

        # payload extra para respuesta
        data.update({
            "user": {
                "id": self.user.id,
                "username": self.user.username,
                "email": self.user.email,
                "first_name": self.user.first_name,
                "last_name": self.user.last_name,
                "role": getattr(self.user, "role", "UNKNOWN"),
                "state": getattr(self.user, "state", None),
                "profile": {
                    "rfid": getattr(getattr(self.user, "profile", None), "rfid", None),
                    "names": getattr(getattr(self.user, "profile", None), "names", None),
                    "surnames": getattr(getattr(self.user, "profile", None), "surnames", None),
                    "phone": getattr(getattr(self.user, "profile", None), "phone", None),
                    "document_id": getattr(getattr(self.user, "profile", None), "document_id", None),
                } if getattr(self.user, "profile", None) else None
            }
        })
        return data
