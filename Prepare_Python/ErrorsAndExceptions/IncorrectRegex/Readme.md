# Validating Regex Patterns

This repository contains a solution for a HackerRank challenge where you need to determine if a given string is a valid regular expression (regex) or not.

## Problem Statement

You are given a string. Your task is to find out whether the string is a valid regex.

### Input Format
- The first line contains an integer `T`, the number of test cases.
- The next `T` lines each contain a string that represents a regex.

### Output Format
- For each test case, print `"True"` if the regex is valid, otherwise print `"False"`.

#### Sample Input
```
2
.*\+
.*+
```

#### Sample Output
```
True 
False
```

## Key Functions and Modules

### Input Handling
- **`sys.stdin.read()`**  
  Reads the entire input from standard input as a single string.
- **`.splitlines()`**  
  Splits the input string into a list of lines.

### Exception Handling
- **`try` and `except` Blocks:**  
  Used to catch and handle exceptions during execution.
- **`re.error`:**  
  The specific exception raised when a regex compilation fails.

### Regular Expression Handling
- **`re.compile(pattern)`**  
  Attempts to compile the given pattern into a regex object. If the pattern is invalid, it raises a `re.error`.

---

## What You Can Learn

- **Efficient Input Processing:**  
  Learn to use `sys.stdin.read()` combined with `.splitlines()` to handle multi-line input.

- **Parsing and Conversion:**  
  Understand how to convert input strings to the required format using Python functions.

- **Exception Handling:**  
  Learn to use `try`/`except` blocks to catch specific exceptions such as `re.error` and provide custom error handling.

- **Iterating Over Test Cases:**  
  Understand how to process multiple inputs efficiently by iterating over slices of lists.

- **Error Reporting:**  
  Gain experience in handling errors gracefully and outputting appropriate messages.

---

## Additional Resources

- [Wikipedia: Regular Expression](https://en.wikipedia.org/wiki/Regular_expression)
- [Python re Module Documentation](https://docs.python.org/3/library/re.html)

---

## Conclusion

This solution demonstrates how to validate regex patterns using Python's built-in `re` module and robust exception handling. By working through this challenge, you will strengthen your understanding of input processing, exception handling, and regular expressions in Python.

**Happy Coding!**
