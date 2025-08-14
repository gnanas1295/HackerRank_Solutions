import unittest
from solution1 import formingMagicSquare


class TestFormingMagicSquare(unittest.TestCase):

    def test_case_1(self):
        s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
        self.assertEqual(formingMagicSquare(s), 1)

    def test_case_2(self):
        s = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
        self.assertEqual(formingMagicSquare(s), 4)
