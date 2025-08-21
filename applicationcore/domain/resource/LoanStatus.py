from enum import Enum

class LoanStatus(Enum):
    ABIERTO = "ABIERTO"
    CERRADO = "CERRADO"
    VENCIDO = "VENCIDO"

    def __str__(self):
        return self.value