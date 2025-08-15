import unittest
from solution1 import climbingLeaderboard


class TestClimbingLeaderboard(unittest.TestCase):
    def test_climbing_leaderboard(self):
        self.assertEqual(
            climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]),
            [6, 5, 4, 2, 1],
        )
