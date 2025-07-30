import unittest
from solution1 import strToSort


class TestSortingTechniques(unittest.TestCase):
    def test_mixed_case_and_digits(self):
        self.assertEqual(strToSort("Sorting1234"), "ginortS1324")

    def test_only_lowercase(self):
        self.assertEqual(strToSort("abcdefg"), "abcdefg")

    def test_only_uppercase(self):
        self.assertEqual(strToSort("ABCDEFG"), "ABCDEFG")

    def test_only_digits(self):
        self.assertEqual(strToSort("9876543210"), "1357902468")

    def test_mixed_characters(self):
        self.assertNotEqual(strToSort("aBcD1e2F3gH4"), "abcdeFHG1342")
