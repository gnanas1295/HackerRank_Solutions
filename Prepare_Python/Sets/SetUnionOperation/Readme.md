# Newspaper Subscription Union Challenge

## Problem Statement

Students at District College subscribe to English and French newspapers. Some subscribe to both. Given two sets of student roll numbers representing subscriptions for each newspaper, determine the total number of unique students who have at least one subscription.

## Input Format

- The first line contains an integer, **n**, the number of students subscribed to the English newspaper.
- The second line contains **n** space-separated roll numbers.
- The third line contains an integer, **m**, the number of students subscribed to the French newspaper.
- The fourth line contains **m** space-separated roll numbers.

## Output Format

- Output a single integer representing the total number of students who have subscribed to at least one newspaper.

## Sample Input

```
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```

## Sample Output
```
13
```


## Explanation

- The English subscribers are: {1, 2, 3, 4, 5, 6, 7, 8, 9}
- The French subscribers are: {10, 1, 2, 3, 11, 21, 55, 6, 8}
- The union of both sets (students with at least one subscription) is: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21, 55}
- Thus, there are 13 unique students.

## Key Functions and Modules Used

- **`set` and Set Operations:**  
  - The `set` data structure is used to store unique elements.
  - The union operator `|` is used to combine two sets while automatically eliminating duplicates.

- **`sys.stdin.read()` and `.splitlines()`:**  
  These functions are used to read all input data at once and split it into individual lines for processing.

## What You Can Learn

- **Set Operations in Python:**  
  Gain an understanding of how to use sets for union operations and why sets are ideal for handling unique items.

- **Efficient Input Handling:**  
  Learn how to handle multi-line input efficiently using `sys.stdin.read()`.

- **Code Readability and Conciseness:**  
  Understand the benefits of using built-in operators (like `|` for union) to write concise and expressive code.

## Additional Resources

- [Python Sets Documentation](https://docs.python.org/3/tutorial/datastructures.html#set)
- [Python sys Module Documentation](https://docs.python.org/3/library/sys.html)
- [Python Union Operator for Sets](https://docs.python.org/3/library/stdtypes.html#set.union)

## Conclusion

This challenge demonstrates the power of Python's set operations to handle real-world problems like finding unique elements across datasets. By working through this challenge, you'll enhance your skills in input handling, set operations, and writing clean, efficient code.

**Happy Coding!**
