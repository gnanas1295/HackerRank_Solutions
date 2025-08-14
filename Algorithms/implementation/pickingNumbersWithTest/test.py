import unittest
from solution1 import pickingNumbers


class TestPickingNumbers(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(pickingNumbers([4, 6, 5, 3, 3, 1]), 3)

    def test_case_2(self):
        self.assertEqual(pickingNumbers([1, 2, 2, 3, 1, 2]), 5)
