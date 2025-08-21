from dataclasses import dataclass
from UtilNumber import UtilNumber
from UtilObject import UtilObject
from UtilText import UtilText
from inventory import Hardware
from LoanStatus import LoanStatus
from datetime import datetime

@dataclass
class Loan:
    _id: str
    _count: int
    _rfidLender: str
    _idLender: str
    _idMonitor: str
    _serialHardware: str
    _loanDate: datetime
    _returnDate: datetime
    _status: LoanStatus

    def __init__(self, id: str, count: int, rfidLender: str, idLender: str, idMonitor: str, serialHardware: Hardware, loanDate: datetime, returnDate: datetime, status: LoanStatus):
        self.set_id(id)
        self.set_count(count)
        self.set_rfidLender(rfidLender)
        self.set_idLender(idLender)
        self.set_idMonitor(idMonitor)
        self.set_serialHardware(serialHardware)
        self.set_loadDate(loanDate)
        self.set_returnDate(returnDate)
        self.set_status(status)
    
    @classmethod
    def build(cls, id: str, count: int, rfidLender: str, idLender: str, idMonitor: str, serialHardware: Hardware, loanDate: datetime, returnDate: datetime, status: LoanStatus):
        return cls(id, count, rfidLender, idLender, idMonitor, serialHardware, loanDate, returnDate, status)
    
    @classmethod
    def build_dummy(cls):   
        return cls(
            id = UtilText.EMPTY,
            count = UtilNumber.ZERO,
            rfidLender = UtilText.EMPTY,
            idLender = UtilText.EMPTY,
            idMonitor = UtilText.EMPTY,
            serialHardware = UtilText.EMPTY,
            loanDate = datetime.now(),
            returnDate = datetime.now(),
            status = LoanStatus.ABIERTO
        )

    def set_id(self, id: str):
        self._id = UtilText.apply_trim(id)
        return self
    
    def set_count(self, count: int):
        self._count = count
        return self
    
    def set_rfidLender(self, rfidLender: str):
        self._rfidLender = UtilText.apply_trim(rfidLender)
        return self
    
    def set_idLender(self, idLender: str):
        self._idLender = UtilText.apply_trim(idLender)
        return self
    
    def set_idMonitor(self, idMonitor: str):
        self._idMonitor = UtilText.apply_trim(idMonitor)
        return self
    
    def set_serialHardware(self, hardware: str):
        self._hardware = UtilText.apply_trim(hardware)
        return self 
    
    def set_loadDate(self, loadDate: datetime):
        self._loadDate = UtilObject.get_default(datetime, datetime.now())
        return self
    
    def set_returnDate(self, returnDate: datetime):
        self._returnDate = UtilObject.get_default(datetime, datetime.now())
        return self
    
    def set_status(self, status: LoanStatus):
        self._status = status
        return self 
    
    def get_id(self) -> str: return self._id 
    def get_count(self) -> int: return self._count
    def get_rfidLender(self) -> str: return self._rfidLender
    def get_idLender(self) -> str: return self._idLender
    def get_idMonitor(self) -> str: return self._idMonitor
    def get_serialHardware(self) -> Hardware: return self._hardware
    def get_loadDate(self) -> datetime: return self._loadDate
    def get_returnDate(self) -> datetime: return self._returnDate
    def get_status(self) -> LoanStatus: return self._status
    