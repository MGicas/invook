from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from co.edu.uco.invook.applicationcore.facade.impl.InventoryFacadeImpl import InventoryFacadeImpl
from co.edu.uco.invook.userinterface.api.serializers.HardwareSerializer import HardwareSerializer

class HardwareController(APIView):
    facade = InventoryFacadeImpl()

    def get(self, request, serial=None):
        if serial:
            hw = self.facade.get_hardware(serial)
            serializer = HardwareSerializer(hw)
            return Response(serializer.data)
        else:
            all_hw = self.facade.list_all_hardware()
            serializer = HardwareSerializer(all_hw, many=True)
            return Response(serializer.data)

    def post(self, request):
        hw = self.facade.create_hardware(**request.data)
        serializer = HardwareSerializer(hw)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, serial):
        hw = self.facade.patch_hardware(serial, **request.data)
        serializer = HardwareSerializer(hw)
        return Response(serializer.data)

    def delete(self, request, serial):
        self.facade.delete_hardware(serial)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Acciones especiales
    def post_mark_available(self, request, serial):
        hw = self.facade.mark_hardware_available(serial)
        serializer = HardwareSerializer(hw)
        return Response(serializer.data)

    def post_mark_unavailable(self, request, serial):
        hw = self.facade.mark_hardware_unavailable(serial)
        serializer = HardwareSerializer(hw)
        return Response(serializer.data)
