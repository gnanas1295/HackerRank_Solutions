#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    """
    Calculates the player's rank after each game using an efficient
    two-pointer approach.
    """
    # In Python 3.7+, dict.fromkeys is a standard way to get unique items
    # from an iterable while preserving order. This is O(N).
    unique_ranks = list(dict.fromkeys(ranked))

    player_ranks = []

    # Start a pointer at the end of the unique leaderboard (lowest score).
    rank_idx = len(unique_ranks)

    # Iterate through each of the player's scores (which are ascending).
    for score in player:
        # Move the leaderboard pointer up (to lower indices/higher scores)
        # as long as the player's score is greater than or equal to the
        # score at the pointer's current position.
        while rank_idx > 0 and score >= unique_ranks[rank_idx - 1]:
            rank_idx -= 1

        # The rank is the pointer's index + 1 (since ranks are 1-based).
        player_ranks.append(rank_idx + 1)

    return player_ranks


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
