import unittest
from solution1 import birthday


class TestChoclateDivision(unittest.TestCase):
    def test_example_case(self):
        s = [1, 2, 1, 3, 2]
        d = 3
        m = 2
        result = birthday(s, d, m)
        self.assertEqual(result, 2)

    def test_no_valid_subarray(self):
        s = [4, 5, 6]
        d = 3
        m = 2
        result = birthday(s, d, m)
        self.assertEqual(result, 0)

    def test_single_element_subarray(self):
        s = [1]
        d = 1
        m = 1
        result = birthday(s, d, m)
        self.assertEqual(result, 1)

    def test_multiple_valid_subarrays(self):
        s = [1, 2, 1, 3, 2]
        d = 4
        m = 3
        result = birthday(s, d, m)
        self.assertEqual(result, 1)
