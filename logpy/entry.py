from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Tuple


@dataclass(frozen=True, order=True)
class Entry:
    """
    Class for log entries
    """
    start_time: datetime
    end_time: datetime
    category: str
    description: str = ''

    def __post_init__(self):
        if self.end_time <= self.start_time:
            raise ValueError('end_time must be larger than start_time')

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
