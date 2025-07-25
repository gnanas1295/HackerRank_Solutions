# Mini-Max Sum Challenge

This repository contains an efficient Python solution for the "Mini-Max Sum" problem, a challenge focused on array manipulation and logical thinking.

---

## Problem Statement

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Print the respective minimum and maximum values as a single line of two space-separated integers.

### Input Format
- A single line containing five space-separated integers.

### Output Format
- Print two space-separated long integers on one line: the minimum sum and the maximum sum.

#### Sample Input

```
1 2 3 4 5
```

#### Sample Output
```
10 14
```

## Explanation

To get the minimum possible sum from four of the five numbers, you should exclude the largest number from the total sum.
-   `Sum = 1 + 2 + 3 + 4 + 5 = 15`
-   `Largest number = 5`
-   `Minimum Sum = 15 - 5 = 10`

To get the maximum possible sum, you should exclude the smallest number from the total sum.
-   `Smallest number = 1`
-   `Maximum Sum = 15 - 1 = 14`

---

## Key Functions and Modules

### Core Logic
The most efficient solution avoids sorting the array.
-   **`sum(iterable)`**: This built-in function is used to calculate the sum of all five integers in a single pass.
-   **`min(iterable)`**: Finds the smallest integer in the array.
-   **`max(iterable)`**: Finds the largest integer in the array.

By combining these, we can find the min and max sums with simple arithmetic, which is more performant than sorting.

---

## What You Can Learn

-   **Algorithmic Shortcuts**: How to find a simpler logical path to the answer (e.g., subtracting from the total sum instead of summing all subsets).
-   **Efficiency**: Understanding that a linear scan using `min()` and `max()` is often faster ($O(N)$) than sorting the entire array ($O(N \log N)$).
-   **Integer Overflow**: This problem highlights the need to be mindful of data types, as sums can exceed the capacity of a standard 32-bit integer in some languages. Python's arbitrary-precision integers handle this automatically.

---

## Additional Resources

-   [Python Built-in Functions: sum(), min(), max()](https://docs.python.org/3/library/functions.html)

---

## Conclusion

This solution demonstrates an elegant and efficient approach to the Mini-Max Sum problem. By identifying the logical shortcut, we can solve the problem with minimal computation, resulting in clean, readable, and performant code.

**Happy Coding!** ➕
