from dataclasses import dataclass

from co.edu.uco.invook.crosscutting.util.UtilText import UtilText

@dataclass
class HardwareType:
    _id: str
    _name: str
    _description: str
    
    def __init__(self, id: str, name: str, description: str):
        self.set_id(id)
        self.set_name(name)
        self.set_description(description)
    
    @classmethod
    def build(cls, id: str, name: str, description: str):
        return cls(id, name, description)
    
    @classmethod
    def build_dummy(cls):
        return cls(
            id = UtilText.EMPTY,
            name = UtilText.EMPTY,
            description = UtilText.EMPTY
        )

    def set_id(self, id: str):
        self._id = UtilText.apply_trim(id)
        return self
    
    def set_name(self, name: str):
        self._name = UtilText.apply_trim(name)
        return self
    
    def set_description(self, description: str):
        self._description = UtilText.apply_trim(description)
        return self

    def get_id(self) -> str: return self._id
    def get_name(self) -> str: return self._name
    def get_description(self) -> str: return self._description