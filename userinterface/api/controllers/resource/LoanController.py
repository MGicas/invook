from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from co.edu.uco.invook.applicationcore.facade.impl.InventoryFacadeImpl import InventoryFacadeImpl
from co.edu.uco.invook.userinterface.api.serializers.LoanSerializer import LoanSerializer

class LoanController(APIView):
    facade = InventoryFacadeImpl()

    def get(self, request, loan_id=None):
        if loan_id:
            loan = self.facade.get_loan(loan_id)
            serializer = LoanSerializer(loan)
            return Response(serializer.data)
        else:
            all_loans = self.facade.list_all_loans()
            serializer = LoanSerializer(all_loans, many=True)
            return Response(serializer.data)

    def post(self, request):
        loan = self.facade.create_loan(**request.data)
        serializer = LoanSerializer(loan)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request, loan_id):
        loan = self.facade.patch_loan(loan_id, **request.data)
        serializer = LoanSerializer(loan)
        return Response(serializer.data)

    def delete(self, request, loan_id):
        self.facade.delete_loan(loan_id)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Acciones especiales
    def post_partial_return(self, request, loan_id):
        serials = request.data.get('serials', [])
        loan = self.facade.partial_return_hardware(loan_id, serials)
        serializer = LoanSerializer(loan)
        return Response(serializer.data)

    def post_close_loan(self, request, loan_id):
        loan = self.facade.close_loan(loan_id)
        serializer = LoanSerializer(loan)
        return Response(serializer.data)
