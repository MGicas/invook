import logging
from django.db import transaction
from typing import Optional
from django.utils import timezone

logger = logging.getLogger(__name__)

from ...applicationcore.domain.resource.LoanHardware import LoanHardware
from ...applicationcore.domain.user.AdministrativeUser import AdministrativeUser
from ...applicationcore.domain.user.Lender import Lender
from ...crosscutting.util.UtilPatch import UtilPatch
from ...applicationcore.domain.inventory.Hardware import Hardware
from ...applicationcore.domain.inventory.HardwareAvailable import HardwareAvailable
from ...applicationcore.domain.inventory.HardwareState import HardwareState
from ...applicationcore.domain.resource.Loan import Loan
from ...applicationcore.domain.resource.LoanStatus import LoanStatus
from ...crosscutting.exception.impl.BusinessException import BusinessException, LoanAlreadyClosedException, LoanNotFoundException
from ...crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
from ...crosscutting.exception.impl.BusinessException import HardwareNotFoundException, LenderNotFoundException, AdministrativeUserNotFoundException

class LoanService:

    @staticmethod
    def _attach_hardware(loan: Loan, serial: str) -> LoanHardware:
        try:
            hardware = Hardware.objects.get(serial=serial)
        except Hardware.DoesNotExist:
            raise HardwareNotFoundException(f"Hardware con serial {serial} no encontrado.")

        if hardware.available == HardwareAvailable.NO_DISPONIBLE.value:
            raise BusinessException(f"El hardware con serial {serial} no está disponible para préstamo.")

        loan_hardware, created = LoanHardware.objects.get_or_create(
            loan=loan,
            hardware=hardware
        )
        if not created:
            raise BusinessException(f"El hardware con serial {serial} ya está asociado a este préstamo.")

        hardware.available = HardwareAvailable.NO_DISPONIBLE.value
        hardware.save()

        return loan_hardware

    @staticmethod
    def _detach_hardware(hardware: Hardware) -> None:
        hardware.available = HardwareAvailable.DISPONIBLE.value
        hardware.save()

    @staticmethod
    @transaction.atomic
    def create_loan(id_lender, id_monitor, serials_hardware, status=None):
        try:
            lender = Lender.objects.get(id=id_lender)
            monitor = AdministrativeUser.objects.get(id=id_monitor)
            
            loan = Loan.objects.create(
                id_lender = lender,
                id_monitor = monitor,
                status = status or LoanStatus.ABIERTO.value
            )

            for serial in serials_hardware:
                LoanService._attach_hardware(loan, serial)
        
            return loan
        
        except Lender.DoesNotExist:
            raise LenderNotFoundException(f"Lender con id {id_lender} no encontrado.")
        except AdministrativeUser.DoesNotExist:
            raise AdministrativeUserNotFoundException(f"Monitor con id {id_monitor} no encontrado.")
        except Exception as e:
            raise DatabaseOperationException("Error al crear el préstamo en la base de datos.") from e
        
    @staticmethod
    @transaction.atomic
    def close_loan(id: str) -> Loan:
        try:
            loan = Loan.objects.get(id=id)
            if loan.status == LoanStatus.CERRADO.value:
                raise LoanAlreadyClosedException(id)

            for lh in LoanHardware.objects.filter(loan=loan):
                LoanService._detach_hardware(lh.hardware)

            loan.status = LoanStatus.CERRADO.value
            loan.return_date = timezone.now()
            loan.save()
            return loan

        except Loan.DoesNotExist:
            raise LoanNotFoundException(id)
        except Exception as e:
            raise DatabaseOperationException("Error al cerrar el préstamo en la base de datos.") from e

    @staticmethod
    def validate_loan_status(loan: Loan) -> bool:
        return loan.status == LoanStatus.ABIERTO.value

    @staticmethod
    def check_if_all_hardware_returned(loan: Loan) -> bool:
        loan_hardwares = LoanHardware.objects.filter(loan=loan)
        return all(lh.returned_at is not None for lh in loan_hardwares)
     
    @staticmethod
    @transaction.atomic
    def return_hardware(loan: Loan, hardware_returns: list[dict]) -> Loan:
        try:
            if not LoanService.validate_loan_status(loan):
                raise LoanAlreadyClosedException(loan.id)

            loan_hardwares = {lh.hardware.serial: lh for lh in LoanHardware.objects.filter(loan=loan)}

            logger.debug(f"Loan ID: {loan.id}, Loan Hardwares: {loan_hardwares}")

            invalid_serials = [hr["serial"] for hr in hardware_returns if hr["serial"] not in loan_hardwares]
            if invalid_serials:
                raise BusinessException(f"Los siguientes seriales no pertenecen al préstamo: {', '.join(invalid_serials)}")

            for hr in hardware_returns:
                serial = hr["serial"]
                state = hr.get("state")

                if not state or state not in HardwareState.__members__:
                    raise BusinessException(f"Estado inválido para el hardware {serial}: {state}")

                lh = loan_hardwares[serial]
                lh.returned_at = timezone.localtime(timezone.now())
                lh.return_state = state
                lh.save()

                hw = lh.hardware
                hw.available = HardwareAvailable.DISPONIBLE.value
                hw.state = state
                hw.save()

            if LoanService.check_if_all_hardware_returned(loan):
                loan.status = LoanStatus.CERRADO.value
                loan.return_date = timezone.localtime(timezone.now())
                loan.save()

            return loan

        except Loan.DoesNotExist:
            raise LoanNotFoundException(loan.id)
        except LoanAlreadyClosedException:
            raise
        except BusinessException:
            raise
        except Exception as e:
            raise DatabaseOperationException("Error al realizar la devolución parcial en la base de datos.") from e

    @staticmethod
    def add_hardware_to_loan(id: str, serials_hardware: list[str]) -> Loan:
        try:
            loan = Loan.objects.get(id=id)
            if not LoanService.validate_loan_status(loan):
                raise LoanAlreadyClosedException(loan.id)

            for serial in serials_hardware:
                LoanService._attach_hardware(loan, serial)

            return loan

        except Loan.DoesNotExist:
            raise LoanNotFoundException(f"Préstamo con id {id} no encontrado.")
        except Exception as e:
            raise DatabaseOperationException("Error al asociar hardware con préstamo.") from e

    @staticmethod
    def get(id: str) -> Optional[Loan]:
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
    def patch_loan(id: str, **kwargs) -> Loan:
        try:
            loan = Loan.objects.get(id=id)
            return UtilPatch.patch_model(loan, kwargs)
        except Loan.DoesNotExist:
            raise LoanNotFoundException(f"Préstamo con id {id} no encontrado.")
        except Exception as e:
            raise DatabaseOperationException("Error al realizar la actualización en el préstamo en la base de datos.") from e