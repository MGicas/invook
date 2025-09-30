from typing import Optional
from ..InventoryFacade import InventoryFacade
from ....crosscutting.exception.impl.BusinessException import BusinessException, MissingFieldException
from ....applicationcore.domain.resource.Loan import Loan
from ....applicationcore.domain.inventory.Supply import Supply
from ....services.inventory.HardwareService import HardwareService
from ....services.inventory.SupplyService import SupplyService
from ....services.resource.ConsumService import ConsumService
from ....services.resource.LoanService import LoanService

class InventoryFacadeImpl(InventoryFacade): 

    def __init__(self):
        self.hardware_service = HardwareService()
        self.supply_service = SupplyService()
        self.consum_service = ConsumService()    
        self.loan_service = LoanService()

    #Hardware
    def create_hardware(self, **kwargs):
        return self.hardware_service.create_hardware(**kwargs)

    def get_hardware(self, serial: str):
        return self.hardware_service.get(serial)

    def patch_hardware(self, serial: str, **kwargs):
        return self.hardware_service.patch_hardware(serial, **kwargs)

    def delete_hardware(self, serial: str):
        return self.hardware_service.delete_hardware(serial)

    def list_all_hardwares(self):
        return self.hardware_service.list_all()
    
    def list_hardwares_by_type(self, hardware_type_id: str):
        return self.hardware_service.list_by_type(hardware_type_id)


    def toggle_availability(self, serial: str):
        return self.hardware_service.toggle_availability(serial)


    #Supply
    def create_supply(self, **kwargs) -> Supply:
        return self.supply_service.create_supply(**kwargs)

    def get_supply(self, code: str):
        return self.supply_service.get(code)

    def patch_supply(self, code: str, **kwargs):
        return self.supply_service.patch_supply(code, **kwargs)

    def delete_supply(self, code: str):
        return self.supply_service.delete_supply(code)

    def list_all_supplies(self):
        return self.supply_service.list_all()
    
    def list_supplies_by_type(self, supply_type_id: str):
        return self.supply_service.list_by_type(supply_type_id)

    def list_low_stock_supplies(self, threshold: int):
        return self.supply_service.list_low_stock(threshold)

    def restock_supply(self, code, count, quantity):
        return self.supply_service.restock_supply(code, count, quantity)

    #Consum
    def create_consum(self, id_lender, id_monitor, supplies_list: list):
        return self.consum_service.create_consum(id_lender, id_monitor, supplies_list)

    def get_consum(self, code: str):
        return self.consum_service.get(code)

    def patch_consum(self, code: str, **kwargs):
        return self.consum_service.patch_consum(code, **kwargs)
    
    def update_consum(self, identifier, **kwargs):
        return self.consum_service.update_consum(identifier, **kwargs)

    def list_all_consums(self):
        return self.consum_service.list_all()
    
    #Loan
    def create_loan(self, id_lender: str, id_monitor: str, serials_hardware: list[str], status: Optional[str] = None) -> Loan:
        return self.loan_service.create_loan(id_lender, id_monitor, serials_hardware, status)

    def get_loan(self, id: str) -> Loan:
        return self.loan_service.get(id)

    def patch_loan(self, id: str, **kwargs) -> Loan:
        return self.loan_service.patch_loan(id, **kwargs)

    def close_loan(self, id: str) -> Loan:
        return self.loan_service.close_loan(id)

    def list_all_loans(self, status: Optional[str] = None) -> list[Loan]:
        if status:
            return self.loan_service.list_all(status)
        return self.loan_service.list_all()
    
    def list_loans_by_lender(self, lender_id: str, status: Optional[str] = None) -> list[Loan]:
        return self.loan_service.list_by_lender(lender_id, status)


    def add_hardware_to_loan(self, loan_id: str, serials_hardware: list[str]) -> Loan:
        return self.loan_service.add_hardware_to_loan(loan_id, serials_hardware)

    def return_hardware_from_loan(self, loan_id: str, hardware_returns: list[dict], id_monitor: str) -> Loan:
        return self.loan_service.return_hardware(loan_id, hardware_returns, id_monitor)
