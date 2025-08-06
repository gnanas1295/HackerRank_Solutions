import unittest
from solution1 import vowelFind


class TestVowelFind(unittest.TestCase):

    def test_vowel_find_basic(self):
        self.assertEqual(vowelFind("rabcdeefg"), ["ee"])

    def test_vowel_find_multiple(self):
        self.assertEqual(vowelFind("rabcdeefgyiiik"), ["ee", "iii"])

    def test_vowel_find_no_match(self):
        self.assertEqual(vowelFind("rhythm"), -1)

    def test_vowel_find_start_end_vowel(self):
        self.assertEqual(vowelFind("aeiouaeiou"), -1)

    def test_vowel_find_consecutive_consonants(self):
        self.assertEqual(vowelFind("qwrtypsdfghjklzxcvbnm"), -1)

    def test_vowel_find_mixed_case(self):
        self.assertEqual(vowelFind("rAbcdeEfGyIiIk"), ["eE", "IiI"])

    def test_vowel_find_single_vowel(self):
        self.assertEqual(vowelFind("rabcdEfgh"), -1)

    def test_vowel_find_long_vowel_sequence(self):
        self.assertEqual(vowelFind("rAeiouAeiouAeiouB"), ["AeiouAeiouAeiou"])

    def test_vowel_find_empty_string(self):
        self.assertEqual(vowelFind(""), -1)

    def test_vowel_find_only_vowels(self):
        self.assertEqual(vowelFind("aeiou"), -1)

    def test_vowel_find_only_consonants(self):
        self.assertEqual(vowelFind("rhythm"), -1)

    def test_vowel_find_with_spaces(self):
        self.assertEqual(vowelFind("r abcdeefg"), ["ee"])

    def test_vowel_find_with_numbers(self):
        self.assertEqual(vowelFind("r123deefg"), ["ee"])
