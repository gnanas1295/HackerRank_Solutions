import unittest
from solution1 import pageCount


class TestPageCount(unittest.TestCase):
    def test_pageCount(self):
        self.assertEqual(pageCount(6, 2), 1)
        self.assertEqual(pageCount(5, 4), 0)
        self.assertEqual(pageCount(7, 1), 0)
        self.assertEqual(pageCount(10, 3), 1)
        self.assertEqual(pageCount(1, 1), 0)
        self.assertEqual(pageCount(2, 1), 0)
        self.assertEqual(pageCount(2, 2), 0)
        self.assertEqual(pageCount(6, 5), 1)
        self.assertEqual(pageCount(6, 4), 1)
        self.assertEqual(pageCount(6, 3), 1)
        self.assertEqual(pageCount(7, 7), 0)
        self.assertEqual(pageCount(7, 6), 0)
        self.assertEqual(pageCount(7, 5), 1)
        self.assertEqual(pageCount(7, 4), 1)


if __name__ == "__main__":
    unittest.main()
