class LoginUseCase:
    def __init__(self, user_service):
        self.user_service = user_service

    def execute(self, username, password):
        user = self.user_service.authenticate(username, password)
        if not user:
            raise ValueError("Credenciales inválidas o usuario inactivo")
        return user
