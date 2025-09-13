from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .....applicationcore.domain.user.AdministrativeUser import AdministrativeUser


class LoginController(APIView):
    def post(self, request):
            username = request.data.get('username')
            password = request.data.get('password')
            try:
                user = AdministrativeUser.objects.get(username=username)
                if user.check_password(password):
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'access': str(refresh.access_token),
                        'refresh': str(refresh)
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({'detail': 'Contraseña incorrecta'}, status=status.HTTP_400_BAD_REQUEST)
            except AdministrativeUser.DoesNotExist:
                return Response({'detail': 'Usuario no encontrado'}, status=status.HTTP_400_BAD_REQUEST)