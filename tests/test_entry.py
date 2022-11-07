import unittest
from logpy.entry import Entry
from datetime import datetime, timedelta

start_time = datetime(2022, 11, 7, 17)
end_time = datetime(2022, 11, 7, 18)
category = 'Category'
description = 'Description'

duration = timedelta(0, 1)


class ConstructorTestCase(unittest.TestCase):
    def test00(self):
        entry = Entry(start_time, end_time, category, description)
        self.assertEqual(entry.start_time, start_time)
        self.assertEqual(entry.end_time, end_time)
        self.assertEqual(entry.category, category)
        self.assertEqual(entry.description, description)

    def test01(self):
        entry = Entry(start_time, end_time, category)
        self.assertEqual(entry.start_time, start_time)
        self.assertEqual(entry.end_time, end_time)
        self.assertEqual(entry.category, category)
        self.assertEqual(entry.description, '')

    def test02(self):
        with self.assertRaises(ValueError):
            entry = Entry(end_time, start_time, category, description)


class DurationTestCase(unittest.TestCase):

    def test00(self):
        entry = Entry(start_time, end_time, category)
        self.assertEqual(entry.duration, duration)
