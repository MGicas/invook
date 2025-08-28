# co/edu/uco/invook/userinterface/controller/supply_controller.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from co.edu.uco.invook.userinterface.api.serializers.SupplySerializer import SupplySerializer
from co.edu.uco.invook.applicationcore.facade.impl.SupplyFacade import SupplyFacade

class SupplyController(APIView):

    def get(self, request):
        supplies = SupplyFacade.get_all()
        serializer = SupplySerializer(supplies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SupplySerializer(data=request.data)
        if serializer.is_valid():
            new_supply = SupplyFacade.create(serializer.validated_data)
            return Response(SupplySerializer(new_supply).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        supply_id = str(pk)
        SupplyFacade.delete(supply_id)
        return Response({'message': 'Supply deleted'}, status=status.HTTP_204_NO_CONTENT)
