# Newspaper Subscription Analysis

This repository contains a Python solution to determine the number of students subscribed to either an English or a French newspaper, but not both. This is a classic set theory problem involving the symmetric difference of two sets.

---

## Problem Statement

Students of District College have subscriptions to English and French newspapers. Some students have subscribed to English only, some have subscribed to French only, and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.

### Input Format
- The first line contains the number of students who have subscribed to the English newspaper. (This line is consumed but not used in the calculation).
- The second line contains a space-separated list of student roll numbers who have subscribed to the English newspaper.
- The third line contains the number of students who have subscribed to the French newspaper. (This line is consumed but not used in the calculation).
- The fourth line contains a space-separated list of student roll numbers who have subscribed to the French newspaper.

### Output Format
- Print the total number of students who have subscriptions to the English or the French newspaper but not both.

#### Sample Input

```
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```

#### Sample Output
```
8
```

## Explanation

The problem asks for students who subscribe to *either* English *or* French, but *not both*. This is the definition of the [symmetric difference](https://en.wikipedia.org/wiki/Symmetric_difference) between two sets.

Given:
- English subscribers set: `{1, 2, 3, 4, 5, 6, 7, 8, 9}`
- French subscribers set: `{10, 1, 2, 3, 11, 21, 55, 6, 8}`

The students who subscribe to *both* are the intersection: `{1, 2, 3, 6, 8}`.

The students who subscribe to *English only* are: `{4, 5, 7, 9}`.
The students who subscribe to *French only* are: `{10, 11, 21, 55}`.

The union of English-only and French-only subscribers is the symmetric difference: `{4, 5, 7, 9, 10, 11, 21, 55}`.
The count of these students is 8.

Python's `set` data structure provides a built-in method `symmetric_difference()` that efficiently computes this. We read the roll numbers into two sets and then apply this operation, finally taking the `len()` of the resulting set to get the count.

---

## Key Functions and Modules

### Built-in Functions
- **`input()`**: Used to read a line of text from standard input.
- **`split()`**: A string method that splits a string into a list of substrings based on a delimiter (space by default).
- **`len()`**: Returns the number of items (length) of an object. In this case, it's used to count the elements in the resulting set.

### Set Data Structure
- **`set()`**: A built-in Python data type that represents an unordered collection of unique elements. It is highly efficient for membership testing and set operations.
- **`set.symmetric_difference(other_set)`**: Returns a new set containing all elements that are in either `set` or `other_set` but not in their intersection. This is equivalent to `(set - other_set) | (other_set - set)`.

---

## Learning Points

- **Understanding Set Operations:** This problem is a direct application of the symmetric difference set operation. Understanding common set operations (union, intersection, difference, symmetric difference) is crucial for efficiently solving problems involving unique collections of items.
- **Efficient Data Structures:** Using Python's built-in `set` is highly efficient for this type of problem. Set operations are optimized and often run in close to O(N) time (where N is the number of elements), making them suitable for large datasets.
- **Concise Python Code:** Python's rich standard library allows for very concise and readable solutions to problems that might require more verbose code in other languages.

---

## Useful Reference Links

- [Python Sets Documentation](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Python `set.symmetric_difference()` Method](https://docs.python.org/3/library/stdtypes.html#frozenset.symmetric_difference)
- [Symmetric Difference on Wikipedia](https://en.wikipedia.org/wiki/Symmetric_difference)

---

**Happy Coding!**