# Divisible Sum Pairs Counter

This repository contains a Python solution for the "Divisible Sum Pairs" problem, which involves finding pairs of numbers in an array whose sum is divisible by a given integer.

---

## Problem Statement

Given an array of integers, `ar`, and a positive integer `k`, determine the number of pairs `(i, j)` where `i < j` and the sum `ar[i] + ar[j]` is evenly divisible by `k`.

### Input Format
- The first line contains two space-separated integers, **n** (the size of the array) and **k** (the divisor).
- The second line contains **n** space-separated integers representing the array `ar`.

### Output Format
- A single integer representing the count of valid pairs.

#### Sample Input

```
6 3
1 3 2 6 1 2
```

#### Sample Output

```
5
```

## Explanation

The provided solution is an elegant and concise implementation that leverages Python's powerful `itertools` library.

1.  **Generate Pairs:** It first uses `itertools.combinations(ar, 2)` to create an iterator that efficiently generates all unique pairs of elements from the input array `ar`. This avoids the need for manual nested loops.
2.  **Check and Count:** It then uses a generator expression `(1 for i, j in combi if (i+j) % k == 0)` to iterate through these pairs. For each pair `(i, j)`, it checks if their sum is divisible by `k` using the modulo operator (`%`). If the condition is true, it yields a `1`.
3.  **Sum the Results:** Finally, the built-in `sum()` function tallies all the `1`s yielded by the generator to produce the final total count of valid pairs.

---
## Algorithm Used

The algorithm is a **brute-force** check of all possible pairs. By using `itertools.combinations`, it does this in a very clean and "Pythonic" way. See the Time Complexity section below for a detailed performance analysis.

---
## Time Complexity Analysis ⏱️

Understanding the time complexity is crucial for evaluating a solution's performance, especially with larger inputs.

### Brute-Force Solution: `O(n²)`

The `itertools.combinations(ar, 2)` function generates every possible unique pair from the list of `n` items. The number of such pairs is `n * (n-1) / 2`. As `n` grows, this number grows quadratically. This means if you double the input size, the number of operations roughly quadruples. This is known as **O(n²)** complexity and is too slow for very large datasets.

### Optimized Solution: `O(n)`

A more optimized solution uses a frequency map of remainders.
1. It iterates through the array of `n` numbers **only once**.
2. Inside the loop, it performs constant-time operations (calculating a remainder, accessing an array index, and doing addition).

Because it only needs a single pass through the input, its performance scales linearly with the size of the input. If you double the input size, the number of operations only doubles. This is known as **O(n)** complexity and is significantly more efficient and scalable.

---
## Key Functions and Modules

### Core Logic
- **`itertools.combinations(iterable, r)`**: This is the core function of the solution. It creates an iterator that returns all unique `r`-length combinations of elements from the input iterable.
- **Generator Expression**: The expression `(1 for ... if ...)` creates an efficient iterator that is consumed by `sum()`. This is a memory-efficient way to perform a "filter and count" operation.
- **`sum()`**: The built-in function used to tally the results from the generator expression.
- **`%` (Modulo Operator)**: Used to perform the divisibility check.

---

## What You Can Learn

-   **Combinatorics with `itertools`:** This is a perfect example of how the `itertools` library can simplify complex combinatorial tasks like generating pairs or permutations.
-   **Writing Concise Code:** The solution demonstrates how to combine Python's powerful features (library functions, generators, `sum()`) to write code that is both short and highly readable.
-   **Analyzing Performance:** Comparing the `O(n²)` brute-force approach to the `O(n)` remainder-based solution highlights the importance of choosing the right algorithm for scalability.

---

## Additional Resources

-   [`itertools.combinations` Documentation](https://docs.python.org/3/library/itertools.html#itertools.combinations)
-   [Understanding Time Complexity](https://wiki.python.org/moin/TimeComplexity)

---

## Conclusion

This solution is a prime example of effective Python programming. It uses the right tool from the standard library (`itertools`) to solve the problem in a way that is clear, concise, and correct, perfectly capturing the logic in just a few lines of code.

**Happy Coding!**
