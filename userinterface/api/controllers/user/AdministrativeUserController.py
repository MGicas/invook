from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from co.edu.uco.invook.applicationcore.facade.impl.UserFacadeImpl import UserFacadeImpl
from co.edu.uco.invook.userinterface.api.serializers.AdministrativeUserSerializer import AdministrativeUserSerializer

class AdministrativeUserController(APIView):
    facade = UserFacadeImpl()

    def get(self, request, user_id=None):
        if user_id:
            user = self.facade.get_admin_user(user_id)
            serializer = AdministrativeUserSerializer(user)
            return Response(serializer.data)
        else:
            users = self.facade.list_all_admin_users()
            serializer = AdministrativeUserSerializer(users, many=True)
            return Response(serializer.data)

    def post(self, request):
        user = self.facade.create_admin_user(**request.data)
        serializer = AdministrativeUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, user_id):
        user = self.facade.patch_admin_user(user_id, **request.data)
        serializer = AdministrativeUserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, user_id):
        self.facade.delete_admin_user(user_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
