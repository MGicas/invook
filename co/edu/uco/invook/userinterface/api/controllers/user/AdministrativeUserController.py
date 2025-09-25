from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .....crosscutting.util.UtilText import UtilText
from .....crosscutting.exception.impl.BusinessException import AdministrativeUserNotFoundException
from .....crosscutting.exception.impl.BusinessException import InvalidPasswordException
from .....applicationcore.facade.impl.UserFacadeImpl import UserFacadeImpl
from ...serializers.AdministrativeUserSerializer import AdministrativeUserSerializer

class AdministrativeUserController(APIView):
    facade = UserFacadeImpl()

    def get(self, request, username=None):
        if username:
            user = self.facade.get_administrative_user(username)
            if user:
                serializer = AdministrativeUserSerializer(user)
                return Response(serializer.data)
            else:
                return Response(
                    {"detail": f"Administrador con username '{username}' no existe."},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            users = self.facade.list_all_administrative_users()
            serializer = AdministrativeUserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        email = request.data.get('email')
        if email and not UtilText.email_string_is_valid(email):
            return Response(
                {"detail": "El formato del correo electrónico es inválido."},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            user = self.facade.create_administrative_user(**request.data)
            serializer = AdministrativeUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, username = None):
        email = request.data.get('email')
        if email and not UtilText.email_string_is_valid(email):
            return Response(
                {"detail": "El formato del correo electrónico es inválido."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if not username:
            return Response(
                {"detail": "Se requiere un username para actualizar el recurso."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        
        if old_password and new_password:
            try:
                user = self.facade.change_password(username, old_password, new_password)
                serializer = AdministrativeUserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except AdministrativeUserNotFoundException as e:
                return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)
            except InvalidPasswordException as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        if 'id' in request.data:
            return Response(
                {"detail": "No se puede cambiar el ID de un Administrative user."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if 'username' in request.data and request.data['username'] != username:
            return Response(
                {"detail": "No se puede cambiar el username de un usuario administrativo."},
                status=status.HTTP_400_BAD_REQUEST
            )
                
        try:
            user = self.facade.patch_administrative_user(username, **request.data)
            serializer = AdministrativeUserSerializer(user)
            return Response(serializer.data)
        except AdministrativeUserNotFoundException as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, username):
        try:
            self.facade.delete_administrative_user(username)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AdministrativeUserNotFoundException as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)
        