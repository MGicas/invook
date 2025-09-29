from datetime import datetime, time
from django.db.models import Q
from django.utils import timezone

from ...applicationcore.domain.resource.Loan import Loan
from ...applicationcore.domain.resource.LoanStatus import LoanStatus  # Enum
from ...applicationcore.dto.DailyLoanStats import DailyLoanStats

TZ = timezone.get_current_timezone()

class StatisticsService:

    @staticmethod
    def _day_bounds(day: datetime):
        """Retorna (inicio_dia, fin_dia) en timezone del sistema (America/Bogota)."""
        local_day = timezone.make_naive(day, TZ) if timezone.is_aware(day) else day
        start = timezone.make_aware(datetime.combine(local_day.date(), time.min), TZ)
        end = timezone.make_aware(datetime.combine(local_day.date(), time.max), TZ)
        return start, end

    def daily_loans(self, day: datetime, include_ids: bool = False) -> DailyLoanStats:
        start, end = self._day_bounds(day)

        OPEN = LoanStatus.ABIERTO.value
        CLOSED = getattr(LoanStatus, "CERRADO", None)
        CLOSED = CLOSED.value if CLOSED else "CERRADO"

        open_started_today_qs = Loan.objects.filter(
            loan_date__gte=start, loan_date__lte=end
        ).filter(Q(return_date__isnull=True) | Q(status=OPEN))

        closed_opened_today_qs = Loan.objects.filter(
            loan_date__gte=start, loan_date__lte=end
        ).filter(Q(return_date__isnull=False) | Q(status=CLOSED))

        overdue_open_qs = Loan.objects.filter(
            loan_date__lt=start
        ).filter(Q(return_date__isnull=True) | Q(status=OPEN))

        open_count = open_started_today_qs.count()
        closed_count = closed_opened_today_qs.count()
        overdue_count = overdue_open_qs.count()
        total = open_count + closed_count + overdue_count

        def pct(x): return (x / total * 100) if total > 0 else 0.0

        return DailyLoanStats(
            date=start,
            open_started_today_count=open_count,
            closed_opened_today_count=closed_count,
            overdue_open_count=overdue_count,
            open_started_today_pct=pct(open_count),
            closed_opened_today_pct=pct(closed_count),
            overdue_open_pct=pct(overdue_count),
            open_started_today_ids=list(open_started_today_qs.values_list("id", flat=True)) if include_ids else None,
            closed_opened_today_ids=list(closed_opened_today_qs.values_list("id", flat=True)) if include_ids else None,
            overdue_open_ids=list(overdue_open_qs.values_list("id", flat=True)) if include_ids else None,
        )