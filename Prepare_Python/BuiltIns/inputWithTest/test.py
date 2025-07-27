import unittest
from solution1 import functionExection


class inputTesting(unittest.TestCase):

    def testsampleAdditionEval(self):
        self.assertEqual(functionExection("1 + 2", 3), "True")
