# Athlete Data Sorter

This repository contains a Python solution for a problem that involves sorting a 2D list (a table of athlete data) based on a specific attribute (column).

---

## Problem Statement

You are given a spreadsheet of **N** athletes and **M** attributes. Your task is to sort this data based on the **k-th** attribute and print the resulting sorted table. The sort should be stable, meaning if two rows have the same value for the k-th attribute, their original relative order should be maintained.

### Input Format
- The first line contains integers **N** and **M**.
- The next **N** lines each contain **M** integer elements.
- The last line contains the integer **k**, the zero-indexed column to sort by.

### Output Format
- Print the **N** lines of the sorted table, with elements in each line separated by spaces.

#### Sample Input

```
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
```

#### Sample Output

```
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
```

## Explanation

The solution reads the table dimensions, the table data itself, and the sort key `k`. The core logic is encapsulated in a function that performs the sorting and printing.

1.  **Sorting:** The built-in `sorted()` function is used to sort the list of lists (`arr`).
2.  **Custom Key:** A `lambda` function is passed to the `key` parameter of `sorted()`. This function, `lambda age: age[k]`, tells the sorting algorithm to look only at the element at index `k` in each inner list (row) for its comparison.
3.  **Stable Sort:** Python's `sorted()` function is inherently "stable." This means if two rows have the same value at index `k`, their original order is preserved, which satisfies a key requirement of the problem.
4.  **Printing:** The code then iterates through the newly sorted list. For each row, it uses the `print(*row)` syntax. The splat/unpack operator (`*`) turns the list `[7, 1, 0]` into separate arguments `7, 1, 0`, which `print()` then outputs with spaces in between by default.

---
## Algorithm Used

This solution uses a **custom sort** algorithm, leveraging Python's built-in `Timsort` (the algorithm behind `sorted()`). It does not require implementing a sorting algorithm from scratch but rather demonstrates how to control the behavior of a highly optimized, existing one.

---
## Key Functions and Modules

### Core Logic
- **`sorted(iterable, key=function)`**: The primary built-in function for sorting. It creates a new sorted list from the items in an iterable.
- **`key` parameter**: A crucial argument that specifies a function to be called on each list element prior to making comparisons.
- **`lambda` function**: Used to create a small, anonymous function on the fly. Here, it's used to efficiently extract the k-th element from each row.
- **`*` (Splat/Unpack Operator)**: Used to unpack the elements of a list into individual arguments for a function, which is perfect for printing space-separated values.

---

## What You Can Learn

-   **Custom Sorting:** How to sort complex data structures in Python based on a specific attribute or key.
-   **Lambda Functions:** The power and convenience of using `lambda` for short, simple functions, especially as keys for sorting.
-   **Stable Sorting:** An understanding of what a "stable" sort is and that Python's default sort implementation provides this feature.
-   **Argument Unpacking:** A useful Python trick (`*`) for cleaner code when dealing with functions that accept multiple arguments, like `print()`.

---

## Additional Resources

-   [Python Sorting HOW TO Guide](https://docs.python.org/3/howto/sorting.html)
-   [Python `lambda` Expressions](https://docs.python.org/3/reference/expressions.html#lambda)

---

## Conclusion

This solution is a perfect example of writing clean, efficient, and "Pythonic" code. It leverages Python's powerful built-in sorting capabilities and functional programming features (`lambda`) to solve the problem in a very concise and readable way.

**Happy Coding!**
