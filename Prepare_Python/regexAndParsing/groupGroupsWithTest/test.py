import unittest
from solution1 import repetitiveValueCheck


class TestRepetitiveValueCheck(unittest.TestCase):
    def test_repetitive_value_check(self):
        self.assertEqual(repetitiveValueCheck("aaa"), "a")
        self.assertEqual(repetitiveValueCheck("qwe"), -1)
        self.assertEqual(repetitiveValueCheck("112233"), "1")
        self.assertEqual(repetitiveValueCheck("aabbcc"), "a")
        self.assertEqual(repetitiveValueCheck(""), -1)
        self.assertEqual(repetitiveValueCheck("a"), -1)
        self.assertEqual(repetitiveValueCheck("aa"), "a")
        self.assertEqual(repetitiveValueCheck("abcdeedcba"), "e")
        self.assertEqual(repetitiveValueCheck("123321"), "3")
