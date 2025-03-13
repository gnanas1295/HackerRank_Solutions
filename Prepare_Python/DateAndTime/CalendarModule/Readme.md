# Determine the Day of the Week

This solution uses Python's built-in `calendar` module to determine the day of the week for a given date. The program reads the date in `MM DD YYYY` format, computes the day of the week, and outputs the result in uppercase letters.

---
## Problem Statement

Given a date as input, your task is to determine the day of the week on that date and print it in capital letters.

**Example:**

- **Input:**  
  `08 05 2015`
- **Output:**  
  `WEDNESDAY`

---

## Code Overview

```python
import sys
import calendar

# Read input from standard input and convert each token to an integer.
month, day, year = map(int, sys.stdin.read().split())

# Determine the day of the week.
# calendar.weekday(year, month, day) returns an integer (0 = Monday, 6 = Sunday).
day_number = calendar.weekday(year, month, day)

# Retrieve the day name from calendar.day_name and convert it to uppercase.
print(calendar.day_name[day_number].upper())
```


## Key Functions and Modules

### Input Handling
- **`sys.stdin.read()`**  
  Reads the entire input from standard input as a single string.
- **`.split()`**  
  Splits the input string into a list of substrings based on whitespace.
- **`map(int, ...)`**  
  Converts each substring into an integer. This is used to get numeric values for the month, day, and year.

### Calendar Module
- **`calendar.weekday(year, month, day)`**  
  Returns an integer corresponding to the day of the week (0 for Monday through 6 for Sunday).  
  [Learn more](https://docs.python.org/3/library/calendar.html#calendar.weekday)
- **`calendar.day_name`**  
  A list containing the names of the days of the week. For example, `calendar.day_name[0]` is "Monday".  
  [Calendar Module (Python 2)](https://docs.python.org/2/library/calendar.html#module-calendar)

### String Methods
- **`.upper()`**  
  A built-in string method that converts all characters in a string to uppercase.  
  For additional string functionality, see the [Module String Documentation](https://docs.python.org/2/library/string.html?highlight=str#module-string).

---

## How It Works

- **Input Processing:**  
  The program reads the input date (e.g., `"08 05 2015"`) from standard input, splits it into separate values, and converts them to integers.
- **Determine the Day Number:**  
  The `calendar.weekday()` function calculates the day of the week by returning a number between 0 (Monday) and 6 (Sunday).
- **Retrieve and Format Day Name:**  
  The program uses the computed day number to index into `calendar.day_name`, retrieves the corresponding day name, converts it to uppercase, and prints it.

---

## Additional Resources

- [Calendar Module (Python 2)](https://docs.python.org/2/library/calendar.html#module-calendar)
- [Calendar Module (Python 3) - `calendar.weekday()`](https://docs.python.org/3/library/calendar.html#calendar.weekday)
- [Module String Documentation](https://docs.python.org/2/library/string.html?highlight=str#module-string)