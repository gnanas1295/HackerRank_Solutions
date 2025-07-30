import unittest
from solution1 import allChecks


class TestCheckingValidations(unittest.TestCase):
    def testChecks(self):
        self.assertEqual(allChecks([12, 9, 61, 5, 14]), True)
