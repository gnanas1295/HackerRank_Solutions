# NumPy: Min and Max

This repository contains a Python solution for a challenge that involves chaining two of NumPy's aggregation functions, `min` and `max`, on a 2D array.

---

## Problem Statement

You are given a 2-D array with dimensions N x M. Your task is to first perform the `min` operation along `axis=1` and then find the `max` of the resulting array.

### Input Format
- The first line contains space-separated integers **N** and **M**.
- The next **N** lines contain the rows of the array.

### Output Format
- A single integer representing the final maximum value.

#### Sample Input

```
4 2
2 5
3 7
1 3
4 0
```

#### Sample Output

```
3
```

#### Explanation
1.  The input array is `[[2, 5], [3, 7], [1, 3], [4, 0]]`.
2.  The `min` along `axis=1` (across the rows) is `[min(2,5), min(3,7), min(1,3), min(4,0)]`, which results in the array `[2, 3, 1, 0]`.
3.  The `max` of this resulting array is `3`.

---
## Explanation of the Code

The provided solution is a direct and highly "Pythonic" implementation of the problem's requirements.

1.  **Read Input:** The code first reads the dimensions N and M, then uses a list comprehension to efficiently read the N lines of input into a Python list of lists.
2.  **Core Calculation:** A single function, `minAndMaxNumPY`, performs the entire calculation in one line: `max(numpy.min(arrayList, axis=1))`.
    * `numpy.min(arrayList, axis=1)`: This is the inner part. It takes the input list, treats it as a NumPy array, and finds the minimum value in each row (along `axis=1`). This operation returns a new 1-D NumPy array containing these minimums.
    * `max(...)`: The outer part. This is Python's built-in `max()` function, which takes the 1-D array of minimums and finds the single largest value within it.
3.  **Print Result:** The final integer result is returned and printed.

---
## Algorithm Used

The solution uses **element-wise array aggregation**, a fundamental feature of the NumPy library. It's a direct application of built-in, highly optimized library functions.

### Time and Space Complexity

* **Time Complexity: `O(N*M)`**. The dominant operation is `numpy.min`, which must visit every element in the N x M matrix to find the minimums for each row.
* **Space Complexity: `O(N*M)`**. The program must store the N x M array in memory. An intermediate array of size N is also created to store the row minimums.

---
## Key Functions and Modules

### Core Logic
-   **`numpy.min(array, axis=1)`**: An aggregation function that finds the minimum value along a specified axis. `axis=1` operates on rows.
-   **`max(iterable)`**: Python's built-in function to find the largest item in an iterable. `numpy.max()` could also be used here.

---

## What You Can Learn

-   **Chaining Operations:** This is a perfect example of how to chain functions together in Python (`max(numpy.min(...))`) to create concise and readable code.
-   **Understanding Axes:** The challenge reinforces the concept of an `axis` in NumPy. `axis=1` is a common parameter for performing row-wise operations in data analysis.
-   **NumPy and Python Interoperability:** Shows how seamlessly you can pass the result of a NumPy operation (a NumPy array) to a standard Python built-in function (`max()`).

---

## Additional Resources

-   [NumPy Official Website](https://numpy.org/)
-   [NumPy `min()` Documentation](https://numpy.org/doc/stable/reference/generated/numpy.min.html)

---

## Conclusion

This solution is an excellent and efficient implementation for the given task. It effectively showcases how to combine NumPy's powerful axis-based aggregations to solve data analysis problems in just a single line of code.

**Happy Coding!**
