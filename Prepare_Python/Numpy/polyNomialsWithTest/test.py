import unittest
from solution1 import polyValue


class TestPolynomialEvaluation(unittest.TestCase):

    def test_polyValue(self):
        self.assertAlmostEqual(polyValue([1, 2, 3], 1), 6)
        self.assertAlmostEqual(polyValue([1, 2, 3], 2), 11)
        self.assertAlmostEqual(polyValue([1, 2, 3], 3), 18)
