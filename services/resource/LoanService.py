import datetime
from typing import Optional
from UtilPatch import UtilPatch
from co.edu.uco.invook.applicationcore.domain.inventory.Hardware import Hardware
from co.edu.uco.invook.applicationcore.domain.inventory.HardwareAvailable import HardwareAvailable
from co.edu.uco.invook.applicationcore.domain.resource.Loan import Loan, LoanStatus
from co.edu.uco.invook.applicationcore.domain.resource.LoanStatus import LoanStatus
from co.edu.uco.invook.crosscutting.exception.impl.BusinessException import BusinessException, LoanAlreadyClosedException, LoanNotFoundException
from co.edu.uco.invook.crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from co.edu.uco.invook.crosscutting.util import UtilNumber, UtilText

class LoanService:
    @staticmethod
    def create_loan(self, count, rfidLender, idLender, idMonitor, serialHardware, loanDate, returnDate, status):
        try:
            rfidLender = UtilText.apply_trim(rfidLender)
            idLender = UtilText.apply_trim(idLender)
            idMonitor = UtilText.apply_trim(idMonitor)
            serialHardware = UtilText.apply_trim(serialHardware)
            count = UtilNumber.ensure_positive(count)
            
            loan = Loan.objects.create(
                _rfidLender = rfidLender,
                _idLender = idLender,
                _idMonitor = idMonitor,
                _serialHardware = serialHardware,
                _loanDate = loanDate,
                _returnDate = returnDate,
                _status = status
            )
            return loan
        except Exception as e:
            raise DatabaseOperationException("Error al crear el préstamo en la base de datos.") from e
    
    @staticmethod
    def close_loan(loan_id):
        try:
            loan = Loan.objects.get(id=loan_id)
            if loan._status == LoanStatus.CERRADO.value:
                raise LoanAlreadyClosedException(loan_id)

            loan._status = LoanStatus.CERRADO.value
            loan.save()
            return loan

        except Loan.DoesNotExist:
            raise LoanNotFoundException(loan_id)
        except LoanAlreadyClosedException:
            raise
        except Exception as e:
            raise DatabaseOperationException("Error al cerrar el préstamo en la base de datos.") from e
        

    @staticmethod
    def validate_loan_status(loan: Loan) -> bool:
        return loan.status == LoanStatus.ABIERTO.value

    @staticmethod
    def check_if_all_hardware_returned(loan: Loan) -> bool:
        hardwares = Hardware.objects.filter(loan = loan)
        return all(hw.available == HardwareAvailable.DISPONIBLE.value for hw in hardwares)
    
    @staticmethod
    def return_hardware(loan: Loan, serials_to_return: list[str]) -> Loan:
        try:
            if not LoanService.validate_loan_status(loan):
                raise LoanAlreadyClosedException(loan.id)
            
            hardwares = Hardware.objects.filter(loan = loan)
            hardwares_dict = {hw.serial: hw for hw in hardwares}

            invalid_serials = [serial for serial in serials_to_return if serial not in hardwares_dict]
            if invalid_serials:
                raise BusinessException(f"Los siguientes seriales no pertenecen al préstamo: {', '.join(invalid_serials)}")

            for serial in serials_to_return:
                hw = hardwares_dict[serial]
                hw.available = HardwareAvailable.DISPONIBLE.value
                hw.save()

            if LoanService.check_if_all_hardware_returned(loan):
                LoanService.close_loan(loan.id) 
                loan.returnDate = datetime.now()
                loan.save()

            return loan
        
        except Loan.DoesNotExist:
            raise LoanNotFoundException(loan.id)
        except LoanAlreadyClosedException:
            raise
        except Exception as e:
            raise DatabaseOperationException("Error al realizar la devolución parcial en la base de datos.") from e
    
    @staticmethod
    def get(id: int) -> Optional[Loan]:
        try:
            return Loan.objects.get(id = id)
        except Loan.DoesNotExist:
            return None
        except Exception as e:
            raise DatabaseOperationException("Error al consultar el préstamo en la base de datos.") from e
    
    @staticmethod
    def list_all() -> list[Loan]:
        try:
            return list(Loan.objects.all())
        except Exception as e:
            raise DatabaseOperationException("Error al listar los préstamos en la base de datos.") from e
    
    @staticmethod
    def patch_loan(id: int, **kwargs) -> Loan:
        try:
            loan = Loan.objects.get(id=id)
            return UtilPatch.patch_model(loan, kwargs)
        except Loan.DoesNotExist:
            raise LoanNotFoundException(id)
        except Exception as e:
            raise DatabaseOperationException("Error al realizar la actualización en el préstamo en la base de datos.") from e