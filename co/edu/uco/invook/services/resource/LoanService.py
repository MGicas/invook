import datetime
from typing import Optional

from ...applicationcore.domain.resource.LoanHardware import LoanHardware
from ...applicationcore.domain.user.AdministrativeUser import AdministrativeUser
from ...applicationcore.domain.user.Lender import Lender
from ...crosscutting.util.UtilPatch import UtilPatch
from ...applicationcore.domain.inventory.Hardware import Hardware
from ...applicationcore.domain.inventory.HardwareAvailable import HardwareAvailable
from ...applicationcore.domain.resource.Loan import Loan, LoanStatus
from ...applicationcore.domain.resource.LoanStatus import LoanStatus
from ...crosscutting.exception.impl.BusinessException import BusinessException, LoanAlreadyClosedException, LoanNotFoundException
from ...crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from ...crosscutting.util.UtilText import UtilText

class LoanService:
    @staticmethod
    def create_loan(id_lender, id_monitor, serial_hardware, loan_date, return_date, status):
        try:
            lender = Lender.objects.get(id=lender)
            monitor = AdministrativeUser.objects.get(id=id_monitor)
            hardware = Hardware.objects.get(serial=serial_hardware)
            
            loan = Loan.objects.create(
                id_lender = lender,
                id_monitor = monitor,
                loan_date = loan_date,
                return_date = return_date,
                status = status
            )

            loan.save()

            LoanHardware.objects.create(
                loan=loan,
                hardware=hardware
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

            loan.status = LoanStatus.CERRADO.value
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
    def add_hardware_to_loan(loan_id: str, serialHardware: str) -> LoanHardware:
        try:
            loan = Loan.objects.get(id=loan_id)
            hardware = Hardware.objects.get(serial=serialHardware)

            loan_hardware, created = LoanHardware.objects.get_or_create(
                loan=loan,
                hardware=hardware
            )

            return loan_hardware

        except Loan.DoesNotExist:
            raise LoanNotFoundException(f"Préstamo con id {loan_id} no encontrado.")
        except Hardware.DoesNotExist:
            raise LoanNotFoundException(f"Hardware con serial {serialHardware} no encontrado.")
        except DatabaseOperationException as e:
            raise DatabaseOperationException("Error al asociar hardware con préstamo.") from e

    
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