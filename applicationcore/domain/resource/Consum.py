from dataclasses import dataclass
from UtilNumber import UtilNumber
from co.edu.uco.invook.crosscutting.util.UtilText import UtilText
from inventory import Supply

@dataclass
class Consum:
    _id: str
    _count: int
    _rfidLender: str
    _idLender: str
    _idMonitor: str
    _codeSupply: str
    _quantity: int
    
    def __init__(self, id: str, count: int, rfidLender: str, idLender: str, idMonitor: str, codeSupply: str, quantity: int):
        self.set_id(id)
        self.set_count(count)
        self.set_rfidLender(rfidLender)
        self.set_idLender(idLender)
        self.set_idMonitor(idMonitor)
        self.set_codeSupply(codeSupply)
        
    @classmethod
    def build(cls, id: str, count: int, rfidLender: str, idLender: str, idMonitor: str, codeSupply: str, quantity: int):
        return cls(id, count, rfidLender, idLender, idMonitor, codeSupply, quantity)
    @classmethod
    def build_dummy(cls):
        return cls(
            id = UtilText.EMPTY,
            count = UtilNumber.ZERO,
            rfidLender = UtilText.EMPTY,
            idLender = UtilText.EMPTY,
            idMonitor = UtilText.EMPTY,
            codeSupply = UtilText.EMPTY,
            quantity = UtilNumber.ZERO
        )
    
    def set_id(self, id: str):
        self._id = UtilText.apply_trim(id)
        return self
    
    def set_count(self, count: int):
        self._count = count
        return self
    
    def set_rfidLender(self, rfidLender: str):
        self._rfidLender = UtilText.apply_trim(rfidLender)
        return self
    
    def set_idLender(self, idLender: str):
        self._idLender = UtilText.apply_trim(idLender)
        return self
    
    def set_idMonitor(self, idMonitor: str):
        self._idMonitor = UtilText.apply_trim(idMonitor)
        return self
    
    def set_codeSupply(self, codeSupply: str):
        self._codeSupply = UtilText.apply_trim(codeSupply)
        return self
    
    def set_quantity(self, quantity: int):
        self._quantity = quantity
        return self
    
    
    def get_id(self) -> str: return self._id
    
    def get_count(self) -> int: return self._count
    
    def get_rfidLender(self) -> str: return self._rfidLender
    
    def get_idLender(self) -> str: return self._idLender
    
    def get_idMonitor(self) -> str: return self._idMonitor
    
    def get_codeSupply(self) -> str: return self._codeSupply
    
    def get_quantity(self) -> int: return self._quantity