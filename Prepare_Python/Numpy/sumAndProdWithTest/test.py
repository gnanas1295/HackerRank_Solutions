import unittest
from solution1 import sumAndProdNumPY


class TestSumAndProd(unittest.TestCase):

    def testSumAndProd(self):
        self.assertEqual(sumAndProdNumPY([[1, 2], [3, 4]]), 24)
