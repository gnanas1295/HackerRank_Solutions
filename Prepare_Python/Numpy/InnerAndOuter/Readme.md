# Inner and Outer Product Calculation Using NumPy

## Problem Statement

You are given two arrays, A and B. Your task is to compute:
- The inner product of A and B.
- The outer product of A and B.

The inner product is a scalar representing the sum of the products of corresponding elements of the arrays. The outer product is a matrix where each element (i, j) is the product of A[i] and B[j].

## Input Format

- The first line contains the space-separated elements of array A.
- The second line contains the space-separated elements of array B.

## Output Format

- First, print the inner product (a scalar).
- Second, print the outer product (a 2D array).

## Sample Input
```
0 1
2 3
```

## Sample Output
```
3
[[0 0]
 [2 3]]
```


## Explanation

Given the sample input:
- **Array A:** [0, 1]
- **Array B:** [2, 3]

The **inner product** is computed as:  
`0*2 + 1*3 = 3`

The **outer product** produces a matrix:  
```
[[02, 03],   [[0, 0],
[12, 13]] =  [2, 3]]
```


## Key Functions and Modules Used

- **`numpy.fromstring()`**:  
  Converts a string of numbers into a NumPy array.  
  Documentation: [numpy.fromstring](https://numpy.org/doc/stable/reference/generated/numpy.fromstring.html)

- **`numpy.inner()`**:  
  Computes the inner product of two arrays.  
  Documentation: [numpy.inner](https://numpy.org/doc/stable/reference/generated/numpy.inner.html)

- **`numpy.outer()`**:  
  Computes the outer product of two arrays.  
  Documentation: [numpy.outer](https://numpy.org/doc/stable/reference/generated/numpy.outer.html)

- **`sys.stdin.read()`**:  
  Reads input from standard input.

## What You Can Learn

- **Efficient Data Parsing:**  
  Learn how to convert space-separated input data directly into NumPy arrays using `numpy.fromstring()`.

- **Vectorized Operations in NumPy:**  
  Understand the difference between inner and outer products, and how to compute them using NumPy's built-in functions.

- **Code Conciseness and Readability:**  
  Simplifying input conversion and making use of standard module aliasing (`import numpy as np`) leads to cleaner and more maintainable code.

## Additional Resources

- [NumPy Official Documentation](https://numpy.org/doc/stable/)
- [Introduction to NumPy](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Python sys Module Documentation](https://docs.python.org/3/library/sys.html)

## Conclusion

This challenge reinforces the use of NumPy for efficient array computations and demonstrates how to quickly compute inner and outer products using Python's standard libraries. It is an excellent exercise in both input handling and vectorized mathematical operations.

**Happy Coding!**

