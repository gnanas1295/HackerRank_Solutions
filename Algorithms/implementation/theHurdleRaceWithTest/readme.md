# Hurdle Race - Potion Calculator

This repository contains an optimal Python solution for the "Hurdle Race" problem, which involves calculating the minimum number of potions required for a character to clear all hurdles in a race.

---

## Problem Statement

A character is in a hurdle race. They have a natural jump height of **k**. They can drink a magic potion that increases their jump height by 1 for each dose. Given a list of hurdle heights, what is the minimum number of potion doses the character must take to be able to clear all the hurdles?

### Input Format
- The first line contains **n** (number of hurdles) and **k** (natural jump height).
- The second line contains **n** space-separated integers representing the height of each hurdle.

### Output Format
- A single integer representing the minimum number of potion doses required. If the character can already clear all hurdles, the output should be 0.

#### Sample Input

```
5 4
1 6 3 5 2
```

#### Sample Output

```
2
```

## Explanation

The provided solution is a highly efficient and concise one-liner that correctly solves the problem.

1.  **Find the Tallest Hurdle:** The logic correctly identifies that the character only needs to be able to clear the single tallest hurdle to be able to clear them all. It uses the built-in `max(height)` function to find this value in a single pass.
2.  **Calculate Doses:** It then uses a conditional (ternary) expression to determine the result:
    * `if max(height) <= k`: This checks if the tallest hurdle is less than or equal to the character's natural jump height. If true, the character needs `0` potions.
    * `else max(height) - k`: If the tallest hurdle is higher than the character's jump height, the number of potions needed is simply the difference between the two values.

---
## Algorithm Used

The algorithm is a **direct computation**. It simplifies the problem by identifying that the only relevant piece of information is the single tallest hurdle. The entire calculation is based on this one value.

### Time and Space Complexity

* **Time Complexity: `O(N)`**, where `N` is the number of hurdles. This is because the `max()` function must iterate through the entire list once to find the maximum value. This is the optimal time complexity, as every hurdle must be checked.
* **Space Complexity: `O(1)`**. The solution uses a fixed amount of extra memory that does not scale with the number of hurdles.

---
## Key Functions and Modules

### Core Logic
-   **`max(iterable)`**: The built-in Python function used to find the largest item in an iterable (the list of hurdle heights).
-   **Conditional Expression**: The `value_if_true if condition else value_if_false` syntax, which allows for writing a concise, one-line `if/else` statement.

---

## What You Can Learn

-   **Problem Simplification:** This solution is a perfect example of how to simplify a problem to its core requirement. Instead of iterating and comparing every single hurdle against the jump height, it correctly identifies that only the maximum hurdle matters.
-   **Pythonic Conciseness:** Showcases how a conditional expression can lead to very clean, readable, and efficient one-line solutions.

---

## Additional Resources

-   [Python `max()` Function Documentation](https://docs.python.org/3/library/functions.html#max)
-   [Python Conditional Expressions](https://docs.python.org/3/reference/expressions.html#conditional-expressions)

---

## Conclusion

This solution is a prime example of an elegant and optimal solution. It correctly identifies the simplest path to the answer and implements it in a single, readable line of Python code.

**Happy Coding!**
