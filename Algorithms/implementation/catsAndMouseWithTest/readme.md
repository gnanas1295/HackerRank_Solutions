# Cat and Mouse Chase

This repository contains a Python solution for the "Cat and Mouse" problem, a simple logic challenge based on calculating distances on a 1D line.

---

## Problem Statement

Two cats, A and B, and a mouse, C, are at various positions on a line. You are given their starting positions. Assuming the cats travel at the same speed, determine which cat will reach the mouse first. If they arrive at the same time, the mouse escapes.

### Input Format
- The first line contains **q**, the number of queries.
- Each of the next **q** lines contains three space-separated integers: **x** (Cat A's position), **y** (Cat B's position), and **z** (Mouse C's position).

### Output Format
- For each query, print the result on a new line:
  - "Cat A" if Cat A reaches the mouse first.
  - "Cat B" if Cat B reaches the mouse first.
  - "Mouse C" if they reach the mouse at the same time.

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

## Explanation

The provided solution solves the problem by calculating the absolute distance from each cat to the mouse.

1.  **Calculate Distances:** It first finds the distance for Cat A to reach the mouse using `abs(x - z)`. It then does the same for Cat B with `abs(y - z)`. The `abs()` function is used because distance is always a positive value, regardless of whether a cat is to the left or right of the mouse.
2.  **Compare Distances:** An `if/elif/else` block is used to compare these two distances:
    * If Cat A's distance is less than Cat B's, "Cat A" wins.
    * If Cat B's distance is less than Cat A's, "Cat B" wins.
    * If the distances are equal, the mouse escapes, and the result is "Mouse C".

---
## Algorithm Used

The algorithm is a **direct computation**. It solves the problem using basic arithmetic and conditional logic. It directly calculates the necessary values and compares them according to the problem's rules without needing any complex algorithms or data structures.

### Time and Space Complexity

* **Time Complexity: `O(1)` (Constant Time)**. For each query, the solution performs a fixed number of arithmetic operations (two subtractions, two absolute values) and a comparison. The time taken does not increase as the position numbers get larger.
* **Space Complexity: `O(1)` (Constant Space)**. The solution uses a fixed amount of memory to store a few variables for each query.

---
## Key Functions and Modules

### Core Logic
-   **`abs()`**: The built-in Python function to get the absolute value of a number. This is the key to correctly calculating the distance between two points on a line.
-   **`if/elif/else`**: The primary control structure used to compare the two calculated distances and determine the correct outcome.

---

## What You Can Learn

-   **Problem Abstraction:** This is a great example of how to translate a "story" problem into a simple mathematical comparison.
-   **Absolute Value:** Demonstrates the practical use of the `abs()` function for calculating distance.
-   **Writing Clean Conditionals:** The solution showcases a clear and readable `if/elif/else` structure for handling multiple, mutually exclusive outcomes.

---

## Additional Resources

-   [Python `abs()` Function](https://docs.python.org/3/library/functions.html#abs)

---

## Conclusion

This solution is a perfect example of a simple, direct, and efficient answer to a logic problem. It correctly models the scenario with basic arithmetic and produces the correct result with clean, readable code.

**Happy Coding!**
