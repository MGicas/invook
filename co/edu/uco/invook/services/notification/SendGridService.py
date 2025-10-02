import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from django.conf import settings
from invook.applicationcore.domain.notification.EmailLog import EmailLog

class SendGridService:
    def __init__(self):
        self.sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
    
    def send_email(self, subject, to_email, body):
        from_email = Email(settings.SENDGRID_FROM_EMAIL)
        to_email = To(to_email)
        content = Content("text/plain", body)
        mail = Mail(from_email, to_email, subject, content)

        try:
           response = self.sg.send(mail)

           if response.status_code != 202:
                raise Exception(f"Error al enviar el correo: {response.status_code}, {response.body}")
            
            
           email_log = EmailLog.objects.create(
                to_email=to_email.email,
                subject=subject,
                body=body
            )
           return response, email_log
        except Exception as e:
            raise Exception(f"Error enviando email: {e}") 