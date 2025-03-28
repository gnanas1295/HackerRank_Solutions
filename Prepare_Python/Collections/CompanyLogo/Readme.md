# Top Three Most Common Characters Logo Challenge

## Problem Statement

A newly opened multinational brand wants its company logo to feature the three most common characters in its company name. Given a string representing the company name in lowercase letters, your task is to find the top three most common characters in the string and print them along with their occurrence counts.

## Input Format

- A single line of input containing the company name string.

## Output Format

- Print the three most common characters along with their occurrence counts on separate lines.
- The output should be sorted in descending order by the occurrence count.
- If two characters have the same occurrence count, they should be sorted in alphabetical order.

## Sample Input

```
aabbbccde
```

## Sample Output

```
b 3
a 2
c 2
```


## Explanation

- The character `b` occurs 3 times, so it appears first.
- Both `a` and `c` occur 2 times. Since `a` comes before `c` alphabetically, `a` is printed before `c`.

## Key Functions and Modules Used

- **`collections.Counter`**  
  A convenient tool to count the frequency of elements in an iterable. It simplifies the process of creating a dictionary of counts.

- **`sorted()` with a Lambda Key Function**  
  The lambda function (`lambda x: (-x[1], x[0])`) sorts the items:
  - First, by the negative of the count (i.e., in descending order).
  - Second, by the character itself in alphabetical order.

- **`sys.stdin` / `input()`**  
  Used for reading the input data.

## What You Can Learn

- **Efficient Counting:**  
  Leveraging the `Counter` class to count elements quickly without manual loops.

- **Custom Sorting:**  
  How to sort items using multiple criteria by providing a custom key function to `sorted()`.

- **Python Standard Library:**  
  Utilizing built-in modules to write concise, readable, and efficient code.

## Additional Resources

- [Python collections.Counter Documentation](https://docs.python.org/3/library/collections.html#collections.Counter)
- [Sorting HOW TO – Python Documentation](https://docs.python.org/3/howto/sorting.html)
- [Python Lambda Functions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)

## Conclusion

This challenge demonstrates how to combine efficient counting with custom sorting to solve a common problem in a concise manner. By working through this challenge, you’ll gain valuable insights into using Python’s standard library for practical data processing tasks.

**Happy Coding!**