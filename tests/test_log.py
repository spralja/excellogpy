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

    def test00(self):
        log = Log()
        self.assertEqual(log.add_entry(
            datetime(2022, 11, 8, 13, 0),
            datetime(2022, 11, 8, 14, 0),
            'Category',
        ), log)

    def test01(self):
        """
        Tests adding an Entry
        """

        self.assertEqual(self.log.add_entry(entries[0]), entries[0])

    def test02(self):
        """
        test adding an entry as args
        """

        start_time = entries[0].start_time
        end_time = entries[0].end_time
        category = entries[0].category
        description = entries[0].description

        entry = self.log.add_entry(start_time, end_time, category, description)

        self.assertEqual(start_time, entry.start_time)
        self.assertEqual(end_time, entry.end_time)
        self.assertEqual(category, entry.category)
        self.assertEqual(description, entry.description)

    def test03(self):
        """
        tests adding an entry as args, kwargs
        """

        start_time = entries[0].start_time
        end_time = entries[0].end_time
        category = entries[0].category
        description = entries[0].description

        entry = self.log.add_entry(start_time, category=category, end_time=end_time, description=description)

        self.assertEqual(start_time, entry.start_time)
        self.assertEqual(end_time, entry.end_time)
        self.assertEqual(category, entry.category)
        self.assertEqual(description, entry.description)

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


class RangeTestCase(unittest.TestCase):
    pass
