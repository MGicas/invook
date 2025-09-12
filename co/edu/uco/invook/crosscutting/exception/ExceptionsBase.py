class ExceptionsBase(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        
class NotFoundException(Exception):
    pass

class ConflictException(Exception):
    pass

class BadRequestException(Exception):
    pass
