from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from co.edu.uco.invook.userinterface.api.serializers.UserSerializer import UserSerializer
from co.edu.uco.invook.applicationcore.facade.impl.UserFacade import UserFacade

class UserController(APIView):

    def get(self, request):
        users = UserFacade.get_all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = UserFacade.create(serializer.validated_data)
            return Response(UserSerializer(new_user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        user_id = str(pk)
        UserFacade.delete(user_id)
        return Response({'message': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)


