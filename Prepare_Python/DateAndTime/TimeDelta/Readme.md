# Social Media Timestamp Difference

This solution computes the absolute difference (in seconds) between two timestamps. Each timestamp represents the time a social media post was published, and they include time zone information. The goal is to normalize these times and compute the time difference in seconds.

---

## Problem Statement

When users post updates on social media (such as a URL, image, or status update), other users see the post on their news feed along with a timestamp (showing how long ago it was published). Since posts can be published and viewed in different time zones, the displayed timestamps may need to be compared accurately. Given two timestamps in the format:
Day dd Mon yyyy hh:mm:ss +xxxx where `+xxxx` represents the time zone offset, your task is to print the absolute difference (in seconds) between them.


### Input Format

- The first line contains an integer `t`, the number of test cases.
- Each test case consists of 2 lines:
  - The first line is the first timestamp.
  - The second line is the second timestamp.

### Output Format

For each test case, print the absolute difference (in seconds) between the two timestamps.

#### Sample Input
```
2 
Sun 10 May 2015 13:54:36 -0700 
Sun 10 May 2015 13:54:36 -0000 
Sat 02 May 2015 19:54:36 +0530 
Fri 01 May 2015 13:54:36 -0000
```
#### Sample Output
```
25200 
88200
```
---

## Key Functions and Modules

### Input Handling
- **`sys.stdin.read()`**  
  Reads the entire input from standard input as a single string.
- **`.splitlines()`**  
  Splits the input string into a list of lines.

### The `datetime` Module
- **`datetime.datetime.strptime(date_string, format)`**  
  Parses a date-time string into a `datetime` object according to the specified format.  
  In this solution, the format is:  
    '%a %d %b %Y %H:%M:%S %z'
- **`%a`**: Abbreviated weekday name (e.g., Sun, Mon).
- **`%d`**: Day of the month as a zero-padded decimal.
- **`%b`**: Abbreviated month name (e.g., Jan, Feb).
- **`%Y`**: Four-digit year.
- **`%H:%M:%S`**: Time in 24-hour format.
- **`%z`**: UTC offset in the form +HHMM or -HHMM.

### Subtracting `datetime` Objects and Using `total_seconds()`
- Subtracting two `datetime` objects results in a `timedelta` object.
- Calling `.total_seconds()` on a `timedelta` returns the difference in seconds.

### The `abs()` Function
- **`abs(x)`**  
Returns the absolute value of `x`.  
In this solution, it is used to ensure the difference in seconds is always non-negative, regardless of which timestamp is earlier.  
[Learn more about `abs()`](https://docs.python.org/3/library/functions.html#abs)

### The `range()` Function
- **`range(start, stop, step)`**  
Generates a sequence of numbers.  
In our loop:
```python
for i in range(1, 2 * n, 2):
    start = 1: We start from index 1 since the first line (index 0) contains the number of test cases.
    stop = 2 * n: There are 2 timestamps per test case.
    step = 2: We increment by 2 so that i points to the first timestamp of each pair.
```

## What You Can Learn

- **Efficient Input Processing:**  
  Using `sys.stdin.read()` combined with `.splitlines()` to handle multi-line input.

- **Parsing Date-Time Strings:**  
  How to convert a formatted date-time string into a `datetime` object using `strptime()`, including parsing the timezone offset.

- **Time Difference Calculation:**  
  How subtracting two `datetime` objects yields a `timedelta` and how to convert this into seconds with `.total_seconds()`.

- **Using the `abs()` Function:**  
  Ensuring that the time difference is non-negative, no matter the order of the timestamps.

- **Iterating in Steps with `range()`:**  
  Looping through a list by steps (here, processing pairs of lines for test cases).

---

## Additional Resources

- [Documentation for `abs()`](https://docs.python.org/3/library/functions.html#abs)
- [Python `datetime` Module Documentation](https://docs.python.org/3/library/datetime.html)
- [Python `sys` Module Documentation](https://docs.python.org/3/library/sys.html)

---

## Conclusion

This solution demonstrates how to accurately compute the absolute difference between two timestamps with different time zones by leveraging Python's built-in modules and functions. It covers robust input handling, date-time parsing, and mathematical operations to achieve a concise and efficient solution.

**Happy Coding!**

