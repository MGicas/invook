from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from ...serializers.AdminTokenObtainPairSerializer import AdminTokenObtainPairSerializer
from .....services.resource.LoanService import LoanService

class AdminTokenObtainPairController(TokenObtainPairView):
    serializer_class = AdminTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        # Proceder con la autenticación normal
        response = super().post(request, *args, **kwargs)
        
        # Llamar al servicio para enviar los correos de notificación
        LoanService.send_message_to_lenders()

        return response


class AdminTokenRefreshView(TokenRefreshView):
    pass

class WhoAmIController(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": getattr(user, "role", "UNKNOWN"),
            "state": getattr(user, "state", None),
        }
        if hasattr(user, "profile") and user.profile:
            data["profile"] = {
                "rfid": user.profile.rfid,
                "names": user.profile.names,
                "surnames": user.profile.surnames,
                "phone": user.profile.phone,
                "document_id": user.profile.document_id,
            }
        return Response(data)
