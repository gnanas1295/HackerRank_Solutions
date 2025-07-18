# Python Divmod and Basic Arithmetic

## Problem Statement

This problem demonstrates the use of basic arithmetic operators and the built-in `divmod()` function in Python. You are required to read two integers, say `a` and `b`, and then perform three operations:

1.  Integer division of `a` by `b`.
2.  Modulo operation of `a` by `b`.
3.  Calculate the `divmod()` of `a` and `b`.

The results of these operations must be printed on separate lines.

**Example:**
If `a = 177` and `b = 10`:
* Integer division (`177 // 10`) is `17`.
* Modulo operation (`177 % 10`) is `7`.
* `divmod(177, 10)` returns `(17, 7)`.

## Input Format

The input consists of two lines:
* The first line contains the integer `a`.
* The second line contains the integer `b`.

## Output Format

Print three lines:
* The first line should be the result of the integer division ($a // b$).
* The second line should be the result of the modulo operation ($a \% b$).
* The third line should be the tuple returned by `divmod(a, b)`.

## Sample Input

```
177
10
```

## Sample Output

```
17
7
(2, 3)
```

## Explanation

The problem tests fundamental Python arithmetic operations and knowledge of the `divmod()` built-in function.

1.  **Integer Division (`//`)**: This operator performs division and returns only the integer part of the quotient, truncating any fractional part. For positive numbers, it behaves like floor division. For example, $177 // 10 = 17$.

2.  **Modulo Operator (`%`)**: This operator returns the remainder of the division. For example, $177 \% 10 = 7$.

3.  **`divmod(a, b)` Function**: This is a powerful built-in Python function that takes two arguments, a dividend `a` and a divisor `b`. It efficiently returns a tuple containing both the quotient (from integer division) and the remainder (from the modulo operation) in a single call. This is equivalent to `(a // b, a % b)`.

The solution reads the two integers, then directly applies these operations and prints the results as specified.

## Key Functions and Modules Used

* **`input()`**: Built-in Python function used to read a line of text from standard input. The input is always read as a string, so type conversion is necessary.
* **`int()`**: Built-in Python function used to convert a string or a number to an integer.
* **Integer Division Operator (`//`)**: Performs floor division, returning the integer part of the quotient.
* **Modulo Operator (`%`)**: Returns the remainder of a division.
* **`divmod(a, b)`**: Built-in Python function that returns a tuple containing the quotient and the remainder of `a` divided by `b`.
* **`print()`**: Built-in Python function used to display output to standard output.

## Learning Points

* **Understanding Basic Arithmetic Operators**: Reinforces the understanding of integer division (`//`) and the modulo operator (`%`).
* **Efficiency with `divmod()`**: Learning about `divmod()` is crucial as it's more efficient than calculating quotient and remainder separately, especially when both are needed, as it performs the division operation only once.
* **Python's Built-in Functions**: Demonstrates the utility of Python's rich set of built-in functions for common tasks.
* **Standard Input/Output**: Practices reading input from `STDIN` and printing output to `STDOUT`.

## Useful Reference Links

* [Python Built-in Functions - `divmod()`](https://docs.python.org/3/library/functions.html#divmod)
* [Python Arithmetic Operators](https://docs.python.org/3/reference/expressions.html#arithmetic-operations)
* [Python `input()` and `print()`](https://docs.python.org/3/library/functions.html#input)
