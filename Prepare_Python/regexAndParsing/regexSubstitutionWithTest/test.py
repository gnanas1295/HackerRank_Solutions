import unittest
from solution1 import reSubFunc


class TestSubstitution(unittest.TestCase):
    def testSubstitution(self):
        # Test cases for the reSubFunc function
        self.assertEqual(
            reSubFunc(
                "This is a test && string || with multiple &&& and ||| operators"
            ),
            "This is a test and string or with multiple &&& and ||| operators",
        )
        self.assertEqual(reSubFunc("No operators here"), "No operators here")
        self.assertEqual(reSubFunc("&& and || or"), "&& and or or")
        self.assertEqual(
            reSubFunc("Mixed && and || operators in a sentence"),
            "Mixed and and or operators in a sentence",
        )
