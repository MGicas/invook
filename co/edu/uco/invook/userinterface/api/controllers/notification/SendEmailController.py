from .....applicationcore.facade.impl.SendGridFacade import SendGridFacadeImpl
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .....userinterface.api.serializers.SendEmailSerializer import SendEmailSerializer

class SendEmailController(APIView):
    def post(self, request):
        serializer = SendEmailSerializer(data=request.data)
        if serializer.is_valid():
            subject = serializer.validated_data['subject']
            to_email = serializer.validated_data['to_email']
            body = serializer.validated_data['body']

            sendgrid_facade = SendGridFacadeImpl()
            try:
                response = sendgrid_facade.send_email(subject, to_email, body)
                return Response({"detail": "Email Enviado Satisfactoriamente."}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"detail": "Error al enviar el email: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)