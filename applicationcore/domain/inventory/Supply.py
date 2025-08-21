from dataclasses import dataclass

from UtilNumber import UtilNumber
from co.edu.uco.invook.crosscutting.util.UtilText import UtilText


@dataclass
class Supply:
    _code: str
    _name: str
    _description: str
    _stock: int
    
    def __init__(self, code: str, name: str, description: str, stock: int):
        self.set_code(code)
        self.set_name(name)
        self.set_description(description)
        self.set_stock(stock)
        
    @classmethod
    def build(cls, code: str, name: str, description: str, stock: int):
        return cls(code, name, description, stock)
    
    
    @classmethod
    def build_dummy(cls):
        return cls(
            code = UtilText.EMPTY,
            name = UtilText.EMPTY,
            description = UtilText.EMPTY,
            stock = UtilNumber.ZERO,
        )
    
    def set_code(self, code: str):
        self._code = UtilText.apply_trim(code)
        return self
    
    def set_name(self, name: str):
        self._name = UtilText.apply_trim(name)
        return self
    
    def set_description(self, description: str):
        self._description = UtilText.apply_trim(description)
        return self
    
    def set_stock(self, stock: int):
        self._stock = stock
        return self
    
    def get_code(self) -> str: return self._code   
    def get_name(self) -> str: return self._name   
    def get_description(self) -> str: return self._description
    def get_stock(self) -> int: return self._stock