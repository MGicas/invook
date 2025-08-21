from enum import Enum

class HardwareState(Enum):
    BUENO = "BUENO"
    FUNCIONAL = "FUNCIONAL"
    DAÑO_LEVE = "DAÑO_LEVE"
    NO_FUNCIONA = "NO_FUNCIONA"
    PERDIDO = "PERDIDO"

    def __str__(self):
        return self.value