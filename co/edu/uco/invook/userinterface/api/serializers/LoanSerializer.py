from rest_framework import serializers

from ....applicationcore.domain.resource.Loan import Loan
from .AdministrativeUserSerializer import AdministrativeUserSerializer
from .LenderSerializer import LenderSerializer
from .LoanHardwareSerializer import LoanHardwareSerializer

class LoanSerializer(serializers.ModelSerializer):
    id_lender = LenderSerializer(read_only=True)
    id_monitor = AdministrativeUserSerializer(read_only=True)
    hardwares = LoanHardwareSerializer(source='loanhardware_set', many=True, read_only=True)

    class Meta:
        model = Loan
        fields = ['id', 'id_lender', 'id_monitor', 'status', 'loan_date', 'return_date', 'hardwares']
    
