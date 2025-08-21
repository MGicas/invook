from enum import Enum

class AdministrativeUserState(Enum):
    ACTIVO = "ACTIVO"
    INACTIVO = "INACTIVO"

    def __str__(self):
        return self.value