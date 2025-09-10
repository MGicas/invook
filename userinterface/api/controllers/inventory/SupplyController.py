from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from co.edu.uco.invook.applicationcore.facade.impl.InventoryFacadeImpl import InventoryFacadeImpl
from co.edu.uco.invook.userinterface.api.serializers.SupplySerializer import SupplySerializer

class SupplyController(APIView):
    facade = InventoryFacadeImpl()

    def get(self, request, code=None):
        if code:
            supply = self.facade.get_supply(code)
            serializer = SupplySerializer(supply)
            return Response(serializer.data)
        else:
            all_supplies = self.facade.list_all_supplies()
            serializer = SupplySerializer(all_supplies, many=True)
            return Response(serializer.data)

    def post(self, request):
        supply = self.facade.create_supply(**request.data)
        serializer = SupplySerializer(supply)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, code):
        supply = self.facade.patch_supply(code, **request.data)
        serializer = SupplySerializer(supply)
        return Response(serializer.data)

    def delete(self, request, code):
        self.facade.delete_supply(code)
        return Response(status=status.HTTP_204_NO_CONTENT)
