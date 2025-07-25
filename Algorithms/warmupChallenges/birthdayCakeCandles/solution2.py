def birthdayCakeCandles(candles: list[int]) -> int:
    """
    Counts the number of tallest candles.
    """
    # Find the height of the tallest candle
    max_height = max(candles)

    # Count how many times that height appears in the list
    return candles.count(max_height)


# Example Usage
candle_heights = [3, 2, 1, 3]
result = birthdayCakeCandles(candle_heights)
print(result)  # Output: 2
