from co.edu.uco.invook.applicationcore.facade.UserFacade import UserFacade
from co.edu.uco.invook.applicationcore.usecase.impl.AdministrativeUserUseCase import AdministrativeUserUseCase
from co.edu.uco.invook.applicationcore.usecase.impl.LenderUseCase import LenderUseCase


class UserFacadeImpl(UserFacade):

    def __init__(self):
        self.administrative_user_uc = AdministrativeUserUseCase()
        self.lender_uc = LenderUseCase()

    #AdministrativeUser
    def create_administrative_user(self, **kwargs):
        return self.administrative_user_uc.create(**kwargs)
    
    def get_administrative_user(self, id: str):
        return self.administrative_user_uc.get(id)
    
    def patch_administrative_user(self, id: str, **kwargs):
        return self.administrative_user_uc.patch(id, **kwargs)
    
    def delete_administrative_user(self, id: str):
        return self.administrative_user_uc.delete(id)
    
    def list_all_administrative_users(self):
        return self.administrative_user_uc.list_all()
    
    def mark_administrative_user_unactive(self, id: str):
        return self.administrative_user_uc.mark_unactive(id)
    
    def mark_administrative_user_active(self, id: str):
        return self.administrative_user_uc.mark_active(id)
    
    def update_administrative_user(self, id: str, **kwargs):    
        return self.administrative_user_uc.update(id, **kwargs)
    
    def change_administrative_user_password(self, id: str, new_password: str):
        return self.administrative_user_uc.change_password(id, new_password)

    #Lender
    def create_lender(self, **kwargs):
        return self.lender_uc.create(**kwargs)
    
    def get_lender(self, id: str):
        return self.lender_uc.get(id)
    
    def patch_lender(self, id: str, **kwargs):
        return self.lender_uc.patch(id, **kwargs)
    
    def delete_lender(self, id: str):
        return self.lender_uc.delete(id)
    
    def list_all_lenders(self):
        return self.lender_uc.list_all()