import unittest
from solution1 import sockMerchant


class TestSockMerchant(unittest.TestCase):
    def testsockPairCount(self):
        self.assertEqual(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]), 3)
        self.assertEqual(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]), 2)
        self.assertEqual(sockMerchant(5, [1, 1, 1, 1, 1]), 2)
        self.assertEqual(sockMerchant(0, []), 0)
        self.assertEqual(sockMerchant(4, [1, 2, 3, 4]), 0)
