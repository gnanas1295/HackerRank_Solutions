# Basketball Record Breaking Counter

This repository contains a Python solution for a problem that involves tracking and counting the number of times a season record for most and least points is broken.

---

## Problem Statement

A basketball player wants to track her performance over a season. Given a sequence of scores from her games, we need to determine how many times she broke her record for the most points scored and how many times she broke her record for the least points scored. The first game's score establishes the initial records.

### Input Format
- The first line contains an integer **n**, the number of games played.
- The second line contains **n** space-separated integers representing the scores for each game in order.

### Output Format
- Return an array of two integers:
  1. The count of times the maximum score record was broken.
  2. The count of times the minimum score record was broken.

#### Sample Input

```
9
10 5 20 20 4 5 2 25 1
```

#### Sample Output

```
2 4
```

## Explanation

The provided solution attempts to solve the problem by maintaining two separate lists: one for all the scores that broke the highest record and one for all the scores that broke the lowest record.

1.  **Initialization:** It sets a `thresholdScore` based on the first game and initializes two empty lists, `highestScores` and `lowestScores`.
2.  **Iteration:** The code loops through every score in the input list.
3.  **Complex Checks:** For each score, it compares it to the initial `thresholdScore`.
    * If the score is higher, it enters a series of nested `if` statements to check if the score is not already in the `highestScores` list and if it's greater than the `max()` of that list. If it passes, it's appended.
    * A similar, complex process is applied for scores that are lower than the threshold, using the `lowestScores` list and the `min()` function.
4.  **Final Count:** After iterating through all scores, the final answer is the length of the `highestScores` and `lowestScores` lists.

---
## Algorithm Used

This solution uses a **brute-force** approach that keeps a full history of all record-breaking scores. It iterates through the list of all scores and, for each score, performs checks against lists of previously stored records.

---
## Key Functions and Modules

### Core Logic
- **`for` loop**: To iterate through the list of scores.
- **`if/elif`**: To separate logic for scores that are potentially higher or lower than the initial record.
- **`max()` and `min()`**: Built-in functions used repeatedly inside the loop to find the current records by scanning the lists of past record-breaking scores.
- **`in` operator**: Used to check for the existence of a score in the record lists, which is an inefficient operation for lists.

---

## What You Can Learn

-   **State Tracking:** This problem is a classic example of needing to track state (the current min and max) as you iterate through a sequence.
-   **Algorithmic Efficiency:** The provided solution highlights the importance of choosing an efficient approach. While maintaining a full history of records works, it is much slower than only tracking the single current minimum and maximum values. This shows the difference between an O(n²) and an O(n) solution.

---

## Additional Resources

-   [Python `min()` and `max()` Functions](https://docs.python.org/3/library/functions.html#min)
-   [Time Complexity in Python](https://wiki.python.org/moin/TimeComplexity)

---

## Conclusion

This solution demonstrates one possible way to solve the problem by keeping a history of record-breaking events. However, it also serves as a great lesson in algorithmic efficiency, showing how a simpler approach of only tracking the necessary current state can lead to a much faster and more readable solution.

**Happy Coding!**
