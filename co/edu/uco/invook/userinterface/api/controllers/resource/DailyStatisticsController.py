# interfaces/api/views/statistics_apiviews.py
from datetime import datetime
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .....applicationcore.facade.impl.StatisticsFacade import StatisticsFacade
from .....services.resource.StatisticsService import StatisticsService

class DailyStatisticsController(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        date_str = request.query_params.get("date")  # YYYY-MM-DD
        include_ids = request.query_params.get("include_ids") == "true"

        if date_str:
            try:
                day = datetime.strptime(date_str, "%Y-%m-%d")
                # asumimos que viene naive en local time
                day = timezone.make_aware(day, timezone.get_current_timezone())
            except ValueError:
                return Response({"date": "Formato inválido. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            day = timezone.localtime()

        facade = StatisticsFacade(StatisticsService())
        stats = facade.daily_loans(day, include_ids=include_ids)

        return Response({
    "date": stats.date.date().isoformat(),
    "open_started_today": {
        "count": stats.open_started_today_count,
        "percentage": round(stats.open_started_today_pct, 2),
        "ids": stats.open_started_today_ids,
    },
    "closed_opened_today": {
        "count": stats.closed_opened_today_count,
        "percentage": round(stats.closed_opened_today_pct, 2),
        "ids": stats.closed_opened_today_ids,
    },
    "overdue_open": {
        "count": stats.overdue_open_count,
        "percentage": round(stats.overdue_open_pct, 2),
        "ids": stats.overdue_open_ids,
    },
    "total": stats.open_started_today_count + stats.closed_opened_today_count + stats.overdue_open_count,
})

