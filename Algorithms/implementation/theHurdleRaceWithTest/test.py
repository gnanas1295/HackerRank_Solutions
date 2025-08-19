import unittest
from solution1 import hurdleRace


class TestHurdleRace(unittest.TestCase):
    def testHurdleRace(self):
        self.assertEqual(hurdleRace(4, [1, 6, 3, 5]), 2)
        self.assertEqual(hurdleRace(7, [1, 6, 3, 5]), 0)
        self.assertEqual(hurdleRace(5, [1, 6, 3, 5]), 1)
