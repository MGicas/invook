from rest_framework import serializers

class ConsumSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    count = serializers.IntegerField()
    rfid_lender = serializers.CharField(max_length=100)
    id_lender = serializers.CharField(max_length=100)
    id_monitor = serializers.CharField(max_length=100)
    code_supply = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField()
