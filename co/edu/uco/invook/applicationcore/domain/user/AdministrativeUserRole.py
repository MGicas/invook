from enum import Enum

class AdministrativeUserRole(Enum):
    ADMIN = "ADMIN"
    MONITOR = "MONITOR"

    def __str__(self):
        return self.value