import unittest
from solution2 import triangleQuest


class TraingleQuestTest(unittest.TestCase):

    def testWithPositiveIntegerforFive(self):
        expectedList = [1, 22, 333, 4444]
        self.assertEqual(triangleQuest(5), expectedList)
