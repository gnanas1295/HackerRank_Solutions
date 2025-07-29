import unittest
from solution1 import getTotalX


class FactorsTwoSetsTest(unittest.TestCase):
    def testFactorsOfTwoSets(self):
        a = [2, 4]
        b = [16, 32, 96]
        self.assertEqual(getTotalX(a, b), 3)
