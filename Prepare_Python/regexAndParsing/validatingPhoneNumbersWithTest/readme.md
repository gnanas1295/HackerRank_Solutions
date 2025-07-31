# Regex Mobile Number Validator

This repository contains a Python solution for a problem that involves validating mobile numbers using regular expressions.

---

## Problem Statement

You are given a list of strings. For each string, you must determine if it is a valid mobile number. A valid mobile number is defined as a ten-digit number that starts with a 7, 8, or 9.

### Input Format
- The first line contains an integer **N**, the number of strings to check.
- The next **N** lines each contain a single string.

### Output Format
- For each string, print "YES" if it is a valid mobile number, and "NO" otherwise, each on a new line.

#### Sample Input

```
2
9587456281
1252478965
```

#### Sample Output

```
YES
NO
```

## Explanation

The provided solution reads a count of inputs and then iterates that many times.

1.  **Read Input:** Inside a loop, it reads a single line, which represents a potential phone number.
2.  **Length Check:** It first performs a manual check to see if the string's length is greater than 10, printing "NO" if it is.
3.  **Define Pattern:** It defines a regular expression pattern `r"[789][\d]{9}"`. This pattern looks for a string that starts with a 7, 8, or 9, followed by exactly nine digits.
4.  **Match and Print:** It uses the `re.match()` function to test if the *beginning* of the input string matches this pattern. If `re.match()` finds a match, it prints "YES"; otherwise, it prints "NO".

---
## Algorithm Used

The core of this solution is **Regular Expressions (Regex)**. It defines a specific pattern to match the required format of a valid mobile number and uses Python's `re` module to test input strings against this pattern.

---
## Key Functions and Modules

### Core Logic
- **`re.match(pattern, string)`**: This function from Python's `re` module is used to check for a pattern match. It is important to note that `re.match()` only checks for a match at the **beginning** of the string, not the entire string.
- **Regex Pattern `r"[789][\d]{9}"`**: This is the pattern used for validation.
    -   `[789]`: This character set matches a single character that must be a `7`, `8`, or `9`.
    -   `[\d]`: This is a shorthand for any digit (0-9). The problem statement specifies the input as a string which contains only alphanumeric characters. This is a good way to match any digit `d`.
    -   `{9}`: This is a quantifier that specifies the preceding element (`\d`) must occur exactly nine times.

---

## What You Can Learn

-   **Basic Regex Syntax:** This problem is a great introduction to writing simple regular expressions, including character sets (`[]`) and quantifiers (`{}`).
-   **Using Python's `re` Module:** Demonstrates the fundamental use of the `re` library to apply a regex pattern to a string.
-   **The Importance of Full vs. Partial Matching:** This solution highlights the critical difference between `re.match()` (which checks from the start of the string) and `re.fullmatch()` (which validates the entire string). For strict validation tasks like this, using `re.fullmatch()` or anchoring the pattern (e.g., `^...$`) is essential to avoid incorrect positive matches.

---

## Additional Resources

-   [Python `re` Module Documentation](https://docs.python.org/3/library/re.html)
-   [Google's Python Regex Tutorial](https://developers.google.com/edu/python/regular-expressions)

---

## Conclusion

This solution effectively uses a regular expression to define the pattern for a valid mobile number. It serves as a good example of pattern matching in Python and an important lesson on the nuances of different matching functions within the `re` module.

**Happy Coding!**
