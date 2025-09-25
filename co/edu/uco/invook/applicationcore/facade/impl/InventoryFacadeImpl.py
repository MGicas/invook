from typing import Optional
from ..InventoryFacade import InventoryFacade
from ...usecase.impl.HardwareUseCase import HardwareUseCase
from ...usecase.impl.SupplyUseCase import SupplyUseCase
from ...usecase.impl.ConsumUseCase import ConsumUseCase
from ...usecase.impl.LoanUseCase import LoanUseCase
from ....crosscutting.exception.impl.BusinessException import BusinessException, MissingFieldException
from ....applicationcore.domain.resource.Loan import Loan
from ....applicationcore.domain.inventory.Supply import Supply
from ....services.inventory.SupplyService import SupplyService

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
    def create_supply(self, **kwargs) -> Supply:
        return self.supply_uc.create(**kwargs)

    def get_supply(self, code: str):
        return self.supply_uc.get(code)

    def patch_supply(self, code: str, **kwargs):
        return self.supply_uc.patch(code, **kwargs)

    def delete_supply(self, code: str):
        return self.supply_uc.delete(code)

    def list_all_supplies(self):
        return self.supply_uc.list_all()
    
    def restock_supply(self, code, count, quantity):
        return self.supply_uc.restock(code, count, quantity)

    #Consum
    def create_consum(self, id_lender, id_monitor, supplies_list: list):
        return self.consum_uc.create(id_lender, id_monitor, supplies_list)

    def get_consum(self, code: str):
        return self.consum_uc.get(code)

    def patch_consum(self, code: str, **kwargs):
        return self.consum_uc.patch(code, **kwargs)
    
    def update_consum(self, identifier, **kwargs):
        return self.consum_uc.update(identifier, **kwargs)

    def list_all_consums(self):
        return self.consum_uc.list_all()
    
    #Loan
    def create_loan(self, id_lender: str, id_monitor: str, serials_hardware: list[str], status: Optional[str] = None) -> Loan:
        return self.loan_uc.create_loan(id_lender, id_monitor, serials_hardware, status)

    def get_loan(self, id: str) -> Loan:
        return self.loan_uc.get(id)

    def patch_loan(self, id: str, **kwargs) -> Loan:
        return self.loan_uc.patch(id, **kwargs)

    def close_loan(self, id: str) -> Loan:
        return self.loan_uc.close_loan(id)

    def list_all_loans(self) -> list[Loan]:
        return self.loan_uc.list_all()

    def add_hardware_to_loan(self, loan_id: str, serials_hardware: list[str]) -> Loan:
        return self.loan_uc.add_hardware(loan_id, serials_hardware)

    def return_hardware_from_loan(self, loan_id: str, serials_to_return: list[str]) -> Loan:
        return self.loan_uc.return_hardware_loan(loan_id, serials_to_return)

    