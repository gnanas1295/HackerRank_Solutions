import unittest
from solution1 import findIndices


class TestFindIndices(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(findIndices("ababc", "ab"), ["(0, 1)", "(2, 3)"])
        self.assertEqual(findIndices("aaaa", "aa"), ["(0, 1)", "(1, 2)", "(2, 3)"])
        self.assertEqual(findIndices("hello", "lo"), ["(3, 4)"])
        self.assertEqual(findIndices("test", "xyz"), ["(-1, -1)"])
