# Forming a Magic Square - Minimal Cost Calculator

This repository contains an optimal Python solution for the "Forming a Magic Square" problem. The challenge is to find the minimum cost to convert a given 3x3 matrix into a valid magic square.

---

## Problem Statement

A **magic square** is a square grid where the sum of each row, column, and both main diagonals is the same—this sum is called the "magic constant." For a 3x3 square using the distinct integers from 1 to 9, the magic constant is 15.

You are given a 3x3 matrix of integers. You can change any number in the grid to another number from 1 to 9. The "cost" of a change is the absolute difference between the original and new numbers. Your task is to find the **minimal total cost** to convert the given matrix into a valid magic square.

### Input Format
- Three lines, each containing three space-separated integers, representing the 3x3 input matrix.

### Output Format
- A single integer representing the minimum cost.

#### Sample Input

```
2
1 2 3
1 3 2
```

#### Sample Output

```
Cat B
Mouse C
```

---
## The Core Insight: Brute-Force Comparison

This problem seems like it might require a complex algorithm to figure out which numbers to change. However, the key insight is that the number of possible solutions is very small. For a 3x3 grid using the numbers 1 through 9, there are only **8 possible valid magic squares**.

Since the set of correct answers is so small, the most effective strategy is a **brute-force comparison**. Instead of trying to *transform* the input square, we simply calculate the cost to change it into each of the 8 "perfect" squares and then choose the lowest cost.

### Properties of a 3x3 Magic Square 🧙‍♂️
* **Magic Constant:** The numbers 1 through 9 sum to 45. Since this is spread across 3 rows, each row, column, and diagonal must sum to `45 / 3 = 15`.
* **Center Element:** The number in the center is always **5**.
* **Corners:** The corners are always even numbers.
* **Opposite Pairs:** Numbers opposite each other through the center always sum to 10 (e.g., 2 and 8, 4 and 6).

---
## Explanation of the Code

The provided solution implements the brute-force comparison strategy.

1.  **Store All Solutions:** It begins by hardcoding a list containing all 8 possible valid 3x3 magic squares.
2.  **Initialize Minimum Cost:** A variable, `minValue`, is initialized to infinity (`float('inf')`). This is a standard technique to ensure that the cost of the very first comparison will be lower, establishing a baseline minimum.
3.  **Iterate and Compare:** The code then loops through each of the 8 "perfect" squares.
4.  **Calculate Cost:** For each perfect square, it uses nested loops to go through all 9 cells. It calculates the cost to convert the input square into the current perfect square by summing the absolute differences (`abs(s[i][j] - p[i][j])`) of corresponding cells.
5.  **Find the Minimum:** After calculating the total cost for one perfect square, it compares this `currentValue` to the `minValue` seen so far. If the current cost is lower, it becomes the new `minValue`.
6.  **Return Result:** After comparing the input to all 8 perfect squares, the function returns the final `minValue`.

---
## Algorithm Used

The algorithm is a **Brute-Force Comparison**. It works by comparing the input against a pre-computed, exhaustive set of all possible valid solutions and selecting the best match.

### Time and Space Complexity

* **Time Complexity: `O(1)` (Constant Time)**. The number of operations is fixed. The code always performs 8 comparisons, and each comparison involves 9 subtractions. The runtime does not change based on the values in the input matrix.
* **Space Complexity: `O(1)` (Constant Space)**. The memory used to store the 8 magic squares is constant and does not depend on the input.

---
## Key Functions and Modules

### Core Logic
-   **Hardcoded List:** The list of all 8 possible magic squares is the core data structure.
-   **`float('inf')`**: Used to initialize the minimum cost to a value that is guaranteed to be higher than any possible calculated cost.
-   **`abs()`**: The built-in function to calculate the absolute difference, representing the "cost" of changing one number to another.
-   **Nested `for` loops**: Used to iterate through the 3x3 grid to sum up the costs for each cell.

---

## What You Can Learn

-   **Brute-Force on a Small Solution Space:** This problem is a classic example of how a brute-force approach can be the most effective and efficient solution when the total number of possible valid states is very small and known.
-   **Problem Simplification:** The key to this problem isn't complex algorithms, but the insight that simplifies it into a series of simple comparisons.
-   **Finding Minimums:** The pattern of initializing a variable to infinity and then looping to find a minimum value is a fundamental programming technique.

---

## Additional Resources

-   [Magic Squares - Wikipedia](https://en.wikipedia.org/wiki/Magic_square)

---

## Conclusion

This solution is a perfect example of how a seemingly complex problem can be solved simply and efficiently by leveraging a core insight about its constraints. By pre-defining the small set of valid solutions, the task is reduced to a straightforward set of comparisons.

**Happy Coding!**
