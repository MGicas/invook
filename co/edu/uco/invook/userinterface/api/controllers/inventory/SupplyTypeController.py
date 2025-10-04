from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .....applicationcore.facade.impl.InventoryFacadeImpl import InventoryFacadeImpl
from ...serializers.SupplyTypeSerializer import SupplyTypeSerializer
from .....crosscutting.exception.impl.BusinessException import BusinessException
from .....crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException


class SupplyTypeController(APIView):
    facade = InventoryFacadeImpl()

    def get(self, request, id=None):
        try:
            if id:
                # Buscar por ID
                st = self.facade.get_supply_type(id)
                serializer = SupplyTypeSerializer(st)
                return Response(serializer.data)
            else:
                # Buscar por nombre si viene en query params
                name = request.query_params.get("name", None)
                if name:
                    all_types = self.facade.search_supply_types_by_name(name)
                else:
                    all_types = self.facade.list_all_supply_types()

                serializer = SupplyTypeSerializer(all_types, many=True)
                return Response(serializer.data)

        except BusinessException as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_404_NOT_FOUND
            )
        except DatabaseOperationException as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        try:
            supply_type = self.facade.create_supply_type(**request.data)
            serializer = SupplyTypeSerializer(supply_type)
            return Response(
                {"message": "SupplyType creado correctamente", "supply_type": serializer.data},
                status=status.HTTP_201_CREATED
            )
        except BusinessException as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except DatabaseOperationException as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def patch(self, request, id):
        try:
            supply_type = self.facade.patch_supply_type(id, **request.data)
            serializer = SupplyTypeSerializer(supply_type)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except BusinessException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except DatabaseOperationException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        """
        PUT usado para desactivar un SupplyType (cambiar active = False)
        """
        try:
            supply_type = self.facade.deactivate_supply_type(id)
            serializer = SupplyTypeSerializer(supply_type)
            return Response(
                {
                    "message": f"SupplyType '{id}' desactivado correctamente",
                    "supply_type": serializer.data
                },
                status=status.HTTP_200_OK
            )
        except BusinessException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except DatabaseOperationException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
