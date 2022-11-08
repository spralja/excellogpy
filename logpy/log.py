from .entry import Entry

from typing import List, Self, Optional, Iterator

from pathlib import Path
from datetime import datetime


class Log:
    path: Path
    entries = List[Entry]

    def __init__(self, name: str):
        pass

    def add_entry(self, *args, **kwargs) -> Self:
        """
        :param entry:
        :return: self
        """

    def range(self, start_time: datetime, end_time: Optional[datetime] = None) -> Iterator:
        """
        Returns a range object with entries that end after the start time and begin before the end time in chronological
        order
        :param start_time:
        :param end_time:
        :return:
        """
