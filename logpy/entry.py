from datetime import datetime, timedelta
from typing import Tuple


class Entry:
    start_time: datetime
    end_time: datetime
    category: str
    description: str

    def __init__(self, start_time, end_time, category, description):
        pass

    @property
    def duration(self) -> timedelta:
        pass

    def to_pair(self) -> Tuple[str, timedelta]:
        pass
