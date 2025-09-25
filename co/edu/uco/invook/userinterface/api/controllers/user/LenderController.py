from .....applicationcore.facade.impl.UserFacadeImpl import UserFacadeImpl
from ...serializers.LenderSerializer import LenderSerializer
from .....crosscutting.exception.impl.BusinessException import LenderNotFoundException
from .....crosscutting.util.UtilText import UtilText
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class LenderController(APIView):
    facade = UserFacadeImpl()

    def get(self, request, id=None):
        if id:
            lender = self.facade.get_lender(id)
            if lender:
                serializer = LenderSerializer(lender)
                return Response(serializer.data)
            else:
                return Response(
                    {"detail": f"Lender con id '{id}' no existe."},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            lenders = self.facade.list_all_lenders()
            serializer = LenderSerializer(lenders, many=True)
            return Response(serializer.data, status= status.HTTP_200_OK)

    def post(self, request):
        lender = self.facade.create_lender(**request.data)
        serializer = LenderSerializer(lender)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, id):
        email = request.data.get('email')
        if email and not UtilText.email_string_is_valid(email):
            return Response(
                {"detail": "El formato del correo electrónico es inválido."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if not id:
            return Response(
                {"detail": "Se requiere un id para actualizar el recurso."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if 'id' in request.data:
            return Response(
                {"detail": "No se puede cambiar el ID de un Lender."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            lender = self.facade.patch_lender(id, **request.data)
            serializer = LenderSerializer(lender)
            return Response(serializer.data)
        except LenderNotFoundException as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            self.facade.delete_lender(id)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except LenderNotFoundException as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)