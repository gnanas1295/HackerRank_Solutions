# NumPy Array Mathematics

This repository contains a Python solution for a challenge that involves performing basic, element-wise arithmetic operations on two N x M arrays using the NumPy library.

---

## Problem Statement

You are given two integer arrays, **A** and **B**, both with dimensions N x M. Your task is to perform six element-wise mathematical operations and print the result of each:
1.  Addition (`+`)
2.  Subtraction (`-`)
3.  Multiplication (`*`)
4.  Integer Division (`//`)
5.  Modulo (`%`)
6.  Power (`**`)

### Input Format
- The first line contains space-separated integers **N** and **M**.
- The next **N** lines contain the rows of array **A**.
- The following **N** lines contain the rows of array **B**.

### Output Format
- Print the result of each of the six operations on a new line.

#### Sample Input

```
1 4
1 2 3 4
5 6 7 8
```

#### Sample Output

```
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]
```

## Explanation

The provided solution correctly performs all the required steps to solve the problem.

1.  **Read Input:** It first reads the dimensions `n` and `m`. It then uses two separate `for` loops to read the `n` rows for each of the two arrays, storing the data in standard Python lists of lists.
2.  **Convert to NumPy Arrays:** The two Python lists are then converted into NumPy arrays using `numpy.array()`. This is the crucial step that enables efficient, element-wise calculations.
3.  **Perform Operations:** The solution calls the explicit NumPy functions for each required operation (e.g., `numpy.add`, `numpy.subtract`, `numpy.floor_divide`, etc.).
4.  **Print Results:** The result of each operation, which is a new NumPy array, is printed to the console on a new line.

---
## Algorithm Used

The solution uses **element-wise array operations**, a fundamental feature of the NumPy library. No complex, high-level algorithm is needed. The operations are performed directly by highly optimized, low-level code within the NumPy library.

### Time and Space Complexity

* **Time Complexity: `O(N*M)`**. The dominant parts of the program—reading the input, creating the arrays, and performing each arithmetic operation—are all directly proportional to the number of elements in the arrays, which is `N * M`.
* **Space Complexity: `O(N*M)`**. The program must store the two N x M arrays in memory. The result of each operation also creates a new N x M array.

---
## Key Functions and Modules

### Core Logic
-   **`numpy.array(list)`**: The core function for converting a Python list of lists into a 2D NumPy array.
-   **`numpy.add()`**, **`numpy.subtract()`**, **`numpy.multiply()`**, etc.: The explicit functions for performing element-wise arithmetic on NumPy arrays. A more common and readable alternative is to use the standard Python operators (`+`, `-`, `*`), which NumPy overloads.

---

## What You Can Learn

-   **Basic NumPy Workflow:** The solution demonstrates the standard workflow of creating NumPy arrays from raw input and performing calculations.
-   **Element-Wise Operations:** This is a clear illustration of NumPy's primary strength: applying mathematical operations to entire arrays at once without writing explicit loops in Python.
-   **NumPy Functions vs. Operators:** The code uses the explicit functions (`numpy.add`). This provides a good opportunity to learn about the more idiomatic operator alternative (`a + b`), which is the preferred style in the NumPy community for its readability.

---

## Additional Resources

-   [NumPy Official Website](https://numpy.org/)
-   [NumPy: The absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)

---

## Conclusion

This solution is a straightforward and correct implementation of basic NumPy array operations. It effectively showcases how to set up and perform element-wise calculations, which are foundational to scientific computing in Python.

**Happy Coding!**
