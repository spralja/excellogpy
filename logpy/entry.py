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
        if end_time <= start_time:
            raise ValueError("end_time must be greater than start_time")

        self.start_time = start_time
        self.end_time = end_time
        self.category = category
        self.description = description

    @property
    def duration(self) -> timedelta:
        """
        Returns the duration of the entry
        :return: duration
        """

        return self.end_time - self.start_time

    def to_pair(self) -> Tuple[str, timedelta]:
        """
        Returns a tuple of the form (category, duration)
        :return:
        """

        return self.category, self.duration
