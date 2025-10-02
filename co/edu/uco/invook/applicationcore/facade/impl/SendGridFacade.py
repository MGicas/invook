from ....services.notification.SendGridService import SendGridService

class SendGridFacadeImpl:
    def __init__(self):
        self.sendgrid_service = SendGridService()
    
    def send_email(self, subject, to_email, body):
        return self.sendgrid_service.send_email(subject, to_email, body)