from rest_framework import serializers

class LoanSerializer(serializers.Serializer):
    id = serializers.CharField()  
    count = serializers.IntegerField()
    rfid_lender = serializers.CharField(max_length=100)
    id_lender = serializers.CharField(max_length=100)
    id_monitor = serializers.CharField(max_length=100)
    serial_hardware = serializers.CharField(max_length=100)
    loan_date = serializers.DateTimeField()
    return_date = serializers.DateTimeField()
    status = serializers.ChoiceField(choices=['abierto', 'cerrado', 'vencido'])
    
