# NumPy: Evaluate Polynomial (polyval)

This repository contains a Python solution for a challenge that demonstrates the use of NumPy's `polyval` function to evaluate a polynomial at a specific point.

---

## Problem Statement

You are given the coefficients of a polynomial **P**. Your task is to find the value of **P(x)** for a given value of **x**.

### Input Format
- The first line contains the space-separated coefficients of the polynomial.
- The second line contains the integer value of **x**.

### Output Format
- Print the result of the polynomial evaluation.

#### Sample Input

```
1.1 2 3
0
```

#### Sample Output

```
3.0
```

## Explanation of the Code

The provided solution is a direct and efficient implementation of the problem's requirements.

1.  **Read Input:** The code first reads a line of space-separated coefficients and uses `map(float, ...)` to convert them into a Python list of floats. It then reads the second line to get the integer value of `x`.
2.  **Evaluate Polynomial:** The list of coefficients and the value `x` are passed to a function that contains the core logic: `numpy.polyval(inputCoefficients, xValue)`.
3.  **`polyval` Function:** This NumPy function takes the list of coefficients (representing a polynomial like `1.1x² + 2x + 3`) and the point `x` (e.g., `0`) and calculates the result (`1.1*(0)² + 2*(0) + 3 = 3.0`).
4.  **Print Result:** The final floating-point value returned by `polyval` is printed to the console.

---
## Algorithm Used

The solution uses the **`numpy.polyval`** function, which implements an efficient and numerically stable algorithm (like **Horner's method**) for polynomial evaluation. It is a direct application of a built-in library function.

### Time and Space Complexity

* **Time Complexity: `O(N)`**, where N is the number of coefficients (one more than the degree of the polynomial). Evaluating the polynomial requires a number of operations proportional to the number of its terms.
* **Space Complexity: `O(N)`** to store the list of coefficients in memory.

---
## Key Functions and Modules

### Core Logic
-   **`numpy.polyval(p, x)`**: The core NumPy function for evaluating a polynomial `p` (represented by its coefficients) at a point `x`.
-   **`map(float, ...)`**: Used to efficiently convert the input string of numbers into a list of floats.

---

## What You Can Learn

-   **Polynomial Evaluation:** This is a direct demonstration of the standard way to evaluate a polynomial from its coefficients using the NumPy library.
-   **NumPy Workflow:** It shows the simple workflow of reading numerical data, passing it to a NumPy function, and getting a result, which is central to scientific computing in Python.
-   **Horner's Method (Implicit):** While not explicitly coded, `numpy.polyval` uses an efficient algorithm like Horner's method, which is a good concept to be aware of for polynomial evaluation.

---

## Additional Resources

-   [`numpy.polyval` Documentation](https://numpy.org/doc/stable/reference/generated/numpy.polyval.html)
-   [Horner's Method - Wikipedia](https://en.wikipedia.org/wiki/Horner%27s_method)

---

## Conclusion

This solution is a perfect, concise implementation for the given task. It effectively showcases the primary function for polynomial evaluation in NumPy, a fundamental operation in many scientific and engineering domains.

**Happy Coding!**
