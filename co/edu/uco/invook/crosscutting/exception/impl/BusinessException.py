from ....crosscutting.exception.ExceptionsBase import ExceptionsBase

#General exceptions
class DatabaseConnectionException(ExceptionsBase):
    def __init__(self, message: str):
        super().__init__(f"Database connection error: {message}")
        
class NegativeQuantityException(ExceptionsBase):
    def __init__(self, name: str, quantity: int):
        super().__init__(
            f"'{name}' cannot have negative quantity: {quantity}"
        )
        
class MissingFieldException(ExceptionsBase):
    def __init__(self, field: str):
        super().__init__(f"Field '{field}' is required")

#User exceptions
class UserNotFoundException(ExceptionsBase):
    def __init__(self, id: str):
        super().__init__(f"User with id '{id}' not found")
        
class AdministrativeUserNotFoundException(ExceptionsBase):
    """Se lanza cuando no se encuentra un admin user."""
    def __init__(self, admin_id: str):
        super().__init__(f"Administrative user with id '{admin_id}' not found")

class AdminPermissionDeniedException(ExceptionsBase):
    """Se lanza cuando un admin intenta realizar una acción sin permisos."""
    def __init__(self, action: str):
        super().__init__(f"Administrative user does not have permission to perform '{action}'")

class DuplicateAdminEmailException(ExceptionsBase):
    """Se lanza cuando se intenta registrar un admin con un correo ya existente."""
    def __init__(self, email: str):
        super().__init__(f"Administrative user with email '{email}' already exists")

class InvalidEmailException(ExceptionsBase):
    def __init__(self, email: str):
        super().__init__(f"The email '{email}' is not valid")
        
class DuplicateUsernameException(ExceptionsBase):
    def __init__(self, username: str):
        super().__init__(f"Username '{username}' is already taken")
        
class InvalidPasswordException(ExceptionsBase):
    def __init__(self, message: str = "La contraseña es incorrecta."):
        super().__init__(message)

#Lender exceptions
class LenderNotFoundException(ExceptionsBase):
    """Se lanza cuando no se encuentra un prestamista."""
    def __init__(self, lender_id: str):
        super().__init__(f"Lender with id '{lender_id}' not found")

class LenderHasActiveLoansException(ExceptionsBase):
    """Se lanza cuando se intenta eliminar un lender con préstamos activos."""
    def __init__(self, lender_id: str):
        super().__init__(f"Lender with id '{lender_id}' has active loans and cannot be deleted")

class DuplicateLenderException(ExceptionsBase):
    """Se lanza cuando ya existe un lender con el mismo identificador único (ej: email o doc)."""
    def __init__(self, identifier: str):
        super().__init__(f"Lender with identifier '{identifier}' already exists")

        
#HARDWARE EXCEPTIONS
class HardwareNotFoundException(ExceptionsBase):
    def __init__(self, serial: str):
        super().__init__(f"No hay ningun hardware con el serial {serial}")


class InvalidHardwareTypeException(ExceptionsBase):
    def __init__(self, hw_type: str):
        super().__init__(f"Hardware type '{hw_type}' is not valid")

class InvalidPatchFieldException(ExceptionsBase):
    def __init__(self, serial: str):
        super().__init__(serial)

class DuplicateSerialException(ExceptionsBase):
    def __init__(self, serial: str):
        super().__init__(serial)
        
#SUPPLY EXCEPTIONS
class SupplyNotFoundException(ExceptionsBase):
    def __init__(self, supply_id: str):
        super().__init__(f"Supply with id '{supply_id}' not found")

####!!!
class InsufficientSupplyQuantityException(ExceptionsBase):
    def __init__(self, name: str, requested: int, available: int):
        super().__init__(
            f"Not enough quantity for supply '{name}'. "
            f"Requested: {requested}, Available: {available}"
        )
        
class DuplicateSupplyCodeException(ExceptionsBase):
    def __init__(self, code: str):
        super().__init__(f"Supply with code '{code}' already exists")
        
#CONSUM EXCEPTIONS

class ConsumNotFoundException(ExceptionsBase):
    def __init__(self, id: str):
        super().__init__(f"Consum with id '{id}' not found")

###!!!!variable name
class InvalidConsumQuantityException(ExceptionsBase):
    def __init__(self, quantity: int):
        super().__init__(f"Consum quantity must be greater than zero. Received: {quantity}")


class ConsumExceedsSupplyException(ExceptionsBase):
    def __init__(self, supply_id: str, requested: int, available: int):
        super().__init__(
            f"Consum of supply '{supply_id}' exceeds available stock. "
            f"Requested: {requested}, Available: {available}"
        )


#LOAN EXCEPTIONS
class LoanNotFoundException(ExceptionsBase):
    def __init__(self, id: str):
        super().__init__(f"Loan with id '{id}' not found")


class HardwareUnavailableException(ExceptionsBase):
    def __init__(self, hardware_id: str):
        super().__init__(f"Hardware with id '{hardware_id}' is not available for loan")


class InvalidLoanPeriodException(ExceptionsBase):
    def __init__(self, loan_date, return_date):
        super().__init__(f"Invalid loan period: loan_date={loan_date}, return_date={return_date}")


class LoanAlreadyReturnedException(ExceptionsBase):
    def __init__(self, id: str):
        super().__init__(f"Loan with id '{id}' has already been returned")

class LoanAlreadyClosedException(ExceptionsBase):
    def __init__(self, id: str):
        super().__init__(f"Loan with id '{id}' is already closed")

class OverdueLoanException(ExceptionsBase):
    def __init__(self, id: str, due_date):
        super().__init__(f"Loan with id '{id}' is overdue since {due_date}")  

class BusinessException(ExceptionsBase):
    def __init__(self, message: str):
        super().__init__(f"Business error: {message}")      