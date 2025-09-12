
class TechnicalException(Exception):
    def __init__(self, message: str, *args):
        super().__init__(message, *args)
        self.message = message

    def __str__(self):
        return f"[TechnicalException] {self.message}"


class DatabaseOperationException(TechnicalException):
    def __init__(self, message: str = "Error en la operación de base de datos", *args):
        super().__init__(message, *args)

    def __str__(self):
        return f"[DatabaseOperationException] {self.message}"


class ConnectionException(TechnicalException):
    def __init__(self, message: str = "Error de conexión", *args):
        super().__init__(message, *args)

    def __str__(self):
        return f"[ConnectionException] {self.message}"


class ExternalServiceException(TechnicalException):
    def __init__(self, service_name: str, message: str = "Error en servicio externo", *args):
        super().__init__(f"{service_name}: {message}", *args)
        self.service_name = service_name

    def __str__(self):
        return f"[ExternalServiceException] {self.message}"


class FileStorageException(TechnicalException):
    def __init__(self, message: str = "Error en el sistema de archivos", *args):
        super().__init__(message, *args)

    def __str__(self):
        return f"[FileStorageException] {self.message}"


class ConfigurationException(TechnicalException):
    def __init__(self, message: str = "Error en la configuración del sistema", *args):
        super().__init__(message, *args)

    def __str__(self):
        return f"[ConfigurationException] {self.message}"
