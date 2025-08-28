from User import User

class Lender(User):
    def __init__(self, id: str, rfid: str, names: str, surnames: str, email: str, phone: str):
        super().__init__(id, rfid, names, surnames, email, phone)

    @classmethod
    def build(cls, id: str, rfid: str, names: str, surnames: str, email: str, phone: str):
        return cls(id, rfid, names, surnames, email, phone)

    @classmethod
    def build_dummy(cls):
        return cls(
            id = "",
            rfid = "",
            names = "",
            surnames = "",
            email = "",
            phone = ""
        )
