import unittest
from solution1 import meanVarStd
import numpy


class TestMeanVarStd(unittest.TestCase):
    def test_mean(self):
        actual_result = meanVarStd([[1, 2], [3, 4]])
        expected_mean = [1.5, 3.5]
        expected_var = [1.0, 1.0]
        expected_std = 1.11803398875

        # Test each part of the result separately
        numpy.testing.assert_allclose(actual_result[0], expected_mean)
        numpy.testing.assert_allclose(actual_result[1], expected_var)
        self.assertAlmostEqual(actual_result[2], expected_std)
