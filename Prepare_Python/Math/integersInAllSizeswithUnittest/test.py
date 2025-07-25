import unittest
from solution1 import powerCalculation


class TestMyPowerFunction(unittest.TestCase):

    def testPowerOfTwoPostitiveIntergers(self):
        self.assertEqual(powerCalculation(2, 3), 8)

    def testPowerOfTwoNegativeIntergers(self):
        self.assertEqual(powerCalculation(-2, 3), -8)

    def testPowerOfTwoZeroIntergers(self):
        self.assertEqual(powerCalculation(0, 3), 0)

    def testPowerOfTwoZeroIntergers(self):
        self.assertEqual(powerCalculation(0, 0), 1)
