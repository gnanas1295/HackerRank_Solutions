import unittest
from solution2 import validate_roman_numeral


class TestValidateRomanNumberal(unittest.TestCase):
    def testVaildRomanNumerals(self):
        valid_numerals = [
            "I",
            "II",
            "III",
            "IV",
            "V",
            "VI",
            "VII",
            "VIII",
            "IX",
            "X",
            "XL",
            "L",
            "XC",
            "C",
            "CD",
            "D",
            "CM",
            "M",
            "MM",
            "MMM",
        ]
        for numeral in valid_numerals:
            self.assertTrue(validate_roman_numeral(numeral))

    def testinvalidRomanNumerals(self):
        invalid_numerals = [
            "IIII",  # Invalid: 4 should be IV
            "XXXX",  # Invalid: 40 should be XL
            "CCCC",  # Invalid: 400 should be CD
            "MMMM",  # Invalid: 4000 should be (not representable)
            "VV",  # Invalid: 5 should be V
            "LL",  # Invalid: 50 should be L
            "DD",  # Invalid: 500 should be D
        ]
        for numeral in invalid_numerals:
            self.assertFalse(validate_roman_numeral(numeral))
