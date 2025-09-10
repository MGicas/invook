from abc import ABC, abstractmethod

class InventoryFacade(ABC):

    #Hardware
    @abstractmethod
    def create_hardware(self, **kwargs):
        pass

    @abstractmethod
    def get_hardware(self, identifier):
        pass

    @abstractmethod
    def patch_hardware(self, identifier, **kwargs):
        pass

    @abstractmethod
    def delete_hardware(self, identifier):
        pass

    @abstractmethod
    def list_all_hardwares(self):
        pass
    
    #Supply
    @abstractmethod
    def create_supply(self, **kwargs):
        pass

    @abstractmethod
    def get_supply(self, identifier):
        pass

    @abstractmethod
    def patch_supply(self, identifier, **kwargs):
        pass

    @abstractmethod
    def delete_supply(self, identifier):
        pass

    @abstractmethod
    def list_all_supplies(self):
        pass    

    @abstractmethod
    def restock_supply(self, identifier, quantity):
        pass    

    #Consum
    @abstractmethod
    def create_consum(self, **kwargs):
        pass

    @abstractmethod
    def get_consum(self, identifier):
        pass    

    @abstractmethod
    def patch_consum(self, identifier, **kwargs):
        pass

    @abstractmethod
    def update_consum(self, identifier, **kwargs):
        pass    

    @abstractmethod
    def delete_consum(self, identifier):
        pass    


    #Loan
    @abstractmethod
    def create_loan(self, **kwargs):
        pass
    
    @abstractmethod
    def get_loan(self, identifier):
        pass
    
    @abstractmethod
    def patch_loan(self, identifier, **kwargs):
        pass
    
    @abstractmethod
    def close_loan(self, identifier):
        pass
    
    @abstractmethod
    def list_all_loans(self):
        pass
    
    @abstractmethod
    def return_hardware_loan(self, identifier, serials_to_return: list[str]):
        pass