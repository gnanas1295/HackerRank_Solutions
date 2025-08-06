import unittest
from solution1 import floatingValueCheck


class TestFloatingPointDetection(unittest.TestCase):
    def testValidFloatingPoints(self):
        self.assertTrue(floatingValueCheck("3.14"))
        self.assertTrue(floatingValueCheck("-0.001"))
        self.assertTrue(floatingValueCheck("+.5"))
        self.assertTrue(floatingValueCheck(".123456789"))

    def testInvalidFloatingPoints(self):
        self.assertFalse(floatingValueCheck("3.14.15"))
        self.assertFalse(floatingValueCheck("abc"))
        self.assertFalse(floatingValueCheck("1.2.3"))
        self.assertFalse(floatingValueCheck("+-1.23"))
