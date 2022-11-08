import unittest
from logpy.log import Log

from datetime import datetime


class ConstructorTestCase(unittest.TestCase):

    def test00(self):
        log = Log('Name')
        self.assertEqual(log.name, 'Name')

    def test01(self):
        log = Log()
        self.assertEqual(log.name, '')


class AddEntryTestCase(unittest.TestCase):

    def test00(self):
        log = Log()
        self.assertEqual(log.add_entry(
            datetime(2022, 11, 8, 13, 0),
            datetime(2022, 11, 8, 14, 0),
            'Category',
        ), log)

entries = [
    (datetime(2022, 11, 8, 13), datetime(2022, 11, 8, 14), 'Category'),

]

class RangeTestCase(unittest.TestCase):
