from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .....crosscutting.exception.impl.BusinessException import BusinessException, LoanAlreadyClosedException, MissingFieldException
from .....crosscutting.exception.impl.BusinessException import LoanNotFoundException
from .....applicationcore.facade.impl.InventoryFacadeImpl import InventoryFacadeImpl
from ...serializers.LoanSerializer import LoanSerializer

class LoanController(APIView):
    facade = InventoryFacadeImpl()

    def get(self, request, id=None):
        if id:
            try:
                loan = self.facade.get_loan(id)
                serializer = LoanSerializer(loan)
                return Response(serializer.data)
            except LoanNotFoundException as e:
                return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        else:
            all_loans = self.facade.list_all_loans()
            serializer = LoanSerializer(all_loans, many=True)
            return Response(serializer.data)

    def post(self, request, id: str = None):
        action = request.data.get("action")

        try:
            if action == "create":
                id_lender = request.data.get("id_lender")
                id_monitor = request.data.get("id_monitor")
                serials_hardware = request.data.get("serials_hardware", [])
                status_value = request.data.get("status")
                loan = self.facade.create_loan(id_lender, id_monitor, serials_hardware, status_value)
                return Response({"message": "Préstamo creado exitosamente", "loan_id": str(loan.id)}, status=status.HTTP_201_CREATED)

            elif action == "add_hardware":
                if not id:
                    return Response({"error": "Se requiere el parámetro 'id' en la URL para añadir hardware"}, status=status.HTTP_400_BAD_REQUEST)
                serials_hardware = request.data.get("serials_hardware", [])
                loan = self.facade.add_hardware_to_loan(id, serials_hardware)
                return Response({"message": f"Hardware agregado al préstamo {id}."}, status=status.HTTP_200_OK)

            elif action == "return_hardware":
                if not id:
                    return Response({"error": "Se requiere el parámetro 'id' en la URL para devolver hardware"}, status=status.HTTP_400_BAD_REQUEST)
                serials_to_return = request.data.get("serials_hardware", [])
                loan = self.facade.return_hardware_from_loan(id, serials_to_return)
                return Response({"message": f"Hardware devuelto en préstamo {id}."}, status=status.HTTP_200_OK)

            elif action == "close_loan":
                if not id:
                    return Response({"error": "Se requiere el parámetro 'id' en la URL para cerrar el préstamo"}, status=status.HTTP_400_BAD_REQUEST)
                loan = self.facade.close_loan(id)
                return Response({"message": f"Préstamo con id {id} cerrado exitosamente."}, status=status.HTTP_200_OK)

            else:
                return Response({"error": "Acción no válida o no especificada."}, status=status.HTTP_400_BAD_REQUEST)

        except MissingFieldException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except LoanNotFoundException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except LoanAlreadyClosedException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except BusinessException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Error interno del servidor", "detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, id):
        data = request.data.copy()
        if 'id' in data:
            return Response(
                {"detail": "No se puede cambiar el ID de un Préstamo."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            loan = self.facade.patch_loan(id, **data)
            serializer = LoanSerializer(loan)
            return Response(serializer.data)
        except LoanNotFoundException as e:
            return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        except BusinessException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Error interno del servidor'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
