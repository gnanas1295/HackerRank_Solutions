import unittest
from solution1 import gradingStudents


class TestingGrading(unittest.TestCase):
    def testgradesofStudents(self):
        expectedGradesList = [34, 65, 72, 90]
        self.assertEqual(gradingStudents([34, 63, 72, 88]), expectedGradesList)
