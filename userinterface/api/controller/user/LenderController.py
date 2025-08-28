# co/edu/uco/invook/userinterface/controller/lender_controller.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from co.edu.uco.invook.userinterface.api.serializers.LenderSerializer import LenderSerializer
from co.edu.uco.invook.applicationcore.facade.impl.LenderFacade import LenderFacade

class LenderController(APIView):

    def get(self, request):
        lenders = LenderFacade.get_all()
        serializer = LenderSerializer(lenders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LenderSerializer(data=request.data)
        if serializer.is_valid():
            new_lender = LenderFacade.create(serializer.validated_data)
            return Response(LenderSerializer(new_lender).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        lender_id = str(pk)
        LenderFacade.delete(lender_id)
        return Response({'message': 'Lender deleted'}, status=status.HTTP_204_NO_CONTENT)
