import re
from .UtilObject import UtilObject


class UtilText:
    EMPTY = ""
    UNDERLINE = "_"
    EMAIL_RE = r'^[_A-Za-z0-9\-+]+(\.[_A-Za-z0-9\-]+)*@[A-Za-z0-9\-]+(\.[A-Za-z0-9]+)*(\.[A-Za-z]{2,})$'
    PASSWORD_PATTERN = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    @staticmethod
    def is_null(string: str) -> bool:
        return UtilObject().is_null(string)

    @staticmethod
    def is_null_or_empty(string: str) -> bool:
        return UtilText.is_null(string) or UtilText.EMPTY == UtilText.apply_trim(string)

    @staticmethod
    def apply_trim(string: str) -> str:
        return UtilText.get_default(string).strip()

    @staticmethod
    def get_default(string: str, default_value: str = EMPTY) -> str:
        return UtilObject().get_default(string, default_value)

    @staticmethod
    def concatenate(*strings: str) -> str:
        if UtilObject().is_null(strings):
            return UtilText.EMPTY
        return ''.join([UtilText.apply_trim(s) for s in strings])

    @staticmethod
    def match_pattern(text: str, pattern: str) -> bool:
        return bool(re.fullmatch(UtilText.get_default(pattern), UtilText.get_default(text)))

    @staticmethod
    def email_string_is_valid(email: str) -> bool:
        return UtilText.match_pattern(email, UtilText.EMAIL_RE)

    @staticmethod
    def is_password_valid(password: str) -> bool:
        return UtilText.match_pattern(password, UtilText.PASSWORD_PATTERN)
