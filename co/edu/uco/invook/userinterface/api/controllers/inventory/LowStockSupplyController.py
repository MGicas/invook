from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .....applicationcore.facade.impl.InventoryFacadeImpl import InventoryFacadeImpl
from ...serializers.SupplySerializer import SupplySerializer
from .....crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException

class LowStockSupplyController(APIView):
    facade = InventoryFacadeImpl()

    def get(self, request):
        threshold = request.query_params.get("threshold", 10)
        try:
            threshold = int(threshold)
        except ValueError:
            return Response(
                {"error": "El parámetro 'threshold' debe ser un número entero."},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            supplies = self.facade.list_low_stock_supplies(threshold)
            print("SUPPLIES:", list(supplies))
            serializer = SupplySerializer(supplies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DatabaseOperationException as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )