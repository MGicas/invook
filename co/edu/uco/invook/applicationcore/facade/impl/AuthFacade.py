from rest_framework_simplejwt.tokens import RefreshToken

class AuthFacade:
    def __init__(self, login_usecase):
        self.login_usecase = login_usecase

    def login(self, username, password):
        user = self.login_usecase.execute(username, password)
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "username": user.username,
                "role": user.role,
                "state": user.state
            }
        }
