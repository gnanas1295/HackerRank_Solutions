import unittest
from solution1 import dayOfProgrammer


class TestDayOfProgrammer(unittest.TestCase):
    def test_leap_year_gregorian(self):
        self.assertEqual(dayOfProgrammer(2000), "12.09.2000")
        self.assertEqual(dayOfProgrammer(2004), "12.09.2004")

    def test_non_leap_year_gregorian(self):
        self.assertEqual(dayOfProgrammer(2001), "13.09.2001")
        self.assertEqual(dayOfProgrammer(1901), "13.09.1901")

    def test_leap_year_julian(self):
        self.assertEqual(dayOfProgrammer(1600), "12.09.1600")
        self.assertEqual(dayOfProgrammer(1704), "12.09.1704")

    def test_non_leap_year_julian(self):
        self.assertEqual(dayOfProgrammer(1701), "13.09.1701")
        self.assertEqual(dayOfProgrammer(1801), "13.09.1801")

    def test_day_of_programmer_1918(self):
        self.assertEqual(dayOfProgrammer(1918), "26.09.1918")
