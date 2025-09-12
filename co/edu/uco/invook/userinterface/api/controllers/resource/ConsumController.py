from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from co.edu.uco.invook.applicationcore.facade.impl.InventoryFacadeImpl import InventoryFacadeImpl
from co.edu.uco.invook.userinterface.api.serializers.ConsumSerializer import ConsumSerializer

class ConsumController(APIView):
    facade = InventoryFacadeImpl()

    def get(self, request, consum_id=None):
        if consum_id:
            consum = self.facade.get_consum(consum_id)
            serializer = ConsumSerializer(consum)
            return Response(serializer.data)
        else:
            all_consum = self.facade.list_all_consums()
            serializer = ConsumSerializer(all_consum, many=True)
            return Response(serializer.data)

    def post(self, request):
        consum = self.facade.create_consum(**request.data)
        serializer = ConsumSerializer(consum)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, consum_id):
        consum = self.facade.patch_consum(consum_id, **request.data)
        serializer = ConsumSerializer(consum)
        return Response(serializer.data)


