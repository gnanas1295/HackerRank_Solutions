import unittest
from solution1 import emailValidation


class TestEmailValidation(unittest.TestCase):
    def test_valid_email(self):
        self.assertEqual(
            emailValidation("John Doe <john.doe@example.com>"),
            "John Doe <john.doe@example.com>",
        )
