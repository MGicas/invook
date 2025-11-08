from django.utils import timezone
from ...applicationcore.domain.notification.EmailLog import EmailLog
from ...applicationcore.domain.resource.Loan import Loan
from ...applicationcore.domain.resource.LoanStatus import LoanStatus
from .SendGridService import SendGridService
import logging

logger = logging.getLogger(__name__)

class EmailNotificationService:

    @staticmethod
    def send_daily_email_to_lenders():
        today = timezone.now().date()

        # Solo enviar si es día hábil (lunes a viernes)
        if today.weekday() >= 5:  # 5 = sábado, 6 = domingo
            logger.debug(f"No se enviarán correos hoy, es fin de semana.")
            return "No se envió correo, es fin de semana."

        # Filtrar los préstamos que están abiertos o vencidos
        loans = Loan.objects.filter(status__in=[LoanStatus.ABIERTO.value, LoanStatus.VENCIDO.value])
        print(loans)
        if not loans.exists():
            logger.debug("No hay préstamos abiertos ni vencidos.")
            return "No hay préstamos abiertos ni vencidos."

        # Enviar correos y registrar en EmailLog
        for loan in loans:
            lender_email = loan.id_lender.email

            # Verificar si ya se envió el correo hoy
            if not EmailLog.objects.filter(to_email=lender_email, sent_at__date=today).exists():
                if loan.status == LoanStatus.ABIERTO.value:
                    subject = "Recordatorio: préstamo abierto"
                    body = f"""
                    Hola {loan.id_lender.names} {loan.id_lender.surnames},

                    Tu préstamo con ID {loan.id}, iniciado el {loan.loan_date.strftime('%Y-%m-%d')}, 
                    aún está pendiente de devolución.

                    Por favor, realízalo lo antes posible.
                    """
                elif loan.status == LoanStatus.VENCIDO.value:
                    # Si el préstamo está vencido, aseguramos que hardware_info esté definido
                    hardware_info = "\n".join(
                        [f"- {item.hardware.name} (Serial: {item.hardware.serial})" for item in loan.hardware.filter(available=False)]
                    ) or "No hay hardware no disponible para este préstamo."

                    subject = "Recordatorio: préstamo vencido"
                    body = f"""
                    Hola {loan.id_lender.names} {loan.id_lender.surnames},

                    Tu préstamo con ID {loan.id}, iniciado el {loan.loan_date.strftime('%Y-%m-%d')}, 
                    aún tiene hardware sin devolver y se ha marcado como VENCIDO.

                    A continuación, te informamos sobre los hardware pendientes:

                    {hardware_info}

                    Por favor, realiza la devolución lo antes posible.
                    """

                try:
                    # Enviar correo con SendGrid
                    SendGridService().send_email(subject, lender_email, body)
                    logger.info(f"Correo enviado a {lender_email}.")

                    # Registrar el correo en EmailLog
                    EmailLog.objects.create(
                        to_email=lender_email,
                        subject=subject,
                        body=body,
                        sent_at=timezone.now()
                    )
                except Exception as e:
                    logger.error(f"Error al enviar correo a {lender_email}: {e}")
            else:
                logger.debug(f"Correo ya enviado hoy a {lender_email}.")

        return "Correos enviados correctamente."

