from dataclasses import dataclass
from AdministrativeUserState import AdministrativeUserState
from AdministrativeUserRole import AdministrativeUserRole
from UtilText import UtilText

@dataclass
class AdministrativeUser:
    _username: str
    _password: str
    _state: AdministrativeUserState
    _role: AdministrativeUserRole
    
    def __init__(self, username: str, password: str, state: AdministrativeUserState, role: AdministrativeUserRole):
        self.set_username(username)
        self.set_password(password)
        self.set_state(state)
        self.set_role(role)
    
    @classmethod
    def build(cls, username: str, password: str, state: AdministrativeUserState, role: AdministrativeUserRole):
        return cls(username, password, state, role)

    @classmethod
    def build_dummy(cls):
        return cls(
            username = "",
            password = "",
            state = AdministrativeUserState.INACTIVO,
            role = AdministrativeUserRole.MONITOR
        )

    def set_username(self, username: str):
        self._username = UtilText.apply_trim(username)
        return self
    
    def set_password(self, password: str):
        self._password = UtilText.apply_trim(password)
        return self
    
    def set_state(self, state: AdministrativeUserState):
        self._state = state
        return self
    
    def set_role(self, role: AdministrativeUserRole):
        self._role = role
        return self
    
    def get_username(self) -> str: return self._username
    
    def get_state(self) -> AdministrativeUserState: return self._state
    
    def get_role(self) -> AdministrativeUserRole: return self._role