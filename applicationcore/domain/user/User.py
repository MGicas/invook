from abc import ABC, abstractmethod
from dataclasses import dataclass

from UtilText import UtilText


@dataclass
class User(ABC):
    _id: str
    _rfid: str
    _names: str
    _surnames: str
    _email: str
    _phone: str

    def __init__(self, id: str, rfid: str, names: str, surnames: str, email: str, phone: str):
        self.set_id(id)
        self.set_rfid(rfid)
        self.set_names(names)
        self.set_surnames(surnames)
        self.set_email(email)
        self.set_phone(phone)

    @classmethod
    def build(cls, id: str, rfid: str, names: str, surnames: str, email: str, phone: str):
        raise NotImplementedError("Use a subclass to instantiate a User.")

    @classmethod
    def build_dummy(cls):
        raise NotImplementedError("Use a subclass to instantiate a User.")
        
    def set_id(self, id: str):
        self._id = UtilText.apply_trim(id)
        return self
    
    def set_rfid(self, rfid: str):
        self._rfid = UtilText.apply_trim(rfid)
        return self
    
    def set_names(self, names: str):
        self._names = UtilText.apply_trim(names)
        return self
    
    def set_surnames(self, surnames: str):
        self._surnames = UtilText.apply_trim(surnames)
        return self
    
    def set_email(self, email: str):
        self._email = UtilText.apply_trim(email)
        return self
    
    def set_phone(self, phone: str):
        self._phone = UtilText.apply_trim(phone)
        return self

    def get_id(self) -> str: return self._id
    
    def get_rfid(self) -> str: return self._rfid
    
    def get_names(self) -> str: return self._names
    
    def get_surnames(self) -> str: return self._surnames
    
    def get_email(self) -> str: return self._email
    
    def get_phone(self) -> str: return self._phone
