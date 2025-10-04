from abc import ABC, abstractmethod

class UserFacade(ABC):

    # Lender
    @abstractmethod
    def create_lender(self, **kwargs):
        pass

    @abstractmethod
    def get_lender(self, id):
        pass
    
    @abstractmethod
    def patch_lender(self, id, **kwargs):
        pass

    @abstractmethod
    def delete_lender(self, id):
        pass

    @abstractmethod
    def list_all_lenders(self):
        pass

    @abstractmethod
    def change_lender_state(self, id):
        pass
    
    #AdministrativeUser

    @abstractmethod
    def create_administrative_user(self, **kwargs):
        pass

    @abstractmethod
    def update_profile(self, **kwargs):
        pass

    @abstractmethod
    def change_state(self, **kwargs):
        pass

    @abstractmethod
    def set_role(self, **kwargs):
        pass
