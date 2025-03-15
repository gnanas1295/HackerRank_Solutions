# Student Marks Average Calculator Using Namedtuple

This repository contains a solution for calculating the average marks of students from a spreadsheet-like input using Python's `namedtuple`. The solution leverages efficient input processing and Python’s powerful data structures to handle a dynamic order of columns.

---

## Problem Statement

Dr. John Wesley has a spreadsheet containing a list of students with the columns: `ID`, `MARKS`, `NAME`, and `CLASS`. The columns can appear in any order. Your task is to calculate the average marks of the students and print it, corrected to 2 decimal places.

### Input Format

- The first line contains an integer `N`, the total number of students.
- The second line contains the names of the columns in any order.
- The next `N` lines each contain the details of a student corresponding to the column names.

### Output Format

Print the average marks of the students rounded to 2 decimal places.

#### Sample Input
```
5 
ID MARKS NAME CLASS 
1 97 Raymond 7 
2 50 Steven 4 
3 91 Adrian 9 
4 72 Stewart 5 
5 80 Peter 6
```

#### Sample Output

```
78.00
```

## Explanation

### Input Processing:
- We read the input using `sys.stdin.read()` and split it into lines using `.splitlines()`.
- The first line gives the number of students, and the second line contains the column names (order may vary).

### Using `namedtuple`:
- We define a `Student` namedtuple using the column names.
- The expression `Student(*line.split())` unpacks the list returned by `line.split()` into separate arguments.
  - For example, if `line.split()` returns `["1", "97", "Raymond", "7"]`, then `Student(*line.split())` is equivalent to `Student("1", "97", "Raymond", "7")`.
- This is crucial because passing the list as a single argument with `Student(line.split())` would not work; the namedtuple constructor expects each field as a separate argument.

### Calculating the Average:
- We iterate over each student record (from the third line onward), extract the `MARKS` field, convert it to an integer, and sum all the marks.
- Finally, we compute the average and print it formatted to 2 decimal places.

---

## Key Functions and Modules

### Input Handling
- **`sys.stdin.read()`**  
  Reads the entire input from standard input as a single string.
- **`.splitlines()`**  
  Splits the input string into a list of lines.

### Collections Module
- **`collections.namedtuple()`**  
  Creates lightweight object types that behave like tuples with named fields. This makes it easier to access elements by name (e.g., `student.MARKS`) rather than by an index.

### Unpacking with the `*` Operator
- **`Student(*line.split())`**  
  The `*` operator unpacks the list returned by `line.split()` so that each element is passed as a separate positional argument to `Student`.
- **Why Not `Student(line.split())`?**  
  Passing the list as a single argument would not match the expected number of arguments for the namedtuple, resulting in a `TypeError`.

### Output Formatting
- **String Formatting:**  
  Using `"{:.2f}".format(...)` to print the average marks rounded to 2 decimal places.

---

## What You Can Learn

- **Efficient Input Processing:**  
  Handling multi-line input using `sys.stdin.read()` and `.splitlines()`.

- **Parsing and Conversion:**  
  Converting string input into the required data types, such as integers.

- **Using Namedtuples:**  
  How `namedtuple` can provide a convenient and self-documenting way to work with structured data without needing to reference fields by index.

- **Unpacking in Python:**  
  The significance of the `*` operator in unpacking iterables into function arguments.

- **Output Formatting:**  
  Formatting numbers to a specific number of decimal places using Python string formatting.

---

## Additional Resources

- [Wikipedia: Regular Expression](https://en.wikipedia.org/wiki/Regular_expression) *(for regex topics, if needed)*
- [Python re Module Documentation](https://docs.python.org/3/library/re.html) *(for regex topics)*
- [Python Exceptions Documentation](https://docs.python.org/2/library/exceptions.html#module-exceptions)
- [Python sys Module Documentation](https://docs.python.org/3/library/sys.html)
- [Python Namedtuple Documentation](https://docs.python.org/3/library/collections.html#collections.namedtuple)

---

## Conclusion

This solution demonstrates how to calculate the average marks of students using Python's `namedtuple` and efficient input parsing. It highlights the power of Python’s unpacking operator to simplify the code and make it more readable. By working through this challenge, you'll deepen your understanding of input handling, data conversion, and using named data structures in Python.

**Happy Coding!**
