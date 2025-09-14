from ..InventoryFacade import InventoryFacade
from ...usecase.impl.HardwareUseCase import HardwareUseCase
from ...usecase.impl.SupplyUseCase import SupplyUseCase
from ...usecase.impl.ConsumUseCase import ConsumUseCase
from ...usecase.impl.LoanUseCase import LoanUseCase


class InventoryFacadeImpl(InventoryFacade):

    def __init__(self):
        self.hardware_uc = HardwareUseCase()
        self.supply_uc = SupplyUseCase()
        self.consum_uc = ConsumUseCase()    
        self.loan_uc = LoanUseCase()

    #Hardware
    def create_hardware(self, **kwargs):
        return self.hardware_uc.create(**kwargs)

    def get_hardware(self, serial: str):
        return self.hardware_uc.get(serial)

    def patch_hardware(self, serial: str, **kwargs):
        return self.hardware_uc.patch(serial, **kwargs)

    def delete_hardware(self, serial: str):
        return self.hardware_uc.delete(serial)

    def list_all_hardwares(self):
        return self.hardware_uc.list_all()

    def toggle_availability(self, serial: str):
        return self.hardware_uc.toggle_availability(serial)


    #Supply
    def create_supply(self, **kwargs):
        return self.supply_uc.create(**kwargs)

    def get_supply(self, code: str):
        return self.supply_uc.get(code)

    def patch_supply(self, code: str, **kwargs):
        return self.supply_uc.patch(code, **kwargs)

    def delete_supply(self, code: str):
        return self.supply_uc.delete(code)

    def list_all_supplies(self):
        return self.supply_uc.list_all()
    
    def restock_supply(self, identifier, quantity):
        return self.supply_uc.restock(identifier, quantity)

    #Consum
    def create_consum(self, **kwargs):
        return self.consum_uc.create(**kwargs)

    def get_consum(self, code: str):
        return self.consum_uc.get(code)

    def patch_consum(self, code: str, **kwargs):
        return self.consum_uc.patch(code, **kwargs)
    
    def update_consum(self, identifier, **kwargs):
        return self.consum_uc.update(identifier, **kwargs)

    def list_all_consums(self):
        return self.consum_uc.list_all()
    
    #Loan
    def create_loan(self, **kwargs):
        return self.loan_uc.create(**kwargs)

    def get_loan(self, loan_id: str):
        return self.loan_uc.get(loan_id)

    def patch_loan(self, loan_id: str, **kwargs):
        return self.loan_uc.patch(loan_id, **kwargs)

    def list_all_loans(self):
        return self.loan_uc.list_all()

    def close_loan(self, loan_id: str):
        loan = self.loan_uc.get(loan_id)
        return self.loan_uc.close_loan(loan_id)

    def return_hardware_loan(self, loan_id: str, serials: list[str]):
        loan = self.loan_uc.get(loan_id)
        return self.loan_uc.return_hardware_loan(loan, serials)

    def add_hardware_to_loan(self, loan_id: str, serial_hardware: str):
        return self.loan_uc.add_hardware(loan_id, serial_hardware)

    