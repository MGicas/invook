from co.edu.uco.invook.crosscutting.exception import Exceptions

#General exceptions
class DatabaseConnectionException(Exceptions):
    def __init__(self, message: str):
        super().__init__(f"Database connection error: {message}")
        
class NegativeQuantityException(Exceptions):
    def __init__(self, name: str, quantity: int):
        super().__init__(
            f"'{name}' cannot have negative quantity: {quantity}"
        )
        
class MissingFieldException(Exceptions):
    def __init__(self, field: str):
        super().__init__(f"Field '{field}' is required")

#User exceptions
class UserNotFoundException(Exceptions):
    def __init__(self, id: str):
        super().__init__(f"User with id '{id}' not found")
        
class AdministrativeUserNotFoundException(Exceptions):
    """Se lanza cuando no se encuentra un admin user."""
    def __init__(self, admin_id: str):
        super().__init__(f"Administrative user with id '{admin_id}' not found")

class AdminPermissionDeniedException(Exceptions):
    """Se lanza cuando un admin intenta realizar una acción sin permisos."""
    def __init__(self, action: str):
        super().__init__(f"Administrative user does not have permission to perform '{action}'")

class DuplicateAdminEmailException(Exceptions):
    """Se lanza cuando se intenta registrar un admin con un correo ya existente."""
    def __init__(self, email: str):
        super().__init__(f"Administrative user with email '{email}' already exists")

class InvalidEmailException(Exceptions):
    def __init__(self, email: str):
        super().__init__(f"The email '{email}' is not valid")
        
class DuplicateUsernameException(Exceptions):
    def __init__(self, username: str):
        super().__init__(f"Username '{username}' is already taken")

#Lender exceptions
class LenderNotFoundException(Exceptions):
    """Se lanza cuando no se encuentra un prestamista."""
    def __init__(self, lender_id: str):
        super().__init__(f"Lender with id '{lender_id}' not found")

class LenderHasActiveLoansException(Exceptions):
    """Se lanza cuando se intenta eliminar un lender con préstamos activos."""
    def __init__(self, lender_id: str):
        super().__init__(f"Lender with id '{lender_id}' has active loans and cannot be deleted")

class DuplicateLenderException(Exceptions):
    """Se lanza cuando ya existe un lender con el mismo identificador único (ej: email o doc)."""
    def __init__(self, identifier: str):
        super().__init__(f"Lender with identifier '{identifier}' already exists")

        
#HARDWARE EXCEPTIONS
class HardwareNotFoundException(Exceptions):
    def __init__(self, serial: str):
        super().__init__(f"Hardware with serial '{serial}' not found")


class InvalidHardwareTypeException(Exceptions):
    def __init__(self, hw_type: str):
        super().__init__(f"Hardware type '{hw_type}' is not valid")


class DuplicateSerialException(Exceptions):
    def __init__(self, serial: str):
        super().__init__(f"Hardware with serial '{serial}' already exists")
        
#SUPPLY EXCEPTIONS
class SupplyNotFoundException(Exceptions):
    def __init__(self, supply_id: str):
        super().__init__(f"Supply with id '{supply_id}' not found")

####!!!
class InsufficientSupplyQuantityException(Exceptions):
    def __init__(self, name: str, requested: int, available: int):
        super().__init__(
            f"Not enough quantity for supply '{name}'. "
            f"Requested: {requested}, Available: {available}"
        )
        
class DuplicateSupplyCodeException(Exceptions):
    def __init__(self, code: str):
        super().__init__(f"Supply with code '{code}' already exists")
        
#CONSUM EXCEPTIONS

class ConsumNotFoundException(Exceptions):
    def __init__(self, id: str):
        super().__init__(f"Consum with id '{id}' not found")

###!!!!variable name
class InvalidConsumQuantityException(Exceptions):
    def __init__(self, quantity: int):
        super().__init__(f"Consum quantity must be greater than zero. Received: {quantity}")


class ConsumExceedsSupplyException(Exceptions):
    def __init__(self, supply_id: str, requested: int, available: int):
        super().__init__(
            f"Consum of supply '{supply_id}' exceeds available stock. "
            f"Requested: {requested}, Available: {available}"
        )


#LOAN EXCEPTIONS
class LoanNotFoundException(Exceptions):
    def __init__(self, id: str):
        super().__init__(f"Loan with id '{id}' not found")


class HardwareUnavailableException(Exceptions):
    def __init__(self, hardware_id: str):
        super().__init__(f"Hardware with id '{hardware_id}' is not available for loan")


class InvalidLoanPeriodException(Exceptions):
    def __init__(self, loan_date, return_date):
        super().__init__(f"Invalid loan period: loan_date={loan_date}, return_date={return_date}")


class LoanAlreadyReturnedException(Exceptions):
    def __init__(self, id: str):
        super().__init__(f"Loan with id '{id}' has already been returned")


class OverdueLoanException(Exceptions):
    def __init__(self, id: str, due_date):
        super().__init__(f"Loan with id '{id}' is overdue since {due_date}")  

class BusinessException(Exceptions):
    def __init__(self, message: str):
        super().__init__(f"Business error: {message}")      