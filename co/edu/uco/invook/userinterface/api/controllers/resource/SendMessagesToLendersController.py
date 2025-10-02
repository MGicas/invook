from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .....applicationcore.facade.impl.InventoryFacadeImpl import InventoryFacadeImpl

class SendMessagesToLendersController(APIView):

    def post(self, request):
        
        try:
            result_message = InventoryFacadeImpl.send_message_to_lenders()
            
            return Response(
                {"detail": "Proceso de notificaciones iniciado.", "status": result_message},
                status=status.HTTP_200_OK
            )
            
        except Exception as e:
            return Response(
                {"error": "Ocurrió un error al intentar enviar las notificaciones.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
