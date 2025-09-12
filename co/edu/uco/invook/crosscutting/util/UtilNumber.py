class UtilNumber:
    ZERO: int = 0
    ZERO_FLOAT: float = 0.0

    def __new__(cls):
        raise TypeError("Esta clase no puede ser instanciada.")
    
    @staticmethod
    def ensure_positive(number: int) -> int:
        if number < 0:
            raise ValueError("Number must be positive")
