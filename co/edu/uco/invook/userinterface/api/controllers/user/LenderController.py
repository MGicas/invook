from .....applicationcore.facade.impl.UserFacadeImpl import UserFacadeImpl
from ...serializers.LenderSerializer import LenderSerializer
from .....crosscutting.exception.impl.BusinessException import LenderNotFoundException
from .....crosscutting.util.UtilText import UtilText
from .....crosscutting.exception.impl.BusinessException import BusinessException
from .....crosscutting.exception.impl.BusinessException import InvalidEmailException
from .....crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException
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
        try:
            lender = self.facade.create_lender(**request.data)
            serializer = LenderSerializer(lender)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except BusinessException as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

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
        except InvalidEmailException as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except BusinessException as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except DatabaseOperationException as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"detail": "Error inesperado: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            lender = self.facade.get_lender(id)
            if not lender:
                return Response({"detail": f"Lender con id '{id}' no existe."},
                                status=status.HTTP_404_NOT_FOUND)

            if lender.active is False:
                return Response({"detail": "El Lender ya está inactivo."},
                                status=status.HTTP_400_BAD_REQUEST)

            lender = self.facade.change_lender_state(id, active=False)
            serializer = LenderSerializer(lender)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except LenderNotFoundException as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except BusinessException as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except DatabaseOperationException as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"detail": f"Error inesperado: {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, id):
        try:
            lender = self.facade.get_lender(id)
            if not lender:
                return Response({"detail": f"Lender con id '{id}' no existe."}, status=status.HTTP_404_NOT_FOUND)

            self.facade.delete_lender(id)
            return Response(status=status.HTTP_204_NO_CONTENT)

        except BusinessException as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except LenderNotFoundException as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)

