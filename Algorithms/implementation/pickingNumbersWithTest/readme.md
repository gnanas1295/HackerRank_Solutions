# Picking Numbers - Longest Subarray

This repository contains a Python solution for the "Picking Numbers" problem, which involves finding the longest subarray of an array where the absolute difference between any two elements is at most 1.

---

## Problem Statement

Given an array of integers, find the length of the longest subarray that can be created where the absolute difference between any two of its elements is less than or equal to 1.

### Input Format
- The first line contains **n**, the size of the array.
- The second line contains **n** space-separated integers.

### Output Format
- A single integer representing the length of the longest valid subarray.

#### Sample Input

```
6
4 6 5 3 3 1
```

#### Sample Output

```
3
```

## Explanation

The provided solution correctly solves the problem by using a frequency counting approach.

1.  **Count Frequencies:** It first uses `collections.Counter` to get a count of every unique number in the input array.
2.  **Find Adjacent Pairs:** It then creates a sorted list of the unique numbers and iterates through it to find all pairs of numbers that are adjacent (their difference is exactly 1), for example, (3, 4) or (5, 6).
3.  **Calculate Pair Lengths:** For each of these adjacent pairs, it calculates the potential subarray length by summing their frequencies from the counter (e.g., `count of 3s + count of 4s`).
4.  **Determine Max Length:** Finally, it compares the longest length found from the adjacent pairs with the longest length of a subarray containing only a single number (which is simply the maximum frequency of any one number). It returns the greater of these two values.

---
## Algorithm Used

The algorithm is a **Frequency Count** (or Hash Map) approach. It works by pre-calculating the counts of all numbers. This allows it to quickly determine the size of potential subarrays by summing the counts of their constituent numbers, avoiding a more complex brute-force search through all possible subarrays.

### Time and Space Complexity

* **Your Solution:**
    * **Time Complexity: `O(N log N)`**. This is dominated by the initial `a.sort()` step. If the sort were removed (as it is not strictly necessary for the rest of the logic), the complexity would be **`O(N)`**, as creating the `Counter` takes O(N) time and the subsequent loops run on the `k` unique elements, which is faster.
    * **Space Complexity: `O(k)`**, where `k` is the number of unique elements in the array, to store the `Counter` object and other lists.

* **Optimized Solution:**
    * **Time Complexity: `O(N)`**. The solution makes a single pass to build the `Counter` (O(N)) and a second pass over the `k` unique keys (O(k)). The total complexity is O(N + k), which simplifies to O(N).
    * **Space Complexity: `O(k)`**. It only requires space for the `Counter` object.

---
## Key Functions and Modules

### Core Logic
-   **`collections.Counter`**: A specialized dictionary from Python's standard library used to efficiently count the occurrences of each number.
-   **`set()`**: Used to get a collection of the unique numbers in the input array.
-   **`sort()`**: Used to order the unique numbers to make finding adjacent pairs easier.
-   **`abs()`**: Used to check the difference between two numbers.

---

## What You Can Learn

-   **Frequency Counting:** This is a classic example of a problem that becomes much simpler once you count the frequency of the elements.
-   **Problem Decomposition:** The solution correctly identifies that the longest subarray must be composed of either one distinct number or two distinct numbers that differ by 1.
-   **Code Simplification:** The approach works, but it also demonstrates how multiple steps (sorting, creating a set, multiple loops, complex return statement) can often be simplified into a single, more elegant loop, as shown in the optimized solution.

---

## Additional Resources

-   [`collections.Counter` Documentation](https://docs.python.org/3/library/collections.html#collections.Counter)

---

## Conclusion

This solution effectively solves the problem by leveraging a frequency map to analyze the composition of potential subarrays. It correctly identifies and tests the two types of valid subarrays (those with one distinct number and those with two) to find the maximum possible length.

**Happy Coding!**
