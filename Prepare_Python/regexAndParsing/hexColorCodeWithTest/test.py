import unittest
from solution1 import regexPatternSearch


class TestHexColorCode(unittest.TestCase):
    def test_valid_hex_codes(self):
        input_str = "Here are some colors: #ff5733, #123456, and #abc"
        expected_output = ["#ff5733", "#123456", "#abc"]
        self.assertEqual(regexPatternSearch(input_str), expected_output)
