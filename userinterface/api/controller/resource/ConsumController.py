from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from co.edu.uco.invook.userinterface.api.serializers.ConsumSerializer import ConsumSerializer
from co.edu.uco.invook.applicationcore.facade.impl.ConsumFacade import ConsumFacade

class ConsumController(APIView):

    def get(self, request):
        consumptions = ConsumFacade.get_all()
        serializer = ConsumSerializer(consumptions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ConsumSerializer(data=request.data)
        if serializer.is_valid():
            new_consum = ConsumFacade.create(serializer.validated_data)
            return Response(ConsumSerializer(new_consum).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        consum_id = str(pk)
        ConsumFacade.delete(consum_id)
        return Response({'message': 'Consum deleted'}, status=status.HTTP_204_NO_CONTENT)
