# Birthday Cake Candles Challenge

This repository contains an efficient Python solution for the "Birthday Cake Candles" problem, a common challenge focusing on array traversal and counting.

---

## Problem Statement

You are given a list of integers representing the heights of candles on a birthday cake. The child can only blow out the tallest candles. Your task is to count how many of the candles are the tallest.

### Input Format
- The first line contains an integer, **n**, the number of candles.
- The second line contains **n** space-separated integers representing the candle heights.

### Output Format
- Return a single integer representing the count of the tallest candles.

#### Sample Input

```
4
3 2 1 3
```

#### Sample Output
```
2
```

## Explanation

The candle heights are `[3, 2, 1, 3]`.
1.  First, we find the maximum height in the array, which is **3**.
2.  Next, we count how many times the number **3** appears in the array. It appears **2** times.

Therefore, the result is 2.

---

## Key Functions Used

### Core Logic
The most Pythonic solution uses two simple, built-in functions:
-   **`max(iterable)`**: This function efficiently finds the largest item in an iterable (like a list) in a single pass. We use it to determine the height of the tallest candles.
-   **`list.count(value)`**: This list method counts the number of times a specific `value` appears in the list. We use it to count the occurrences of the maximum height.

This approach is both highly readable and performant, with a time complexity of $O(N)$.

---

## What You Can Learn

-   **Using Built-in Functions**: How to leverage Python's powerful built-in functions like `max()` and `count()` to write clean, simple, and efficient code.
-   **Problem Decomposition**: Breaking down a problem into simple, logical steps (1. Find the max value, 2. Count the max value) often leads to the clearest solution.
-   **Algorithmic Efficiency**: Recognizing that a linear scan ($O(N)$) is more efficient than sorting ($O(N \log N)$) for this type of problem.

---

## Additional Resources

-   [Python Built-in Functions: max()](https://docs.python.org/3/library/functions.html#max)
-   [Python List Methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

---

## Conclusion

This solution demonstrates an elegant approach to a common counting problem. By using Python's built-in capabilities, we can solve the challenge with code that is not only correct but also exceptionally clear and efficient.

**Happy Coding!** 🎂
