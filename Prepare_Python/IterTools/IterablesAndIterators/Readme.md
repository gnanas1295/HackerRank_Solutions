# Probability of 'a' in Combinations

This repository contains a Python solution to calculate the probability that at least one of `K` randomly selected indices from a list of lowercase English letters will contain the letter 'a'.

---

## Problem Statement

You are given a list of `N` lowercase English letters. For a given integer `K`, you can select any `K` indices (0-based indexing) with a uniform probability from the list.

The task is to find the **probability** that at least one of the `K` indices selected will contain the letter: 'a'.

The `itertools` module in Python is a powerful tool for generating efficient iterators, which is key to solving this problem.

### Input Format
- The first line contains an integer **N**, denoting the length of the list.
- The next line consists of **N** space-separated lowercase English letters, denoting the elements of the list.
- The third and the last line of input contains the integer **K**, denoting the number of indices to be selected.

### Output Format
- Print a single line consisting of the **probability** that at least one of the `K` indices selected contains the letter 'a'.
- **Note:** The answer must be correct up to 3 decimal places.

#### Sample Input

```
4
a a c d
2
```

#### Sample Output
```
0.8333
```

## Explanation

Given the sample input:
- `N = 4`
- `letters = ['a', 'a', 'c', 'd']`
- `K = 2`

All possible unordered tuples of length 2 comprising of indices from 0 to 3 are:

` (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3) `

There are `6` total combinations.

The indices containing the letter 'a' are `0` and `1`.

Out of these 6 combinations, 5 of them contain either index 0 or index 1:
- `(0, 1)` (contains both 0 and 1)
- `(0, 2)` (contains 0)
- `(0, 3)` (contains 0)
- `(1, 2)` (contains 1)
- `(1, 3)` (contains 1)

Only `(2, 3)` does not contain 'a'.

Hence, the probability is `5 / 6 = 0.8333`.

---

## Code Structure and Logic

The solution leverages the `itertools` module for efficient combination generation and Python's set data structure for quick checks.

1.  **Input Reading:**
    - Reads `N` (number of characters), the list of `N` characters (`inputString`), and `K` (threshold for combinations).

2.  **Identify 'a' Indices:**
    - Creates a `set` named `indexsWithA` that stores all the 0-based indices where the letter 'a' appears in the `inputString`. Using a set allows for very fast lookups and efficient set operations.

3.  **Generate All Combinations:**
    - Uses `itertools.combinations(range(numberOfChar), threshold)` to generate all possible unique combinations of `K` indices from the total `N` available indices.
    - Converts the iterator to a `list` (`totalCombinations`) and gets its length (`totalCountCombinations`) to determine the total sample space.

4.  **Count Favorable Combinations:**
    - Initializes a `counter` to `0`.
    - Iterates through each `tupleToCheck` (a combination of indices) in `totalCombinations`.
    - For each `tupleToCheck`, it uses `indexsWithA.isdisjoint(tupleToCheck)`:
        - `isdisjoint()` returns `True` if the two sets (or set and iterable) have **no common elements**.
        - `if not indexsWithA.isdisjoint(tupleToCheck):` means "if they are *not* disjoint," which implies they share at least one common index. This is exactly what's needed to identify combinations that contain at least one 'a'.
        - If a combination contains at least one 'a' index, the `counter` is incremented.

5.  **Calculate and Print Probability:**
    - The probability is calculated as `counter / totalCountCombinations`.
    - The result is printed formatted to four decimal places using an f-string: `f"{probability:.4f}"`.

---

## Key Functions and Modules

-   **`itertools.combinations(iterable, r)`**:
    -   Returns an iterator that yields subsequences of length `r` from the `iterable`. These combinations are generated in lexicographic sort order of the input `iterable`. Elements are treated as unique based on their position, not their value. This is crucial for efficiently generating all possible ways to select `K` indices.

-   **`enumerate(iterable)`**:
    -   Used to get both the index and the value when iterating over `inputString`. This helps in building the `indexsWithA` set.

-   **`set()`**:
    -   A built-in Python data structure that stores unique elements. Its efficiency for membership testing (`in` operator) and set operations (`isdisjoint()`) is vital for this problem.

-   **`set.isdisjoint(other_iterable)`**:
    -   Returns `True` if the set has no elements in common with `other_iterable`. Returns `False` if they share at least one element. This method is highly optimized for checking overlap.

---

## What You Can Learn

-   **Combinatorics with `itertools`**: Practical application of `itertools.combinations` to generate subsets of elements.
-   **Efficient Indexing and Filtering**: Using `enumerate` and set comprehensions for concisely identifying specific elements' positions.
-   **Set Operations for Overlap Checks**: Understanding how `set.isdisjoint()` provides an efficient way to determine if two collections share any common elements, which is a common pattern in problems requiring intersection checks.
-   **Probability Calculation**: Basic probability calculation involving favorable outcomes over total possible outcomes.
-   **Formatted Output**: Using f-strings for precise numerical output formatting.

---

## Additional Resources

-   [Python `itertools` Module Documentation](https://docs.python.com/3/library/itertools.html)
-   [Python `set` Data Structure Documentation](https://docs.python.com/3/tutorial/datastructures.html#sets)
-   [Python `enumerate` Function](https://docs.python.com/3/library/functions.html#enumerate)

---

## Conclusion

This solution effectively combines Python's powerful `itertools` module with efficient set operations to solve a probability problem involving combinations. It highlights how choosing the right data structures and algorithms can lead to concise, readable, and performant code.

**Happy Coding!**