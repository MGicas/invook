from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ...serializers.LoginSerializer import LoginSerializer
from .....applicationcore.facade.impl.AuthFacade import AuthFacade
from .....applicationcore.usecase.impl.LoginUseCase import LoginUseCase
from .....services.user.AdministrativeUserService import AdministrativeUserService
from rest_framework.permissions import AllowAny

class LoginController(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        facade = AuthFacade(LoginUseCase(AdministrativeUserService()))
        try:
            data = facade.login(
                serializer.validated_data["username"],
                serializer.validated_data["password"]
            )
            return Response(data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
