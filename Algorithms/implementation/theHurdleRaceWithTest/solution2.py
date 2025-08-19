def hurdleRace(k, height):
    """
    Calculates the minimum number of potions needed to clear all hurdles.
    """
    # 1. Find the height of the tallest hurdle in the race.
    tallest_hurdle = max(height)

    # 2. Compare the tallest hurdle to the character's natural jump height.
    if tallest_hurdle > k:
        # The number of potions needed is the difference.
        potions_needed = tallest_hurdle - k
        return potions_needed
    else:
        # If the character can already clear all hurdles, no potions are needed.
        return 0
