from datetime import datetime
from ....services.resource.StatisticsService import StatisticsService

class StatisticsFacade:
    def __init__(self, stats_service: StatisticsService):
        self.stats_service = stats_service

    def daily_loans(self, day: datetime, include_ids: bool = False):
        return self.stats_service.daily_loans(day, include_ids)
