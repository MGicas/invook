class UtilNumber:
    ZERO: int = 0
    ZERO_FLOAT: float = 0.0

    def __new__(cls):
        raise TypeError("Esta clase no puede ser instanciada.")
