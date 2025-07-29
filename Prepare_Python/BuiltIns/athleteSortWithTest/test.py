import unittest
from solution1 import sortBasedUponAge


class sortAthleteBasedAge(unittest.TestCase):

    def testAtheleteAgeSort(self):
        atheleteList = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]
        ageColumn = 1
        expectedList = [[7, 1, 0], [10, 2, 5], [6, 5, 9], [9, 9, 9], [1, 23, 12]]
        self.assertEqual(sortBasedUponAge(atheleteList, ageColumn), expectedList)
