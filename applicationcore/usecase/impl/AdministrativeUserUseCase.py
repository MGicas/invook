from co.edu.uco.invook.applicationcore.domain.user.AdministrativeUser import AdministrativeUser
from co.edu.uco.invook.applicationcore.usecase.GeneralUsecase import GeneralUseCase
from co.edu.uco.invook.services.user.AdministrativeUserService import AdministrativeUserService
from django.contrib.auth.hashers import make_password

class AdministrativeUserUseCase(GeneralUseCase):

    def create(self, **kwargs) -> AdministrativeUser:
        return AdministrativeUserService.create_administrative_user(**kwargs)

    def get(self, id: int) -> AdministrativeUser:
        return AdministrativeUserService.get(id)

    def patch(self, id: int, **kwargs):
        return AdministrativeUserService.patch_administrative_user(id, **kwargs)

    def delete(self, id: int) -> None:
        admin_user = AdministrativeUserService.get(id)
        if admin_user:
            AdministrativeUserService.delete_administrative_user(admin_user)

    def list_all(self) -> list[AdministrativeUser]:
        return AdministrativeUserService.list_all()
    
    def mark_unactive(self, id: int) -> AdministrativeUser:
        admin_user = AdministrativeUserService.get(id)
        if admin_user:
            return AdministrativeUserService.mark_unactive(admin_user)
        return None
    
    def mark_active(self, id: int) -> AdministrativeUser:
        admin_user = AdministrativeUserService.get(id)
        if admin_user:
            return AdministrativeUserService.mark_active(admin_user)
        return None
    
    def update(self, id: int, **kwargs) -> AdministrativeUser:
        admin_user = AdministrativeUserService.get(id)
        if admin_user:
            return AdministrativeUserService.update_administrative_user(admin_user, **kwargs)
        return None
    
    def change_password(self, id: int, new_password: str) -> AdministrativeUser:
        admin_user = AdministrativeUserService.get(id)
        if admin_user:
            hashed_password = make_password(new_password)
            return AdministrativeUserService.update_administrative_user(admin_user, password=hashed_password)
        return None
    