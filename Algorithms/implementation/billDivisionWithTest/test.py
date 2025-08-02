import unittest
from solution1 import bonAppetit


class TestBonAppetit(unittest.TestCase):
    def testBillDivision(self):
        self.assertEqual(bonAppetit([3, 10, 2, 9], 1, 12), "5")
        self.assertEqual(bonAppetit([3, 10, 2, 9], 1, 7), "Bon Appetit")
        self.assertEqual(bonAppetit([3, 10, 2, 9], 0, 14), "4")
