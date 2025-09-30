from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .....applicationcore.facade.impl.InventoryFacadeImpl import InventoryFacadeImpl
from ...serializers.SupplySerializer import SupplySerializer

class LowStockSupplyController(APIView):
    facade = InventoryFacadeImpl()

    def get(self, request):
        threshold = int(request.query_params.get("threshold", 20))
        supplies = self.facade.list_low_stock_supplies(threshold)
        serializer = SupplySerializer(supplies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)