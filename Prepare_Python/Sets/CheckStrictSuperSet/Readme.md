# Set Superset Checker

This repository provides a Python solution to determine if a primary set (`A`) is a superset of all subsequent input sets (`B_i`).

---

## Problem Statement

You are given a primary set, `A`. Subsequently, you will be given `T` additional sets, `B_1, B_2, ..., B_T`. Your task is to determine if set `A` is a superset of *all* these `B` sets.

- If set `A` is a superset of `B_i` for *every* `i` from `1` to `T`, print `True`.
- If set `A` is *not* a superset of *any* `B_i` (i.e., at least one `B_i` contains an element not in `A`), print `False`.

### Input Format

- The first line contains space-separated integer elements of set `A`.
- The second line contains an integer `T`, representing the number of subsequent sets (`B_i`) to check.
- Following `T` lines, each contains space-separated integer elements for a set `B_i`.

### Output Format

Print `True` or `False` on a single line.

#### Sample Input

```
1 2 3 4 5 6 7 8 9 10
3
1 2 3
4 5 6
7 8 9 11
```

#### Sample Output
```
False
```

#### Explanation of Sample Input/Output

- **Set A:** `{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}`
- **Number of B sets (T):** `3`
- **Set B_1:** `{1, 2, 3}` (A is a superset of B_1: True)
- **Set B_2:** `{4, 5, 6}` (A is a superset of B_2: True)
- **Set B_3:** `{7, 8, 9, 11}` (A is NOT a superset of B_3, because `11` is in B_3 but not in A: False)

Since A is not a superset of all B sets (specifically B_3), the output is `False`. If all checks had passed, the output would be `True`.

---

## Key Functions and Modules Used

### Input Handling
- **`sys` module:** Provides access to system-specific parameters and functions, including `sys.stdin` for reading input.
- **`sys.stdin.readline()`:** Reads a single line from standard input, including the newline character. This is generally efficient for competitive programming.
- **`.split()`:** A string method that splits a string by whitespace (default) and returns a list of substrings.
- **`map(int, ...)`:** Applies the `int` function to each item in an iterable (the list of string numbers), effectively converting them to integers.

### Set Data Structure
- **`set()` constructor:** Creates a set object from an iterable. Sets are unordered collections of unique elements, making them ideal for membership testing.
- **`set.issuperset(other_set)`:** A method of the set object that returns `True` if all elements in `other_set` are also present in the calling set. This operation is highly optimized for performance.

### Control Flow and Logic
- **`all()` built-in function:** Returns `True` if all elements of the iterable are true. Crucially, it short-circuits, meaning it stops processing and returns `False` as soon as it encounters a false element. This is vital for efficiency when you need to check if *all* conditions are met.
- **Generator Expression (`(... for ... in ...)`):** An efficient way to create iterators. Unlike list comprehensions, they do not construct an entire list in memory, making them suitable for large datasets or when used with functions like `all()` or `any()` that consume items one by one.

---

## What You Can Learn

- **Leveraging Python's Set Operations:** Effectively using built-in set methods like `issuperset()` for robust and performant collection comparisons.
- **Pythonic "All True" Checks:** Employing the `all()` function with generator expressions for concise, readable, and efficient validation of multiple conditions. This pattern is widely used in idiomatic Python.
- **Efficient Input Reading:** Understanding the use of `sys.stdin.readline()` for optimal input processing in competitive programming scenarios.
- **Code Conciseness and Readability:** How to write clean and compact code without sacrificing clarity, by combining powerful Python features.

---

## Useful Reference Links

- [Python `set` Documentation](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
- [Python `sys` Module Documentation](https://docs.python.org/3/library/sys.html)
- [Python `map()` Function](https://docs.python.org/3/library/functions.html#map)
- [Python `all()` Function](https://docs.python.org/3/library/functions.html#all)
- [Python Generator Expressions](https://docs.python.org/3/glossary.html#term-generator-expression)

---

**Happy Coding!**
