from rest_framework import serializers

from co.edu.uco.invook.applicationcore.domain.resource.Loan import Loan
from co.edu.uco.invook.userinterface.api.serializers.AdministrativeUserSerializer import AdministrativeUserSerializer
from co.edu.uco.invook.userinterface.api.serializers.LenderSerializer import LenderSerializer
from co.edu.uco.invook.userinterface.api.serializers.LoanHardwareSerializer import LoanHardwareSerializer

class LoanSerializer(serializers.ModelSerializer):
    id_lender = LenderSerializer(read_only=True)
    id_monitor = AdministrativeUserSerializer(read_only=True)
    hardwares = LoanHardwareSerializer(source='loanhardware_set', many=True, read_only=True)

    class Meta:
        model = Loan
        fields = ['id', 'id_lender', 'id_monitor', 'status', 'loan_date', 'return_date', 'hardwares']
    
