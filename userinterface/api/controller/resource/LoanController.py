from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from co.edu.uco.invook.userinterface.api.serializers.LoanSerializer import LoanSerializer
from co.edu.uco.invook.applicationcore.facade.impl.LoanFacade import LoanFacade

class LoanController(APIView):

    def get(self, request):
        loans = LoanFacade.get_all()
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            new_loan = LoanFacade.create(serializer.validated_data)
            return Response(LoanSerializer(new_loan).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, pk=None):
        loan_id = str(pk)
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            updated_loan = LoanFacade.update(loan_id, serializer.validated_data)
            return Response(LoanSerializer(updated_loan).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        loan_id = str(pk)
        
        serializer = LoanSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            updated_loan = LoanFacade.update_partial(loan_id, serializer.validated_data)
            return Response(LoanSerializer(updated_loan).data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk=None):
        loan_id = str(pk)  
        LoanFacade.delete(loan_id)
        return Response({'message': 'Loan deleted'}, status=status.HTTP_204_NO_CONTENT)
