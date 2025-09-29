from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import update_session_auth_hash
from ...serializers.ChangePasswordSerializer import ChangePasswordSerializer

class ChangeOwnPasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        ser = ChangePasswordSerializer(data=request.data)
        ser.is_valid(raise_exception=True)

        user = request.user
        if not user.check_password(ser.validated_data["old_password"]):
            return Response({"old_password": "Contraseña actual incorrecta."}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(ser.validated_data["new_password"])
        user.save()

        update_session_auth_hash(request, user)

        return Response({"detail": "Contraseña actualizada exitosamente."}, status=status.HTTP_200_OK)
