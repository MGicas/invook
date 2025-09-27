from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .....applicationcore.facade.impl.InventoryFacadeImpl import InventoryFacadeImpl
from ...serializers.HardwareSerializer import HardwareSerializer
from .....crosscutting.exception.impl.BusinessException import DuplicateSerialException, HardwareNotFoundException, InvalidPatchFieldException
from .....crosscutting.exception.impl.TechnicalExceptions import DatabaseOperationException


class HardwareController(APIView):
    facade = InventoryFacadeImpl()

    def get(self, request, serial=None):
        try:
            if serial:
                hw = self.facade.get_hardware(serial)
                serializer = HardwareSerializer(hw)
                return Response(serializer.data)
            else:                
                hardware_type = request.query_params.get("hardware_type", None)
                if hardware_type:
                    all_hw = self.facade.list_hardwares_by_type(hardware_type)
                    
                else:
                    all_hw = self.facade.list_all_hardwares()
                    
                serializer = HardwareSerializer(all_hw, many=True)
                return Response(serializer.data)
        except HardwareNotFoundException as e:
            return Response(
                {"error": f"Hardware type con id '{e.args[0]}' no encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )
        except DatabaseOperationException as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        try:
            hardware = self.facade.create_hardware(**request.data)
            serializer = HardwareSerializer(hardware)
            return Response(
                {"message": "Hardware creado correctamente", "hardware": serializer.data},
                status=status.HTTP_201_CREATED
            )
        except DuplicateSerialException as e:
            return Response(
                {"error": f"El hardware con serial '{e.args[0]}' ya existe."},
                status=status.HTTP_409_CONFLICT
            )
        except HardwareNotFoundException as e:
            return Response(
                {"error": f"Hardware type con id '{e.args[0]}' no encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )
        except DatabaseOperationException as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def patch(self, request, serial):
        try:
            action = request.data.get("action", None)

            if action == "t_a":
                hw = self.facade.toggle_availability(serial)
            else:
                data = request.data.copy()
                if "serial" in data:
                    raise InvalidPatchFieldException("No está permitido modificar el serial del hardware")
                hw = self.facade.patch_hardware(serial, **request.data)

            serializer = HardwareSerializer(hw)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except InvalidPatchFieldException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except HardwareNotFoundException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except DatabaseOperationException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

    def delete(self, request, serial):
        try:
            self.facade.delete_hardware(serial)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except HardwareNotFoundException as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
