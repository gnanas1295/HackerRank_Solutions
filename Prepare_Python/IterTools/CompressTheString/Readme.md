# Groupby Compression Challenge

## Problem Statement

You are given a string containing digits. Your task is to compress the string by replacing groups of consecutive identical digits with a tuple representing the count of occurrences and the digit itself.

## Input Format

- A single line of input consisting of the string.
- The string contains only digits (0-9).

## Output Format

- A single line of output containing the compressed string.
- Each group should be formatted as `(count, digit)` and separated by a single space.

## Sample Input

```
1222311
```

## Sample Output
```
(1, 1) (3, 2) (1, 3) (2, 1)
```


## Explanation

- The digit `1` appears once at the beginning, so it is replaced by `(1, 1)`.
- Next, the digit `2` appears three times consecutively, so it is replaced by `(3, 2)`.
- Then, the digit `3` appears once, so it is replaced by `(1, 3)`.
- Finally, the digit `1` appears twice consecutively at the end, so it is replaced by `(2, 1)`.
- The final output is all these tuples joined by a space.

## Key Functions and Modules Used

- **`itertools.groupby()`**  
  Groups consecutive identical elements in an iterable. This function is essential for grouping the characters that appear consecutively in the input string.

- **`sys.stdin.read()`**  
  Reads the entire input from standard input, which is then processed by the program.

- **`str.strip()`**  
  Removes any leading or trailing whitespace from the input string to ensure that only valid characters are processed.

- **`list()` and `len()`**  
  Used to convert the group iterator into a list in order to count the number of elements in each group.

- **`str.join()`**  
  Joins the formatted tuples into a single string with a space between each tuple.

## What You Can Learn

- **Using `itertools.groupby`:**  
  Learn how to group consecutive elements in an iterable effectively, which is a common pattern in problems dealing with sequence compression or run-length encoding.

- **Efficient Input Handling:**  
  Understand how to use `sys.stdin.read()` and `strip()` to manage and clean input data.

- **String Manipulation and Formatting:**  
  Gain experience in processing strings and formatting outputs to meet specific problem requirements.

## Additional Resources

- [Python itertools Documentation](https://docs.python.org/3/library/itertools.html#itertools.groupby)
- [Python sys Module Documentation](https://docs.python.org/3/library/sys.html)
- [Python String Methods](https://docs.python.org/3/library/stdtypes.html#str.strip)
- [Real Python: Itertools Tutorial](https://realpython.com/python-itertools/)

## Conclusion

This solution demonstrates the usefulness of the `itertools.groupby()` function for grouping consecutive identical elements in a string and applying run-length encoding. By working through this challenge, you will deepen your understanding of input processing, grouping data, and efficient string manipulation in Python.

**Happy Coding!**