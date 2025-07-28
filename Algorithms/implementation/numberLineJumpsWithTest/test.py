import unittest
from solution1 import kangaroo


class KangorooMeetUpTesting(unittest.TestCase):

    def testKangarooTestingMeetupSuccess(self):
        self.assertEqual(kangaroo(0, 3, 4, 2), "YES")

    def testKangarooTestingMeetupFail(self):
        self.assertEqual(kangaroo(0, 2, 5, 3), "NO")
