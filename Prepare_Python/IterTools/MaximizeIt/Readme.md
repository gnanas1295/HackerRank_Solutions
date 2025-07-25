# Maximize It! Challenge

This repository contains an efficient Python solution for the "Maximize It!" problem, which involves finding the maximum possible value of an equation by selecting one element from each of several lists.

---

## Problem Statement

You are given a function $f(x) = x^2$ and $K$ lists of integers. Your task is to pick exactly one element $x_i$ from each of the $i^{th}$ lists to maximize the value of $S$ calculated as:

$S = (\sum_{i=1}^{K} x_i^2) \pmod{M}$

You must find this maximum possible value of $S$.

### Input Format
- The first line contains two space-separated integers, **K** (the number of lists) and **M** (the modulo value).
- The next **K** lines each contain an integer $N_i$ (the number of elements in the list), followed by $N_i$ space-separated integers.

### Output Format
- Output a single integer representing the maximum value of $S$.

#### Sample Input

```
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
```

#### Sample Output
```
206
```

## Explanation

A greedy approach of picking the largest element from each list does not work because of the modulo operator. For example, a sum of 999 with $M=1000$ results in 999, but a larger sum of 1000 results in 0.

Therefore, we must test all possible combinations. The solution is to generate the **Cartesian product** of all lists. For the sample input, picking 5 from the 1st list, 9 from the 2nd, and 10 from the 3rd gives:

$(5^2 + 9^2 + 10^2) \pmod{1000} = (25 + 81 + 100) \pmod{1000} = 206 \pmod{1000} = 206$.

This combination yields the maximum possible value for $S$.

---

## Key Functions and Modules

### Combinatorics
- **`itertools.product()`**: This is the core of the solution. It computes the Cartesian product of the input lists, generating an iterator that yields every possible combination of one element from each list.

### Core Logic
- **Generator Expression `(...)`**: We use a generator expression like `(sum(x**2 for x in combo) % M for combo in all_combinations)` to efficiently process each combination. It calculates the sum of squares and applies the modulo without storing all intermediate results in memory.
- **`sum()` and `max()`**: These built-in functions are used to calculate the sum of squares for each combination and to find the overall maximum value across all combinations, respectively.

---

## What You Can Learn

- **Combinatorial Problem Solving**: Recognize when a brute-force approach over all combinations is necessary and feasible, especially in problems involving modulo arithmetic.
- **`itertools` Mastery**: Understand the power of the `itertools` module, particularly `product()`, for solving complex combinatorial and permutation-based problems cleanly.
- **Efficient Iteration**: Learn to use generator expressions to write memory-efficient and highly readable code that processes large sequences of data on the fly.

---

## Additional Resources

- [Python itertools.product() Documentation](https://docs.python.org/3/library/itertools.html#itertools.product)
- [Python Generator Expressions](https://docs.python.org/3/reference/expressions.html#generator-expressions)

---

## Conclusion

This solution effectively solves the problem by generating all possible combinations using `itertools.product` and then using a concise generator expression to find the maximum possible result. It's a powerful demonstration of how to leverage Python's built-in tools for complex calculations.

**Happy Coding!** ✨
