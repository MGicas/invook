from ..UserFacade import UserFacade
from ...dto.CreateAdministrativeUserDTO import CreateAdministrativeUserDTO
from ....services.user.AdministrativeUserService import AdministrativeUserService
from ....services.user.LenderService import LenderService

class UserFacadeImpl(UserFacade):

    def __init__(self):
        self.administrative_service = AdministrativeUserService()
        self.lender_service = LenderService()

    #AdministrativeUser
    def create_administrative_user(self, dto: CreateAdministrativeUserDTO):
        return self.administrative_service.create_with_profile(dto)

    def update_profile(self, user_id: int, **changes):
        return self.administrative_service.update_profile(user_id, **changes)

    def change_state(self, user_id: int, new_state: str):
        return self.administrative_service.change_state(user_id, new_state)

    def set_role(self, user_id: int, role: str):
        return self.administrative_service.set_role(user_id, role)

    #Lender
    def create_lender(self, **kwargs):
        return self.lender_service.create(**kwargs)
    
    def get_lender(self, id: str):
        return self.lender_service.get(id)
    
    def patch_lender(self, id: str, **kwargs):
        return self.lender_service.patch(id, **kwargs)
    
    def delete_lender(self, id: str):
        return self.lender_service.delete(id)
    
    def list_all_lenders(self):
        return self.lender_service.list_all()