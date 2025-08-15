# NumPy: Sum and Prod

This repository contains a Python solution for a challenge that involves chaining two fundamental NumPy aggregation functions: `sum` and `prod`, operating on a specific axis.

---

## Problem Statement

You are given a 2-D array with dimensions N x M. Your task is to first perform a `sum` operation along `axis=0` and then find the `prod` (product) of the resulting array.

### Input Format
- The first line contains space-separated integers **N** and **M**.
- The next **N** lines contain the rows of the array.

### Output Format
- A single integer representing the final product.

#### Sample Input

```
2 2
1 2
3 4
```

#### Sample Output

```
24
```

#### Explanation
1.  The input array is `[[1, 2], [3, 4]]`.
2.  The sum along `axis=0` (down the columns) is `[1+3, 2+4] = [4, 6]`.
3.  The product of this resulting array is `4 * 6 = 24`.

---
## Explanation of the Code

The provided solution is a direct and efficient implementation of the problem's requirements.

1.  **Read Input:** It first reads the dimensions `N` and `M`. It then uses a `for` loop to read the `N` lines of input, creating a Python list of lists.
2.  **Convert to NumPy Array:** The Python list is converted into a NumPy array using `numpy.array()`.
3.  **Sum over Axis 0:** The `numpy.sum()` function is called on the array with the argument `axis=0`. This calculates the sum of the elements down each column, producing a new 1-D array.
4.  **Calculate Product:** Finally, `numpy.prod()` is called on this new 1-D array. With the default `axis=None`, it multiplies all elements together to get the final single integer result, which is then printed.

---
## Algorithm Used

The solution uses **element-wise array aggregation**, a fundamental feature of the NumPy library. It's a direct application of built-in, highly optimized library functions.

### Time and Space Complexity

* **Time Complexity: `O(N*M)`**. The dominant operations—reading the input, creating the array, and summing along the axis—are all directly proportional to the total number of elements in the array, which is `N * M`.
* **Space Complexity: `O(N*M)`**. The program must store the N x M array in memory.

---
## Key Functions and Modules

### Core Logic
-   **`numpy.array()`**: The core function for creating a NumPy array from a Python list.
-   **`numpy.sum(array, axis=0)`**: An aggregation function that sums array elements along a specified axis. `axis=0` operates on columns.
-   **`numpy.prod(array, axis=None)`**: An aggregation function that multiplies all elements in an array. `axis=None` (the default) operates on the entire array.

---

## What You Can Learn

-   **Chaining NumPy Operations:** This is a direct demonstration of how to chain NumPy's aggregation functions to perform multi-step calculations on data.
-   **Understanding Axes:** The challenge reinforces the concept of an `axis` in NumPy, which is fundamental for data manipulation in multi-dimensional arrays. `axis=0` for vertical (column-wise) operations and `axis=1` for horizontal (row-wise) operations.

---

## Additional Resources

-   [NumPy Official Website](https://numpy.org/)
-   [NumPy `sum()` Documentation](https://numpy.org/doc/stable/reference/generated/numpy.sum.html)
-   [NumPy `prod()` Documentation](https://numpy.org/doc/stable/reference/generated/numpy.prod.html)

---

## Conclusion

This solution is a straightforward and perfect implementation for the given task. It effectively showcases how to combine NumPy's powerful aggregation functions to analyze data across specific dimensions.

**Happy Coding!**
