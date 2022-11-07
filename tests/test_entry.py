import unittest
from logpy.entry import Entry
from datetime import datetime


class ConstructorTestCase(unittest.TestCase):
    start_time = datetime(2022, 11, 7, 17)
    end_time = datetime(2022, 11, 7, 18)
    category = 'Category'
    description = 'Description'

    def test00(self):
        entry = Entry(self.start_time, self.end_time, self.category, self.description)
        self.assertEqual(entry.start_time, self.start_time)
        self.assertEqual(entry.end_time, self.end_time)
        self.assertEqual(entry.category, self.category)
        self.assertEqual(entry.description, self.description)

    def test01(self):
        entry = Entry(self.start_time, self.end_time, self.category)
        self.assertEqual(entry.start_time, self.start_time)
        self.assertEqual(entry.end_time, self.end_time)
        self.assertEqual(entry.category, self.category)
        self.assertEqual(entry.description, '')

    def test02(self):
        with self.assertRaises(ValueError):
            entry = Entry(self.end_time, self.start_time, self.category, self.description)
