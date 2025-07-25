# Python Powers and Modular Exponentiation

## Problem Statement

This problem focuses on calculating powers (exponents) in Python, including standard exponentiation and modular exponentiation. You are given three integers: `a`, `b`, and `m`.

Your task is to print two lines:
1.  The result of $a^b$.
2.  The result of $a^b \pmod m$.

Python provides a convenient built-in `pow()` function and the `**` operator for these calculations. Specifically, `pow(a, b, m)` is very useful for efficiently computing modular exponentiation.

## Input Format

The input consists of three lines:
* The first line contains the integer `a`.
* The second line contains the integer `b`.
* The third line contains the integer `m`.

## Constraints

* The problem does not specify numerical constraints for `a`, `b`, or `m`, but implies they fit within standard integer types for `pow()` operations.
* For `pow(a, b, m)`, `m` cannot be negative.

## Sample Input

```
3
4
5
```

## Sample Output
```
81
1
```

## Explanation

This problem leverages Python's built-in capabilities for exponentiation.

1.  **Standard Exponentiation ($a^b$)**:
    This calculates `a` raised to the power of `b`. Python offers two primary ways to do this:
    * **Exponentiation Operator (`**`)**: `a ** b` is the most common and often preferred syntax for simple power calculations in Python.
    * **`pow(a, b)` function**: This function also calculates $a^b$.

    In the sample input: $3^4 = 3 \times 3 \times 3 \times 3 = 81$.

2.  **Modular Exponentiation ($a^b \pmod m$)**:
    This calculates `a` raised to the power of `b`, and then finds the remainder when that result is divided by `m`. This operation is crucial in cryptography and number theory. Python's `pow()` function has a special three-argument form, `pow(a, b, m)`, which efficiently computes this.

    **Why `pow(a, b, m)` is important:**
    Naively calculating $(a^b) \% m$ by first computing $a^b$ can lead to extremely large intermediate numbers, causing overflow errors or significant performance issues, especially when `a` and `b` are large. The `pow(a, b, m)` function performs the modular operations at each step of the exponentiation, keeping intermediate results small and preventing overflow.

    In the sample input:
    * $3^4 = 81$
    * $81 \pmod 5 = 1$ (since $81 = 16 \times 5 + 1$).
    Thus, `pow(3, 4, 5)` returns `1`.

## Key Functions and Modules Used

* **`input()`**: Built-in Python function used to read a line of text from standard input.
* **`int()`**: Built-in Python function used to convert a string to an integer.
* **Exponentiation Operator (`**`)**: An infix operator for calculating powers.
* **`pow(base, exp[, mod])`**: A versatile built-in Python function:
    * `pow(a, b)`: Returns $a^b$.
    * `pow(a, b, m)`: Returns $a^b \pmod m$. This is particularly efficient for modular exponentiation.
* **`print()`**: Built-in Python function to display results to standard output.

## Learning Points

* **Multiple Ways to Compute Powers**: Understanding both `**` and `pow()` for standard exponentiation.
* **Efficient Modular Exponentiation**: Recognizing the importance and utility of `pow(a, b, m)` for computing $(a^b) \pmod m$ without intermediate overflow. This is a fundamental concept in computational number theory.
* **Handling Large Numbers**: Implicitly, this problem touches upon how Python handles arbitrarily large integers, and how `pow(a, b, m)` specifically optimizes for large exponents in modular arithmetic contexts.
* **Reading Multiple Inputs**: Practice reading multiple distinct inputs from `STDIN`.

## Useful Reference Links

* [Python Built-in Functions - `pow()`](https://docs.python.org/3/library/functions.html#pow)
* [Python Arithmetic Operators](https://docs.python.org/3/reference/expressions.html#arithmetic-operations)
* [Modular Exponentiation (Wikipedia)](https://en.wikipedia.org/wiki/Modular_exponentiation)
