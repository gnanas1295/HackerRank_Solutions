# Integer Division Exception Handling

This repository contains a solution for a HackerRank challenge that involves performing integer division with proper exception handling. The problem requires you to read test cases where each test case consists of two values. You must perform integer division and print the result. If a `ZeroDivisionError` or `ValueError` occurs, the corresponding error code should be printed.

---

## Problem Statement

Given two values **a** and **b**, perform integer division `a // b` and print the result.  
In case of an error (i.e., division by zero or an invalid literal), print the error code.

### Input Format
- The first line contains an integer `t`, the number of test cases.
- Each of the next `t` lines contains two space-separated values.

### Output Format
- For each test case, print the result of the integer division.
- If an exception occurs, print the error code in the format:  
  `Error Code: <error message>`

#### Sample Input
```
3 
1 0 
2 $ 
3 1
```

#### Sample Output
```
Error Code: integer division or modulo by zero 
Error Code: invalid literal for int() with base 10: '$' 
3
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
- **`ZeroDivisionError`:**  
  Raised when division or modulo operation is attempted with a zero divisor.
- **`ValueError`:**  
  Raised when an operation receives an argument with the correct type but an inappropriate value (e.g., converting a non-numeric string to int).

### Additional Topics Covered
- **Integer Division:**  
  Using the `//` operator for integer division in Python.
- **Exception Messages:**  
  How to retrieve and display the error message from an exception.

---

## What You Can Learn

- **Efficient Input Processing:**  
  Using `sys.stdin.read()` combined with `.splitlines()` to handle multi-line input.

- **Parsing and Conversion:**  
  Converting input strings to integers using `map()` and handling potential conversion errors.

- **Exception Handling:**  
  Using `try`/`except` blocks to catch specific exceptions (`ZeroDivisionError` and `ValueError`) and print a custom error message.

- **Iterating Over Test Cases:**  
  Using a simple loop to process each test case line by line.

- **Error Reporting:**  
  Displaying the error code as specified when an exception is encountered.

---

## Additional Resources

- [Python Exceptions Documentation](https://docs.python.org/2/library/exceptions.html#module-exceptions)
- [Python sys Module Documentation](https://docs.python.org/3/library/sys.html)
- [Python int() Function Documentation](https://docs.python.org/3/library/functions.html#int)

---

## Conclusion

This solution demonstrates how to perform integer division with robust exception handling in Python. It shows how to gracefully handle errors such as division by zero and invalid input values, ensuring that the program outputs the correct error messages when necessary.

**Happy Coding!**
