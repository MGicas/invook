from ...domain.user.AdministrativeUser import AdministrativeUser
from ...usecase.GeneralUsecase import GeneralUseCase
from ....services.user.AdministrativeUserService import AdministrativeUserService
from ....crosscutting.exception.impl.BusinessException import AdministrativeUserNotFoundException
from django.contrib.auth.hashers import make_password

class AdministrativeUserUseCase(GeneralUseCase):
    
    service= AdministrativeUserService

    def create(self, **kwargs) -> AdministrativeUser:
        return AdministrativeUserService.create_administrative_user(**kwargs)

    def get(self, username: str) -> AdministrativeUser:
        return AdministrativeUserService.get(username)

    def patch(self, username: str, **kwargs):
        return AdministrativeUserService.patch_administrative_user(username, **kwargs)

    def delete(self, username: str) -> None:
        admin_user = self.service.get(username)
        if not admin_user:
            raise AdministrativeUserNotFoundException(username)
        
        self.service.delete_administrative_user(admin_user)

    def list_all(self) -> list[AdministrativeUser]:
        return AdministrativeUserService.list_all()
    
    def mark_unactive(self, username: str) -> AdministrativeUser:
        admin_user = AdministrativeUserService.get(username)
        if admin_user:
            return AdministrativeUserService.mark_unactive(admin_user)
        return None
    
    def mark_active(self, username: str) -> AdministrativeUser:
        admin_user = AdministrativeUserService.get(username)
        if admin_user:
            return AdministrativeUserService.mark_active(admin_user)
        return None
    
    def update(self, username: str, **kwargs) -> AdministrativeUser:
        admin_user = AdministrativeUserService.get(username)
        if admin_user:
            return AdministrativeUserService.update_administrative_user(admin_user, **kwargs)
        return None
    
    def change_password(self, username: str, old_password: str, new_password: str) -> AdministrativeUser:
        admin_user = AdministrativeUserService.get(username)
        if not admin_user:
            raise AdministrativeUserNotFoundException(username)
        return self.service.change_password(admin_user, old_password, new_password)
    