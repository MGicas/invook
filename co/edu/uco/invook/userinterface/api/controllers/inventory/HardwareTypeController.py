from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .....applicationcore.facade.impl.InventoryFacadeImpl import InventoryFacadeImpl
from ...serializers.HardwareTypeSerializer import HardwareTypeSerializer
from .....crosscutting.exception.impl.BusinessException import BusinessException
from .....crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException


class HardwareTypeController(APIView):
    facade = InventoryFacadeImpl()

    def get(self, request, id=None):
        try:
            if id:
                # Buscar por ID
                ht = self.facade.get_hardware_type(id)
                serializer = HardwareTypeSerializer(ht)
                return Response(serializer.data)
            else:
                # Buscar por nombre si viene en query params
                name = request.query_params.get("name", None)
                if name:
                    all_types = self.facade.search_hardware_types_by_name(name)
                else:
                    all_types = self.facade.list_all_hardware_types()

                serializer = HardwareTypeSerializer(all_types, many=True)
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
            hardware_type = self.facade.create_hardware_type(**request.data)
            serializer = HardwareTypeSerializer(hardware_type)
            return Response(
                {"message": "HardwareType creado correctamente", "hardware_type": serializer.data},
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
            hardware_type = self.facade.patch_hardware_type(id, **request.data)
            serializer = HardwareTypeSerializer(hardware_type)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except BusinessException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except DatabaseOperationException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            hardware_type = self.facade.deactivate_hardware_type(id)
            serializer = HardwareTypeSerializer(hardware_type)
            return Response(
                {
                    "message": f"HardwareType '{id}' desactivado correctamente",
                    "hardware_type": serializer.data
                },
                status=status.HTTP_200_OK
            )
        except BusinessException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except DatabaseOperationException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)