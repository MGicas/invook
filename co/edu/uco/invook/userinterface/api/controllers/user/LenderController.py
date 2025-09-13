from .....applicationcore.facade.impl.UserFacadeImpl import UserFacadeImpl
from ...serializers.LenderSerializer import LenderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class LenderController(APIView):
    facade = UserFacadeImpl()

    def get(self, request, id=None):
        if id:
            lender = self.facade.get_lender(id)
            serializer = LenderSerializer(lender)
            return Response(serializer.data)
        else:
            lenders = self.facade.list_all_lenders()
            serializer = LenderSerializer(lenders, many=True)
            return Response(serializer.data)

    def post(self, request):
        lender = self.facade.create_lender(**request.data)
        serializer = LenderSerializer(lender)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, id):
        lender = self.facade.patch_lender(id, **request.data)
        serializer = LenderSerializer(lender)
        return Response(serializer.data)

    def delete(self, request, id):
        self.facade.delete_lender(id)
        return Response(status=status.HTTP_204_NO_CONTENT)
