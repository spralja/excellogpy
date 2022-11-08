from .entry import Entry

from typing import List, Optional, Generator

from datetime import datetime


class Log:
    name: str
    entries = List[Entry]

    def __init__(self, name: str = ''):
        self.name = name

    def add_entry(self, *args, **kwargs) -> Entry:
        """
        Add an Entry object, or pass arguments that are used to create an Entry object
        :param args:
        :param kwargs:
        :return:
        """

    def range(self, start_time: Optional[datetime] = None, end_time: Optional[datetime] = None) -> Generator:
        """
        Returns a range object with entries that end after the start time and begin before the end time in chronological
        order
        :param start_time:
        :param end_time:
        :return:
        """
