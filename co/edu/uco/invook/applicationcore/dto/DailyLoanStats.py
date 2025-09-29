from typing import Optional, List
from dataclasses import dataclass
from datetime import datetime

@dataclass
class DailyLoanStats:
    date: datetime
    open_started_today_count: int
    closed_opened_today_count: int
    overdue_open_count: int

    open_started_today_pct: float = 0.0
    closed_opened_today_pct: float = 0.0
    overdue_open_pct: float = 0.0

    open_started_today_ids: Optional[List[str]] = None
    closed_opened_today_ids: Optional[List[str]] = None
    overdue_open_ids: Optional[List[str]] = None


