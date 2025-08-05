import unittest
from solution1 import matrixScriptDecoding


class TestMatrixScript(unittest.TestCase):
    def test_matrixScript(self):
        self.assertEqual(
            matrixScriptDecoding(
                ["Tsi", "h%x", "i #", "sM ", "$a ", "#t%", "ir!"],
                7,
                3,
            ),
            "This is Matrix#  %!",
        )
        self.assertEqual(
            matrixScriptDecoding(
                ["A1", "B2", "C3", "D4"],
                4,
                2,
            ),
            "ABCD1234",
        )
        self.assertEqual(
            matrixScriptDecoding(
                ["Hello", "World"],
                2,
                5,
            ),
            "HWeolrllod",
        )
