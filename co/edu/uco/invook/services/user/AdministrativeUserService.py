from django.db import transaction
from ...applicationcore.domain.user.AdministrativeUserState import AdministrativeUserState
from ...applicationcore.domain.user.AdministrativeUser import AdministrativeUser
from django.core.exceptions import ValidationError
from ...applicationcore.domain.user.AdministrativeProfile import AdministrativeProfile
from ...applicationcore.dto.CreateAdministrativeUserDTO import CreateAdministrativeUserDTO
from django.contrib.auth.models import Group

ADMIN_GROUP = "ADMIN"
MONITOR_GROUP = "MONITOR"

class AdministrativeUserService:
    @transaction.atomic
    def create_with_profile(self, dto: CreateAdministrativeUserDTO) -> AdministrativeUser:
        if AdministrativeUser.objects.filter(username=dto.username).exists():
            raise ValidationError({"username": "Ya existe un usuario con este username."})
        if AdministrativeProfile.objects.filter(document_id=dto.document_id).exists():
            raise ValidationError({"document_id": "Ya existe un perfil con este documento."})
        if AdministrativeProfile.objects.filter(rfid=dto.rfid).exists():
            raise ValidationError({"rfid": "Ya existe un perfil con este RFID."})

        user = AdministrativeUser(
            username=dto.username,
            email=dto.email or "",
            first_name=dto.first_name or "",
            last_name=dto.last_name or "",
            state=AdministrativeUserState.ACTIVO.name,
        )
        user.set_password(dto.password)
        user.save()

        profile = AdministrativeProfile(
            user=user,
            rfid=dto.rfid,
            names=dto.names,
            surnames=dto.surnames,
            phone=dto.phone,
            document_id=dto.document_id,
        )
        profile.save()

        self._assign_role(user, dto.role)
        return user

    @transaction.atomic
    def update_profile(self, user_id: int, **changes) -> AdministrativeUser:
        user = AdministrativeUser.objects.select_related("profile").get(id=user_id)
        p = user.profile
        for field in {"rfid", "names", "surnames", "phone", "document_id"}:
            if field in changes and changes[field] is not None:
                setattr(p, field, changes[field])
        p.save()
        return user

    @transaction.atomic
    def change_state(self, user_id: int, new_state: str) -> AdministrativeUser:
        if new_state not in [s.name for s in AdministrativeUserState]:
            raise ValidationError({"state": "Estado inválido."})
        user = AdministrativeUser.objects.get(id=user_id)
        user.state = new_state
        user.save()
        return user

    @transaction.atomic
    def set_role(self, user_id: int, role: str) -> AdministrativeUser:
        user = AdministrativeUser.objects.get(id=user_id)
        self._assign_role(user, role)
        return user

    def _assign_role(self, user: AdministrativeUser, role: str) -> None:
        role = role.upper()
        user.groups.clear()
        if role == "ADMIN":
            user.groups.add(Group.objects.get(name=ADMIN_GROUP))
        elif role == "MONITOR":
            user.groups.add(Group.objects.get(name=MONITOR_GROUP))
        else:
            raise ValidationError({"role": "Rol inválido."})