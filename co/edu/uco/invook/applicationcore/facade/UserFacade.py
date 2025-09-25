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

    #AdministrativeUser
    @abstractmethod
    def create_administrative_user(self, **kwargs):
        pass

    @abstractmethod
    def get_administrative_user(self, username):
        pass

    @abstractmethod
    def patch_administrative_user(self, username, **kwargs):
        pass

    @abstractmethod
    def delete_administrative_user(self, username):
        pass

    @abstractmethod
    def list_all_administrative_users(self):
        pass

    @abstractmethod
    def mark_administrative_user_active(self, username):
        pass

    @abstractmethod
    def mark_administrative_user_unactive(self, username):
        pass

    @abstractmethod
    def update_administrative_user(self, username, **kwargs):
        pass

    @abstractmethod
    def change_administrative_user_password(self, username, new_password):
        pass
    
