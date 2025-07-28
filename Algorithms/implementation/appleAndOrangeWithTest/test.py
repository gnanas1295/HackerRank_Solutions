import unittest
from solution1 import countApplesAndOranges


class AppleAndOrangeAtHomeTest(unittest.TestCase):

    def testApplesAndOrangePosition(self):
        self.assertEqual(
            countApplesAndOranges(7, 11, 5, 15, [-2, 2, 1], [5, -6]), [1, 1]
        )
