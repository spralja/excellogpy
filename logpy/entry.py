from datetime import datetime, timedelta
from typing import Tuple


class Entry:
    """
    Class for log entries
    """
    start_time: datetime
    end_time: datetime
    category: str
    description: str

    def __init__(self, start_time, end_time, category, description=''):
        pass

    @property
    def duration(self) -> timedelta:
        """
        Returns the duration of the entry
        :return: duration
        """

    def to_pair(self) -> Tuple[str, timedelta]:
        """
        Returns a tuple of the form (category, duration)
        :return:
        """
