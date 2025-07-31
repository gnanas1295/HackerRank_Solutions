import unittest
from solution1 import validPhoneNumber


class TestValidPhoneNumber(unittest.TestCase):
    def test_valid_phone_numbers(self):
        self.assertEqual(validPhoneNumber("9876543210"), "YES")
        self.assertEqual(validPhoneNumber("9123456789"), "YES")
        self.assertEqual(validPhoneNumber("7890123456"), "YES")

    def test_invalid_phone_numbers(self):
        self.assertEqual(validPhoneNumber("1234567890"), "NO")
        self.assertEqual(validPhoneNumber("4567890123"), "NO")
        self.assertEqual(validPhoneNumber("12345"), "NO")
        self.assertEqual(validPhoneNumber("abcdefghij"), "NO")
