from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from co.edu.uco.invook.userinterface.api.serializers.AdministrativeUserSerializer import AdministrativeUserSerializer
from co.edu.uco.invook.applicationcore.facade.impl.AdministrativeUserFacade import AdministrativeUserFacade

class AdministrativeUserController(APIView):

    def get(self, request):
        admin_users = AdministrativeUserFacade.get_all()
        serializer = AdministrativeUserSerializer(admin_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AdministrativeUserSerializer(data=request.data)
        if serializer.is_valid():
            new_admin = AdministrativeUserFacade.create(serializer.validated_data)
            return Response(AdministrativeUserSerializer(new_admin).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        admin_id = str(pk)
        AdministrativeUserFacade.delete(admin_id)
        return Response({'message': 'Administrative User deleted'}, status=status.HTTP_204_NO_CONTENT)
