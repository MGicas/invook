from co.edu.uco.invook.applicationcore.domain.user.User import User
from django.db import models

class Lender(User, models.Model):
    def __str__(self):
        return f"Lender: {self.names} {self.surnames} ({self.phone})"

    class Meta:
        app_label = "invook"