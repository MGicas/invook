from abc import ABC, abstractmethod

class UserFacade(ABC):

    # Lender
    @abstractmethod
    def create_lender(self, user_data):
        pass

    @abstractmethod
    def get_lender(self, user_id):
        pass

    @abstractmethod
    def delete_lender(self, user_id):
        pass

    @abstractmethod
    def list_all_lenders(self):
        pass

    #AdministrativeUser
    @abstractmethod
    def create_administrative_user(self, user_data):
        pass

    @abstractmethod
    def get_administrative_user(self, user_id):
        pass

    @abstractmethod
    def patch_administrative_user(self, user_id, **kwargs):
        pass

    @abstractmethod
    def delete_administrative_user(self, user_id):
        pass

    @abstractmethod
    def list_all_administrative_users(self):
        pass

    @abstractmethod
    def mark_administrative_user_active(self, user_id):
        pass

    @abstractmethod
    def mark_administrative_user_unactive(self, user_id):
        pass

    @abstractmethod
    def update_administrative_user(self, user_id, **kwargs):
        pass

    @abstractmethod
    def change_administrative_user_password(self, user_id, new_password):
        pass
    
