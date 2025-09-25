from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .....applicationcore.domain.inventory.Supply import Supply
from .....crosscutting.exception.impl.BusinessException import SupplyNotFoundException, DuplicateSupplyCodeException
from .....crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException

from .....applicationcore.facade.impl.InventoryFacadeImpl import InventoryFacadeImpl
from ...serializers.SupplySerializer import SupplySerializer

class SupplyController(APIView):
    facade = InventoryFacadeImpl()

    def get(self, request, code=None):
        try:
            if code:
                supply = self.facade.get_supply(code)
                serializer = SupplySerializer(supply)
                return Response(serializer.data)
            else:
                all_supplies = self.facade.list_all_supplies()
                serializer = SupplySerializer(all_supplies, many=True)
                return Response(serializer.data)
        except SupplyNotFoundException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            supply = self.facade.create_supply(**request.data)
            serializer = SupplySerializer(supply)
            return Response({"message": "Hardware creado correctamente", "hardware": serializer.data},
                            status=status.HTTP_201_CREATED
                            )
        except DuplicateSupplyCodeException as e:
            return Response(
                {"error": f"El hardware con serial '{e.args[0]}' ya existe."},
                status=status.HTTP_409_CONFLICT
            )
        except SupplyNotFoundException as e:
            return Response(
                {"error": f"Hardware type con id '{e.args[0]}' no encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )
        except DatabaseOperationException as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def patch(self, request, code):
        supply = self.facade.patch_supply(code, **request.data)
        serializer = SupplySerializer(supply)
        return Response(serializer.data)

    def delete(self, request, code):
        try:
            self.facade.delete_supply(code)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SupplyNotFoundException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
