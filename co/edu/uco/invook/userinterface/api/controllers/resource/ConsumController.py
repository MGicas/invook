from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .....crosscutting.exception.impl.BusinessException import ConsumNotFoundException
from .....applicationcore.facade.impl.InventoryFacadeImpl import InventoryFacadeImpl
from ...serializers.ConsumSerializer import ConsumSerializer

class ConsumController(APIView):
    facade = InventoryFacadeImpl()

    def get(self, request, id=None):
        if id:
            try:
                consum = self.facade.get_consum(id)
                serializer = ConsumSerializer(consum)
                return Response(serializer.data)
            except ConsumNotFoundException as e:
                return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
        else:
            all_consum = self.facade.list_all_consums()
            serializer = ConsumSerializer(all_consum, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ConsumSerializer(data=request.data)
        if serializer.is_valid():
            consum = serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, id):
        consum = self.facade.patch_consum(id, **request.data)
        serializer = ConsumSerializer(consum)
        return Response(serializer.data)


