import unittest
from solution1 import migratoryBirds


class TestMigratoryBitrdsCount(unittest.TestCase):

    def testMigratingBirdsCount(self):
        self.assertEqual(migratoryBirds([1, 1, 2, 2, 3]), 1)
        self.assertEqual(migratoryBirds([1, 1, 2, 2, 3, 3]), 1)
        self.assertEqual(migratoryBirds([1, 2, 3, 4, 5]), 1)
        self.assertEqual(migratoryBirds([1, 2, 3, 4, 5, 5]), 5)
        self.assertEqual(migratoryBirds([1, 2, 3, 4, 5, 6]), 1)
        self.assertEqual(migratoryBirds([1]), 1)
        self.assertEqual(migratoryBirds([1, 2]), 1)
