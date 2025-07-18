# Set Mutation Operations

This repository contains a Python solution for a problem involving sequential mutation operations on a given set. You will apply various set update operations (`update`, `intersection_update`, `difference_update`, `symmetric_difference_update`) to an initial set and then calculate the sum of its final elements.

---

## Problem Statement

You are given an initial set `A` and a series of `N` other sets. These `N` other sets will perform specific mutation operations on set `A`. Your task is to execute these operations in the given order and then print the sum of all elements remaining in set `A` after all mutations are complete.

The available mutation operations are:
- **`.update()` or `|=`**: Adds elements from another iterable/set to the current set.
- **`.intersection_update()` or `&=`**: Keeps only the elements found in both the current set and another iterable/set.
- **`.difference_update()` or `-=`**: Removes elements found in another iterable/set from the current set.
- **`.symmetric_difference_update()` or `^=`**: Keeps only the elements found in either the current set or another iterable/set, but not in both.

### Input Format
- The first line contains an integer representing the initial number of elements in set `A`. (This value is consumed but not directly used for processing).
- The second line contains a space-separated list of integer elements that constitute the initial set `A`.
- The third line contains an integer `N`, which is the total number of subsequent mutation operations to perform.
- The following `2 * N` lines describe the `N` operations. Each operation consists of two lines:
    - The first line contains two space-separated values: the `operation name` (e.g., "update", "intersection_update") and the `length of the other set` involved in the operation (this length is consumed but not directly used).
    - The second line contains a space-separated list of integer elements belonging to the other set for the current operation.

#### Constraints
- `len(set(A))` (number of elements in set A) is within reasonable limits.
- `len(otherSets)` (number of subsequent operations) is within reasonable limits.
- All elements are integers.

### Output Format
- Print a single integer representing the sum of all elements in set `A` after all operations have been applied.

#### Sample Input

```
 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
```

#### Sample Output
```
38
```

## Explanation

Let's trace the operations with the sample input:

1.  **Initial Set `A`**: `{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 24, 52}`
2.  **`intersection_update` with `{2, 3, 5, 6, 8, 9, 1, 4, 7, 11}`**:
    Set `A` becomes the intersection of itself and the given set.
    `A` = `{1, 2, 3, 4, 5, 6, 7, 8, 9, 11}`
3.  **`update` with `{55, 66}`**:
    Elements from the given set are added to `A`.
    `A` = `{1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 55, 66}`
4.  **`symmetric_difference_update` with `{22, 7, 35, 62, 58}`**:
    `A` becomes elements present in either `A` or the given set, but not both.
    `A` = `{1, 2, 3, 4, 5, 6, 8, 9, 11, 22, 35, 55, 58, 62, 66}` (7 was removed as it was in both)
5.  **`difference_update` with `{11, 22, 35, 55, 58, 62, 66}`**:
    Elements from the given set are removed from `A`.
    `A` = `{1, 2, 3, 4, 5, 6, 8, 9}`

Finally, the sum of elements in `A` is `1 + 2 + 3 + 4 + 5 + 6 + 8 + 9 = 38`.

---

## Key Functions and Modules

### Python Built-in Functions
- **`sys.stdin.read()`**: Reads the entire input from standard input as a single string.
- **`.splitlines()`**: A string method that splits the input string into a list of lines.
- **`map(int, iterable)`**: Applies the `int()` function to each item in the `iterable` (e.g., a list of strings) and returns a map object (which can be converted to a list or set) containing integer values.
- **`set()`**: Constructs a new set object. When passed an iterable, it initializes the set with unique elements from that iterable.
- **`sum(iterable)`**: Calculates the sum of all numeric items in an `iterable`.

### Set Mutation Methods
The core of this solution relies on the in-place set mutation methods:
- **`set.update(other)`**: Adds elements from `other` to the current set.
- **`set.intersection_update(other)`**: Modifies the set to contain only elements common to both sets.
- **`set.difference_update(other)`**: Modifies the set by removing elements also found in `other`.
- **`set.symmetric_difference_update(other)`**: Modifies the set to contain elements found in either set, but not both.

---

## Learning Points

-   **Mutable Set Operations:** This problem highlights the distinction between set operations that return a *new* set (like `union()`, `intersection()`) and those that *mutate* the original set in place (like `update()`, `intersection_update()`). Understanding when to use which is key.
-   **Efficient Input Handling:** Reading all input at once with `sys.stdin.read().splitlines()` can be more efficient for competitive programming problems with many lines of input compared to reading line by line in a loop.
-   **Polymorphism with Dictionaries (Method Dispatch):** Using a dictionary to map string names of operations to their corresponding set methods (`operation_map = {"update": set.update, ...}`) is a powerful and Pythonic way to implement conditional logic. It makes the code cleaner, more readable, and easily extensible if new operations were added.
-   **Early Type Conversion:** Converting input strings to integers (`map(int, ...)` ) as soon as they are parsed simplifies subsequent operations and prevents type-related errors.

---

## Additional Resources

-   [Python Sets Documentation](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
-   [Python `map()` function](https://docs.python.org/3/library/functions.html#map)
-   [Python `sys` module](https://docs.python.org/3/library/sys.html)

---

**Ready for the next set challenge?**