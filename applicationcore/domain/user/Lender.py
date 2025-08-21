from User import User

class Lender(User):
    def __init__(self, id: str, name: str, email: str, phone: str, address: str):
        super().__init__(id, name, email, phone, address)
    
    @classmethod
    def build(cls, id: str, name: str, email: str, phone: str, address: str):
        return cls(id, name, email, phone, address)
    
    @classmethod
    def build_dummy(cls):
        return cls(
            id = "",
            name = "",
            email = "",
            phone = "",
            address = ""
        )
