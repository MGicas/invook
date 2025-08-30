from co.edu.uco.invook.applicationcore.domain.user import User

class Lender(User):
    def __str__(self):
        return f"Lender: {self.names} {self.surnames} ({self.phone_number})"
