import unittest
from logpy.log import Log
from logpy.entry import Entry

from datetime import datetime

entries = [
    Entry(datetime(2022, 11, 8, 13), datetime(2022, 11, 8, 14), 'Category'),
    Entry(datetime(2022, 11, 8, 14), datetime(2022, 11, 8, 15), 'Category'),
    Entry(datetime(2022, 11, 8, 13, 15), datetime(2022, 11, 8, 13, 45), 'Category'),
    Entry(datetime(2022, 11, 8, 12), datetime(2022, 11, 8, 14), 'Category'),
    Entry(datetime(2022, 11, 8, 12, 30), datetime(2022, 11, 8, 13, 30), 'Category'),
    Entry(datetime(2022, 11, 8, 13, 30), datetime(2022, 11, 8, 14, 30), 'Category'),
]


class ConstructorTestCase(unittest.TestCase):

    def test00(self):
        log = Log('Name')
        self.assertEqual(log.name, 'Name')

    def test01(self):
        log = Log()
        self.assertEqual(log.name, '')


class AddEntryTestCase(unittest.TestCase):

    def setUp(self):
        self.log = Log()

    def test04(self):
        """
        Conflict test: no conflict
        """

        self.log.add_entry(entries[0])
        self.log.add_entry(entries[1])

    def test05(self):
        """
        Conflict test
        """

        with self.assertRaises(ValueError):
            self.log.add_entry(entries[0])
            self.log.add_entry(entries[1])

    def test06(self):
        """
        Conflict test
        """

        with self.assertRaises(ValueError):
            self.log.add_entry(entries[0])
            self.log.add_entry(entries[2])

    def test07(self):
        """
        Conflict test
        """

        with self.assertRaises(ValueError):
            self.log.add_entry(entries[0])
            self.log.add_entry(entries[3])

    def test08(self):
        """
        Conflict test
        """

        with self.assertRaises(ValueError):
            self.log.add_entry(entries[0])
            self.log.add_entry(entries[4])

    def test09(self):
        """
        Conflict test
        """

        with self.assertRaises(ValueError):
            self.log.add_entry(entries[0])
            self.log.add_entry(entries[5])

    def test10(self):
        """
        Wrong Arguments
        """

        with self.assertRaises(TypeError):
            self.log.add_entry(entries[0], datetime(2022, 11, 8, 16, 30), category='Category')


class RangeTestCase(unittest.TestCase):
    pass
