from typing import Optional
from dataclasses import dataclass

@dataclass
class CreateAdministrativeUserDTO:
    username: str
    email: Optional[str]
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
    rfid: str
    names: str
    surnames: str
    phone: str
    document_id: str
    role: str  # "ADMIN" | "MONITOR"