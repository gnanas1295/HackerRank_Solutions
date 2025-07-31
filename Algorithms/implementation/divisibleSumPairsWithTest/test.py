import unittest
from solution1 import divisibleSumPairs


class TestDivisibleSumPairs(unittest.TestCase):
    def test_example_case(self):
        n = 6
        k = 3
        ar = [1, 2, 3, 4, 5, 6]
        result = divisibleSumPairs(n, k, ar)
        self.assertEqual(result, 5)

    def test_no_pairs(self):
        n = 4
        k = 10
        ar = [1, 2, 3, 4]
        result = divisibleSumPairs(n, k, ar)
        self.assertEqual(result, 0)

    def test_all_pairs_divisible(self):
        n = 5
        k = 5
        ar = [5, 10, 15, 20, 25]
        result = divisibleSumPairs(n, k, ar)
        self.assertEqual(result, 10)
