import unittest
from solution1 import countingValleys


class TestCountingValleys(unittest.TestCase):
    def testCountingValleys(self):
        self.assertEqual(countingValleys(8, "UDDDUDUU"), 1)
        self.assertEqual(countingValleys(12, "DDUUDDUDUUUD"), 2)
        self.assertEqual(countingValleys(10, "UDUUUDUDDD"), 0)
        self.assertEqual(countingValleys(5, "UUUUU"), 0)
        self.assertEqual(countingValleys(5, "DDDDD"), 0)
