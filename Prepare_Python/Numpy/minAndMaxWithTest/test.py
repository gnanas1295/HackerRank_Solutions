import unittest
from solution1 import minAndMaxNumPY


class TestMinAndMaxNumPY(unittest.TestCase):
    def testMinAndMax(self):
        self.assertEqual(minAndMaxNumPY([[1, 2], [3, 4]]), 3)
