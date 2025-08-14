# NumPy: Floor, Ceil, and Rint

This repository contains a Python solution for a challenge that demonstrates the use of NumPy's element-wise rounding functions: `floor`, `ceil`, and `rint`.

---

## Problem Statement

You are given a 1-D array of floating-point numbers. Your task is to apply three specific NumPy rounding functions to the array and print the results.
1.  **`numpy.floor()`**: Rounds each element down to the nearest integer.
2.  **`numpy.ceil()`**: Rounds each element up to the nearest integer.
3.  **`numpy.rint()`**: Rounds each element to the nearest integer, with half-way cases (like 5.5) rounding to the nearest even value.

### Input Format
- A single line containing space-separated floating-point numbers.

### Output Format
- Three lines of output:
  1. The result of `numpy.floor()`.
  2. The result of `numpy.ceil()`.
  3. The result of `numpy.rint()`.

#### Sample Input

```
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
```

#### Sample Output

```
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
```

## Explanation

The provided solution is a direct and efficient implementation of the problem's requirements.

1.  **Read Input:** It reads a single line of input and uses `map(float, ...)` to convert the space-separated values into a Python list of floats.
2.  **Set Print Options:** It calls `numpy.set_printoptions(legacy='1.13')`. This is a specific requirement of the challenge to ensure the spacing in the output array matches the expected format from older versions of NumPy.
3.  **Create NumPy Array:** It converts the Python list into a NumPy array using `numpy.array()`.
4.  **Apply Functions and Print:** It calls `numpy.floor()`, `numpy.ceil()`, and `numpy.rint()` on the array in sequence, printing the result of each function call on a new line.

---
## Algorithm Used

The solution uses **element-wise array operations**, a fundamental feature of the NumPy library. These are Universal Functions (Ufuncs) that operate on NumPy arrays in a highly optimized way.

### Time and Space Complexity

* **Time Complexity: `O(N)`**, where `N` is the number of elements in the input array. Each NumPy function (`array`, `floor`, `ceil`, `rint`) must process all `N` elements once.
* **Space Complexity: `O(N)`**. The program must store the `N`-element NumPy array in memory. Each operation also creates a new `N`-element array for its result.

---
## Key Functions and Modules

### Core Logic
-   **`numpy.array()`**: The core function for creating a NumPy array from a Python list.
-   **`numpy.floor()`**: An element-wise function that rounds each number down to the nearest integer.
-   **`numpy.ceil()`**: An element-wise function that rounds each number up to the nearest integer.
-   **`numpy.rint()`**: An element-wise function that rounds to the nearest integer.
-   **`numpy.set_printoptions()`**: A utility function to control how NumPy arrays are formatted when printed.

---

## What You Can Learn

-   **Fundamental NumPy Ufuncs:** This is a direct demonstration of some of NumPy's most common mathematical Universal Functions. It shows how a single function call can apply a complex operation to an entire array efficiently.
-   **NumPy I/O:** The code shows a standard pattern for reading numerical data and converting it into a NumPy array for processing.
-   **Output Formatting:** Introduces the `numpy.set_printoptions` utility, which is useful for ensuring consistent output formatting, especially for compatibility or specific display requirements.

---

## Additional Resources

-   [NumPy Mathematical Functions Documentation](https://numpy.org/doc/stable/reference/routines.math.html)
-   [NumPy: The absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)

---

## Conclusion

This solution is a straightforward and perfect implementation for the given task. It effectively showcases the power and simplicity of applying element-wise mathematical functions to entire arrays using the NumPy library.

**Happy Coding!**
