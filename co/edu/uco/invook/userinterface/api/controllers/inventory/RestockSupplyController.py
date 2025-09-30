from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .....applicationcore.facade.impl.InventoryFacadeImpl import InventoryFacadeImpl
from ...serializers.RestockSupplySerializer import RestockSupplyInSerializer
from ...serializers.SupplySerializer import SupplySerializer

class RestockSupplyController(APIView):
    facade = InventoryFacadeImpl()

    def post(self, request, code: str):
        """
        POST /api/v1/inventory/supplies/{code}/restock
        body: { "count": int, "quantity": int }
        """
        in_ser = RestockSupplyInSerializer(data=request.data)
        if not in_ser.is_valid():
            return Response(in_ser.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            supply = self.facade.restock_supply(
                code=code,
                count=in_ser.validated_data["count"],
                quantity=in_ser.validated_data["quantity"],
            )
            return Response(SupplySerializer(supply).data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
