from django.db import models

class EmailLog(models.Model):
    to_email = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email to {self.to_email} at {self.sent_at}"
