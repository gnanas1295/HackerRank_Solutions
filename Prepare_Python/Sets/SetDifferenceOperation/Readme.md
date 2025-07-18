# English Only Newspaper Subscribers

This repository contains a Python solution to identify and count students who have subscribed exclusively to the English newspaper.

---

## Problem Statement

Students of District College have subscriptions to English and French newspapers. Some students have subscribed only to the English newspaper, some have subscribed only to the French newspaper, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to **only English** newspapers.

### Input Format
- The first line contains $N$, the number of students who have subscribed to the English newspaper.
- The second line contains $N$ space-separated roll numbers of those students.
- The third line contains $M$, the number of students who have subscribed to the French newspaper.
- The fourth line contains $M$ space-separated roll numbers of those students.

### Constraints
(Note: The problem description did not provide explicit constraints, so a placeholder is used. In a real scenario, you'd add constraints like $0 < N, M < 1000$ and roll numbers being integers within a certain range.)
- Roll numbers will be unique within each list.
- Roll numbers are represented as strings in the input for simplicity, but conceptually they are identifiers.

### Output Format
- Output the total number of students who are subscribed to the English newspaper only.

#### Sample Input

```
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```

#### Sample Output

```
4
```

## Explanation

The problem requires us to find the students who are in the English subscriber list but *not* in the French subscriber list. This is a classic set difference operation.

- **Input Processing:** The code first reads the total count of students for both English and French newspapers (these counts are not directly used in the logic but are consumed from the input stream). Then, it reads the space-separated roll numbers for English subscribers and converts them into a Python `set`. Similarly, it processes the French subscribers into another `set`. Using `set`s is crucial because they automatically handle uniqueness and provide efficient set operations.

- **Finding the Difference:** Python's `set` data structure offers the `.difference()` method (or the `-` operator). When `english_subscribers.difference(french_subscribers)` is called, it returns a new set containing all elements that are present in `english_subscribers` but *not* in `french_subscribers`. These elements precisely represent the students subscribed *only* to the English newspaper.

- **Counting the Result:** Finally, the `len()` function is applied to the resulting difference set to get the count of these unique students, which is then printed as the final answer.

## Key Functions and Modules

### Built-in Functions
- **`input()`**: Used to read a line of input from standard input (STDIN).
- **`split()`**: A string method that splits a string into a list of substrings based on a delimiter (space by default).
- **`len()`**: Returns the number of items (length) of an object, such as a set or a list.

### Set Data Structure
- **`set()`**: A built-in Python data structure that stores an unordered collection of unique elements. It is highly efficient for operations like checking membership, union, intersection, and difference.
- **`.difference()`**: A method of set objects that returns a new set containing elements that are present in the set but not in the specified iterable(s). The `-` operator can also be used for difference between two sets.

## Learning Points

- **Using Sets for Unique Differences:** This problem highlights how Python's `set` data structure is ideal for finding elements that are present in one collection but absent from another.
- **Efficiency of Set Operations:** Set difference operations are highly optimized in Python, offering excellent performance even with large datasets.
- **Conciseness and Readability:** The solution demonstrates how powerful set operations can lead to very compact and easy-to-understand code for problems involving unique elements and their relationships.
- **Handling Unused Input:** The use of `_ = input()` is a good practice for consuming input lines that are part of the specified input format but not directly needed for the program's core logic.

## Useful Reference Links

- [Python Set Documentation](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Python Built-in Functions: input()](https://docs.python.org/3/library/functions.html#input)
- [Python Built-in Functions: len()](https://docs.python.org/3/library/functions.html#len)
- [String Methods: split()](https://docs.python.org/3/library/stdtypes.html#str.split)

---

## Conclusion

This solution effectively demonstrates the application of Python's `set` data structure and its `difference()` method to solve problems that require identifying unique elements in one collection that are not present in another. By leveraging set operations, you can write elegant and efficient code for similar data analysis tasks.

**Happy Coding!**
