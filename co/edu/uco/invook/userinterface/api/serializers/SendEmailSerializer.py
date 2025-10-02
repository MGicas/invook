from rest_framework import serializers

class SendEmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=255)
    to_email = serializers.EmailField()
    body = serializers.CharField()