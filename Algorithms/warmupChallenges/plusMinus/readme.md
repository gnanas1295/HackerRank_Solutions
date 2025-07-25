# Plus Minus Ratio Challenge

This repository contains an efficient Python solution for the "Plus Minus" challenge, which involves calculating the ratios of positive, negative, and zero elements in an array.

---

## Problem Statement

Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line, formatted to 6 places after the decimal.

### Input Format
- The first line contains an integer, **n**, the size of the array.
- The second line contains **n** space-separated integers.

### Output Format
- Print the following three values, each on a new line:
  1. The ratio of positive values.
  2. The ratio of negative values.
  3. The ratio of zero values.
- Each value must be printed with 6 digits after the decimal.

#### Sample Input

```
6
-4 3 -9 0 4 1
```

#### Sample Output

```
0.500000
0.333333
0.166667
```

## Explanation

In the sample array, there are 6 elements:
- **Positive numbers:** 3, 4, 1 (3 total)
- **Negative numbers:** -4, -9 (2 total)
- **Zeros:** 0 (1 total)

The ratios are calculated as follows:
- **Positive ratio:** 3 / 6 = 0.5
- **Negative ratio:** 2 / 6 = 0.333333...
- **Zero ratio:** 1 / 6 = 0.166667...

Formatted to 6 decimal places, these become the final output.

---

## Key Functions and Modules

### Core Logic
- **Single `for` Loop**: The solution uses a single loop to iterate through the array, making it efficient with a time complexity of O(n).
- **Counters**: Three counter variables are used to keep track of the positive, negative, and zero elements encountered.
- **Formatted Printing**: To meet the output requirements, formatted strings are used. The `f"{value:.6f}"` syntax in an f-string ensures that each ratio is printed as a decimal with exactly six places of precision.

---

## What You Can Learn

- **Basic Array Traversal**: How to efficiently iterate through the elements of a list.
- **Conditional Counting**: Using `if/elif/else` blocks to categorize and count data based on specific conditions.
- **Floating-Point Formatting**: The importance of precise output formatting in programming challenges and how to achieve it in Python for floating-point numbers.

---

## Additional Resources

- [Python String Formatting (f-strings)](https://realpython.com/python-f-strings/)
- [A Guide to the Python For Loop](https://realpython.com/python-for-loop/)

---

## Conclusion

This solution provides a clear and optimal approach to the "Plus Minus" problem. By using a single pass to count the elements and precise string formatting for the output, it correctly and efficiently solves the challenge while adhering to modern Python best practices.

**Happy Coding!** 📊
