from dataclasses import dataclass
from HardwareType import HardwareType
from HardwareState import HardwareState
from HardwareAvailable import HardwareAvailable
from co.edu.uco.invook.crosscutting.util.UtilText import UtilText

@dataclass
class Hardware:
    _serial: str
    _name: str
    _description: str
    _comment: str
    _state: HardwareState
    _idType: str
    _available: HardwareAvailable
    
    def __init__(self, serial: str, name: str, description: str, comment: str, state: HardwareState, idType: str, available: HardwareAvailable):
        self.set_serial(serial)
        self.set_name(name)
        self.set_description(description)
        self.set_comment(comment)
        self.set_state(state)
        self.set_idType(idType)
        self.set_available(available)
    
    @classmethod
    def build(cls, serial: str, name: str, description: str, comment: str, state: HardwareState, type: HardwareType, available: HardwareAvailable):
        return cls(serial, name, description, comment, state, type, available)

    @classmethod
    def build_dummy(cls):
        return cls(
            serial= UtilText.EMPTY,
            name = UtilText.EMPTY,
            description = UtilText.EMPTY,
            comment = UtilText.EMPTY,
            state = HardwareState.BUENO,
            idType = UtilText.EMPTY,
            available = HardwareAvailable.DISPONIBLE
        )
    
    def set_serial(self, serial: str):
        self._serial = UtilText.apply_trim(serial)
        return self

    def set_name(self, name: str):
        self._name = UtilText.apply_trim(name)
        return self
    
    def set_description(self, description: str):
        self._description = UtilText.apply_trim(description)
        return self
    
    def set_comment(self, comment: str):
        self._comment = UtilText.apply_trim(comment)
        return self

    def set_state(self, state: HardwareState):
        self._state = state
        return self
    
    def set_idType(self, idType: str):
        self._idType = idType
        return self
    
    def set_available(self, available: HardwareAvailable):
        self._available = available

    def get_serial(self) -> str: return self._serial
    def get_name(self) -> str: return self._name
    def get_description(self) -> str: return self._description
    def get_comment(self) -> str: return self._comment
    def get_state(self) -> HardwareState: return self._state
    def get_idType(self) -> HardwareType: return self._idType
    def get_available(self) -> HardwareAvailable: return self._available
    

