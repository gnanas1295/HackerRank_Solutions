# Diagonal Difference Challenge

This repository provides an efficient Python solution for calculating the absolute difference between the sums of a square matrix's diagonals.

---

## Problem Statement

Given a square matrix, your task is to calculate the absolute difference between the sums of its two main diagonals: the primary (top-left to bottom-right) and secondary (top-right to bottom-left) diagonals.

### Input Format
- The first line contains a single integer, **n**, representing the number of rows and columns in the matrix.
- The next **n** lines each contain **n** space-separated integers, describing each row of the matrix.

### Output Format
- Return a single integer: the absolute difference between the sums of the two diagonals.

#### Sample Input

```
3
11 2 4
4 5 6
10 8 -12
```

#### Sample Output
```
15
```

## Explanation

For the given sample matrix:
- **Primary diagonal sum:** 11 + 5 + (-12) = 4
- **Secondary diagonal sum:** 4 + 5 + 10 = 19
- **Absolute difference:** |4 - 19| = 15

The final result is 15.

---

## Key Functions and Modules

### Core Logic
- **Single `for` Loop**: The optimized solution uses a single loop that iterates from `i = 0` to `n-1`, where `n` is the size of the matrix. This allows for a single pass over the matrix.
- **Index Calculation**:
    - The primary diagonal elements are accessed using `arr[i][i]`.
    - The secondary diagonal elements are accessed using `arr[i][n - 1 - i]`.
- **`len()`**: This built-in function is used to get the size `n` of the square matrix.
- **`abs()`**: This built-in function is used to calculate the final absolute difference between the two sums.

---

## What You Can Learn

- **Efficient Matrix Traversal**: How to access and process elements of a 2D array in a single pass, which is more performant than making multiple passes.
- **Diagonal Indexing**: Understand the common patterns for accessing the primary (`[i][i]`) and secondary (`[i][n-1-i]`) diagonals of a square matrix.
- **Code Optimization**: Learn to identify and eliminate unnecessary steps, such as creating intermediate data structures when direct calculation is possible.

---

## Additional Resources

- [Python Built-in Functions: abs()](https://docs.python.org/3/library/functions.html#abs)
- [Python Built-in Functions: len()](https://docs.python.org/3/library/functions.html#len)
- [A Guide to 2D Arrays in Python](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/)

---

## Conclusion

This solution demonstrates an efficient, single-pass approach to solving the diagonal difference problem. By calculating both diagonal sums within a single loop, the code is optimized for both speed and memory, showcasing a key principle of effective algorithm design.

**Happy Coding!** 💻
