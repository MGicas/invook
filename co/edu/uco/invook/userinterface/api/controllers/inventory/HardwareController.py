from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .....applicationcore.facade.impl.InventoryFacadeImpl import InventoryFacadeImpl
from ...serializers.HardwareSerializer import HardwareSerializer

class HardwareController(APIView):
    facade = InventoryFacadeImpl()

    def get(self, request, serial=None):
        if serial:
            hw = self.facade.get_hardware(serial)
            serializer = HardwareSerializer(hw)
            return Response(serializer.data)
        else:
            all_hw = self.facade.list_all_hardwares()
            serializer = HardwareSerializer(all_hw, many=True)
            return Response(serializer.data)

    def post(self, request):
        hw = self.facade.create_hardware(**request.data)
        serializer = HardwareSerializer(hw)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, serial):
        action = request.data.get("action", None)

        if action == "t_a":
            hw = self.facade.toggle_availability(serial)
        else:
            hw = self.facade.patch_hardware(serial, request.data)

        serializer = HardwareSerializer(hw)
        return Response(serializer.data)

    def delete(self, request, serial):
        self.facade.delete_hardware(serial)
        return Response(status=status.HTTP_204_NO_CONTENT)
