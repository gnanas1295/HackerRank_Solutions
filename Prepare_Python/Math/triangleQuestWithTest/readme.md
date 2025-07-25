# Arithmetic Numerical Triangle

This repository contains a Python solution for a challenge that requires printing a numerical triangle using only arithmetic operations.

---

## Problem Statement
You are given a positive integer, N. Your task is to print a numerical triangle of height N-1. The challenge is to do this using only arithmetic operations, a single `for` loop, and a single `print` statement. String manipulation is not allowed.

### Input Format
- A single integer, **N**.

### Output Format
- Print N-1 lines of the numerical triangle.

#### Sample Input

```
5
```


#### Sample Output
```
1
22
333
4444
```

## Algorithm Explanation
This problem is a mathematical puzzle rather than a traditional data structure or algorithm challenge. The solution relies on a clever formula to generate the pattern for each line.

The core of the algorithm is to first generate a "repunit" (a number consisting of only the digit 1) and then multiply it by the current line number.

1.  **Generating Repunits:** A number like `1`, `11`, `111`, etc., can be generated arithmetically. The formula for a repunit of length `i` is:
    $$(10^i - 1) / 9$$
    For example, when `i = 3`, this becomes $(10^3 - 1) / 9 = 999 / 9 = 111$.

2.  **Generating the Line:** To get the final output for a given line `i` (e.g., `333`), we simply take the repunit of length `i` (which is `111`) and multiply it by `i`.
    -   Line 1: `( (10^1 - 1) / 9 ) * 1 = 1 * 1 = 1`
    -   Line 2: `( (10^2 - 1) / 9 ) * 2 = 11 * 2 = 22`
    -   Line 3: `( (10^3 - 1) / 9 ) * 3 = 111 * 3 = 333`

This single formula, when placed inside the loop, solves the problem.

---

## Key Concepts
-   **Repunit:** A number consisting of repeated instances of the digit 1. The formula to generate them is a key part of this puzzle.
-   **Integer Division (`//`)**: In Python, using `//` ensures the result of the division is an integer, which is necessary for this problem.
-   **Exponentiation Operator (`**`)**: Used to calculate powers of 10 as part of the formula.

---

## What You Can Learn
-   **Mathematical Problem-Solving**: How to approach pattern-based problems from a mathematical perspective rather than a string manipulation one.
-   **Arithmetic Formulas**: Discovering the powerful formula for generating repunits and applying it to a practical problem.
-   **Thinking Within Constraints**: How to be creative with a limited set of tools (only arithmetic operations) to achieve a complex output.

---

## Additional Resources
-   [Wikipedia: Repunit](https://en.wikipedia.org/wiki/Repunit)

---

## Conclusion
This solution demonstrates an elegant intersection of mathematics and programming. By using the arithmetic formula for repunits, we can solve a seemingly complex pattern-printing problem in a single, efficient line of code that respects all the problem's constraints.

**Happy Coding!** 📐
