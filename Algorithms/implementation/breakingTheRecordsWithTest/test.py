import unittest
from solution1 import breakingRecords


class TestRecordsCount(unittest.TestCase):
    def testBreakingTheRecordCount(self):
        self.assertEqual(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]), [2, 4])
