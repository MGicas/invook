from rest_framework import serializers
from ....applicationcore.domain.user.AdministrativeUser import AdministrativeUser
from ....applicationcore.domain.user.AdministrativeProfile import AdministrativeProfile
from ....applicationcore.dto.CreateAdministrativeUserDTO import CreateAdministrativeUserDTO

class AdministrativeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrativeProfile
        fields = ("rfid", "names", "surnames", "phone", "document_id")

class AdministrativeUserDetailSerializer(serializers.ModelSerializer):
    profile = AdministrativeProfileSerializer()
    role = serializers.CharField(read_only=True)
    class Meta:
        model = AdministrativeUser
        fields = ("id","username","email","first_name","last_name","state","role","profile")

class AdministrativeUserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField(required=False, allow_blank=True, allow_null=True)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    last_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    role = serializers.ChoiceField(choices=["ADMIN","MONITOR"])
    rfid = serializers.CharField(max_length=50)
    names = serializers.CharField(max_length=100)
    surnames = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=20)
    document_id = serializers.CharField(max_length=20)

    def to_dto(self) -> CreateAdministrativeUserDTO:
        d = self.validated_data
        return CreateAdministrativeUserDTO(
            username=d["username"], email=d.get("email"),
            password=d["password"], first_name=d.get("first_name"),
            last_name=d.get("last_name"), rfid=d["rfid"],
            names=d["names"], surnames=d["surnames"],
            phone=d["phone"], document_id=d["document_id"], role=d["role"]
        )

class AdministrativeUserUpdateProfileSerializer(serializers.Serializer):
    rfid = serializers.CharField(required=False)
    names = serializers.CharField(required=False)
    surnames = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    document_id = serializers.CharField(required=False)

class ChangeStateSerializer(serializers.Serializer):
    state = serializers.ChoiceField(choices=[("ACTIVO","ACTIVO"),("INACTIVO","INACTIVO")])

class SetRoleSerializer(serializers.Serializer):
    role = serializers.ChoiceField(choices=["ADMIN","MONITOR","UNKNOWN"])
