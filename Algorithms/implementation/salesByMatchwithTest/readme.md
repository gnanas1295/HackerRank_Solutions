# Sock Merchant - Pair Counter

This repository contains a Python solution for the "Sock Merchant" problem, a classic frequency-counting challenge.

---

## Problem Statement

Given a pile of socks represented by an array of integers where each integer is a color ID, your task is to determine the total number of matching pairs of socks that can be formed.

### Input Format
- The first line contains **n**, the total number of socks.
- The second line contains **n** space-separated integers representing the color of each sock.

### Output Format
- A single integer representing the total number of matching pairs.

#### Sample Input

```
9
10 20 20 10 10 30 50 10 20
```

#### Sample Output

```
3
```

## Explanation

The provided solution is a highly efficient and elegant implementation that uses Python's `collections.Counter`.

1.  **Count Frequencies:** `Counter(ar)` is called to instantly create a dictionary-like object where the keys are the sock colors (e.g., `10`, `20`) and the values are their total counts (e.g., color `10` appears 4 times).
2.  **Get Counts:** The `.values()` method is used to get an iterable of just the frequencies (e.g., `[4, 3, 1, 1]`).
3.  **Calculate Pairs:** A generator expression, `(item // 2 for item in counts)`, iterates through each frequency and uses integer division (`// 2`) to find the number of pairs. For example, a count of `4` socks becomes `2` pairs, and a count of `3` socks becomes `1` pair.
4.  **Sum Total:** The outer `sum()` function adds up the number of pairs calculated for each color to get the final answer.

---
## Algorithm Used

The algorithm is a **Frequency Count** (also known as a Hash Map) approach. It makes a single pass through the list to count the occurrences of each color and then a second, smaller pass through the unique colors to calculate the pairs.

### Time and Space Complexity

* **Time Complexity: `O(N)`**. Where N is the total number of socks. `collections.Counter` iterates through the list once to build the frequency map. The subsequent sum operation iterates through the `k` unique colors. The overall complexity is O(N + k), which simplifies to O(N) since k cannot be greater than N.
* **Space Complexity: `O(k)`**. Where k is the number of unique sock colors. The `Counter` object stores one entry for each unique color. In the worst case, where all socks are different colors, the space complexity would be O(N).

---
## Key Functions and Modules

### Core Logic
-   **`collections.Counter`**: A specialized dictionary from Python's standard library that is highly optimized for counting the occurrences of items in a list.
-   **Generator Expression**: The expression `(item // 2 for item in counts)` creates a memory-efficient iterator to calculate the pairs for each color.
-   **`sum()`**: The built-in function used to aggregate the pair counts into a final total.
-   **`//` (Integer Division)**: The key mathematical operator used to calculate the number of pairs from a given count of socks.

---

## What You Can Learn

-   **The Power of `collections.Counter`**: This solution is a perfect showcase for how `Counter` can drastically simplify frequency-counting problems.
-   **Elegant Data Processing:** Demonstrates how to chain together powerful tools (a `Counter`, a generator expression, and `sum()`) to create a single, readable line of code that solves a complex task.
-   **Optimal Solutions:** This O(N) approach is the optimal way to solve this problem, highlighting the efficiency of using the right data structure (a hash map/`Counter`) for the job.

---

## Additional Resources

-   [`collections.Counter` Documentation](https://docs.python.org/3/library/collections.html#collections.Counter)
-   [Python Generator Expressions](https://peps.python.org/pep-0289/)

---

## Conclusion

This solution is a prime example of idiomatic Python. It is clean, efficient, and uses the best tools from the standard library to solve the problem in a minimal number of lines while maintaining perfect clarity.

**Happy Coding!**s
