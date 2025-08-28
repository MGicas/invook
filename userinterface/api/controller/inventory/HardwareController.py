# co/edu/uco/invook/userinterface/controller/hardware_controller.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from co.edu.uco.invook.userinterface.api.serializers.HardwareSerializer import HardwareSerializer
from co.edu.uco.invook.applicationcore.facade.impl.HardwareFacade import HardwareFacade

class HardwareController(APIView):

    def get(self, request):
        hardwares = HardwareFacade.get_all()
        serializer = HardwareSerializer(hardwares, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = HardwareSerializer(data=request.data)
        if serializer.is_valid():
            new_hardware = HardwareFacade.create(serializer.validated_data)
            return Response(HardwareSerializer(new_hardware).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        serial = str(pk)
        HardwareFacade.delete(serial)
        return Response({'message': 'Hardware deleted'}, status=status.HTTP_204_NO_CONTENT)
