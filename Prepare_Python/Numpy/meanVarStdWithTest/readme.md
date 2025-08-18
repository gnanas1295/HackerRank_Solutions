# NumPy: Mean, Var, and Std

This repository contains a Python solution for a challenge that involves applying fundamental NumPy statistical functions (`mean`, `var`, `std`) to a 2D array along different axes.

---

## Problem Statement

You are given a 2-D array of size N x M. Your task is to find and print the following three results:
1.  The **mean** along **axis 1**.
2.  The **variance** along **axis 0**.
3.  The **standard deviation** along **axis None** (the flattened array).

### Input Format
- The first line contains space-separated integers **N** and **M**.
- The next **N** lines contain the rows of the array.

### Output Format
- Three lines of output:
  1. The resulting mean array.
  2. The resulting variance array.
  3. The resulting standard deviation scalar.

#### Sample Input

```
7
100 100 50 40 40 20 10
4
5 25 50 120
```

#### Sample Output

```
6
4
2
1
```

## Explanation of the Code

The provided solution correctly calculates the required statistical values.

1.  **Read Input:** The code first reads the dimensions N and M. It then uses a list comprehension to read the N lines of input into a Python list of lists.
2.  **Calculate Statistics:** A function `meanVarStd` is called. Inside this function, NumPy automatically converts the input list to a NumPy array to perform the calculations:
    * `numpy.mean(..., axis=1)` is called to find the mean across each row.
    * `numpy.var(..., axis=0)` is called to find the variance down each column.
    * `numpy.std(...)` is called with the default `axis=None` to find the standard deviation of all elements in the entire array.
3.  **Return and Print:** The three results are collected into a list and returned. The main script then uses a generator expression to unpack this list and print each result on a new line.

---
## Algorithm Used

The solution uses **element-wise array aggregation** functions from the NumPy library. It's a direct application of built-in, highly optimized library functions for statistical computation.

### Time and Space Complexity

* **Time Complexity: `O(N*M)`**. Each of the three main aggregation functions (`mean`, `var`, `std`) must visit all `N * M` elements of the array.
* **Space Complexity: `O(N*M)`**. The program must store the N x M array in memory.

---
## Key Functions and Modules

### Core Logic
-   **`numpy.array()`**: To create the NumPy array from a Python list.
-   **`numpy.mean(array, axis)`**: An aggregation function that computes the arithmetic mean along the specified axis.
-   **`numpy.var(array, axis)`**: An aggregation function that computes the variance along the specified axis.
-   **`numpy.std(array, axis)`**: An aggregation function that computes the standard deviation along the specified axis.

---

## What You Can Learn

-   **NumPy Statistical Functions:** This is a direct demonstration of NumPy's core statistical functions.
-   **The `axis` Parameter:** This challenge is a great exercise for understanding how the `axis` parameter works to control the direction of a calculation in a multi-dimensional array. It shows how different `axis` values can produce results of different shapes (a 1D array for `axis=0` or `axis=1`, and a single number for `axis=None`).

---

## Additional Resources

-   [NumPy Official Website](https://numpy.org/)
-   [NumPy Statistical Functions Guide](https://numpy.org/doc/stable/reference/routines.statistics.html)

---

## Conclusion

This solution is a clear and correct implementation of the required task. It effectively showcases how to use NumPy's fundamental statistical functions to analyze data across different dimensions of an array.

**Happy Coding!**
