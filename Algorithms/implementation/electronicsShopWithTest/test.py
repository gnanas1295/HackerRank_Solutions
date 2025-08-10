import unittest
from solution1 import getMoneySpent


class TestElectronicsShop(unittest.TestCase):
    def testElectronicsShop(self):
        self.assertEqual(getMoneySpent([40, 50, 60], [5, 8, 12], 60), 58)
        self.assertEqual(getMoneySpent([40, 50, 60], [5, 8, 12], 50), 48)
        self.assertEqual(getMoneySpent([40, 50, 60], [5, 8, 12], 40), -1)
        self.assertEqual(getMoneySpent([40, 50, 60], [5, 8, 12], 30), -1)
