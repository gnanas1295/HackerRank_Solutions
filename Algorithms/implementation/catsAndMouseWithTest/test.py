import unittest
from solution1 import catAndMouse


class TestCatAndMouseDistance(unittest.TestCase):
    def testDifference(self):
        self.assertEqual(catAndMouse(1, 2, 3), "Cat B")
        self.assertEqual(catAndMouse(1, 3, 2), "Mouse C")
        self.assertEqual(catAndMouse(2, 1, 3), "Cat A")
        self.assertEqual(catAndMouse(3, 2, 1), "Cat B")
        self.assertEqual(catAndMouse(2, 2, 2), "Mouse C")
