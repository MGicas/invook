from enum import Enum

class HardwareAvailable(Enum):
    DISPONIBLE = "DISPONIBLE"
    NO_DISPONIBLE = "NO_DISPONIBLE"

    def __str__(self):
        return self.value