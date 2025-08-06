# Floating Point Number Validator

This repository contains a Python solution for a problem that involves validating strings to determine if they represent a valid floating-point number according to a specific set of rules.

---

## Problem Statement

Your task is to verify if a given string is a valid float number. A valid float must satisfy all of the following criteria:
1.  It can optionally start with a `+`, `-`, or `.` symbol.
2.  It must contain exactly one `.` symbol.
3.  It must have at least one digit after the decimal point.
4.  It must be convertible to a `float` type in Python without errors.

### Input Format
- The first line contains an integer **T**, the number of test cases.
- The next **T** lines each contain a string to be validated.

### Output Format
- For each test case, print `True` if the string is a valid float, and `False` otherwise.

#### Sample Input

```
4
4.0O0
-1.00
+4.5
.5
```

#### Sample Output

```
False
True
True
True
```

## Explanation

The provided solution uses a single, powerful regular expression to validate the input string against all the required rules simultaneously.

1.  **Define Pattern:** A regex pattern, `r'^[+-]?(\d+\.\d+|\.\d+)$'`, is defined. This pattern is designed to match the two possible valid float formats: numbers with digits before the decimal (like `+4.5`) and numbers that start with a decimal (like `.5`).
2.  **Match String:** The `re.match()` function is used to test if the input string matches this pattern from beginning to end. The `^` and `$` anchors in the pattern ensure that the *entire* string must conform to the float format.
3.  **Return Boolean:** The validation function returns `True` if the pattern matches and `False` if it does not. The main script then prints this boolean result for each input string.

---
## Algorithm Used

The core of the solution is **Regular Expressions (Regex)**. It uses a single, complex pattern with anchors, optional groups, character classes, and alternations (`|`) to validate the input string in one pass.

### Time and Space Complexity

* **Time Complexity: `O(L)`** for each string, where `L` is the length of the string. The regex engine makes a single pass over the string to check for a match.
* **Space Complexity: `O(1)`**. The memory used for the validation process is constant and does not scale with the length of the input string.

---
## Key Functions and Modules

### Core Logic
-   **`re.match(pattern, string)`**: A function from Python's `re` module that attempts to match a pattern at the beginning of a string. Since the pattern is anchored with `^` and `$`, it effectively validates the entire string.
-   **Regex Pattern `r'^[+-]?(\d+\.\d+|\.\d+)$'`**:
    -   `^`: Asserts the start of the string.
    -   `[+-]?`: Matches an optional `+` or `-` sign.
    -   `(...)`: A group containing the two possible formats.
    -   `\d+\.\d+`: Matches the first format (e.g., `4.50`).
    -   `|`: An "OR" operator.
    -   `\.\d+`: Matches the second format (e.g., `.5`).
    -   `$`: Asserts the end of the string.

---

## What You Can Learn

-   **Building Complex Regex:** This problem is a great example of how to combine smaller regex components (like character sets, quantifiers, anchors, and alternations) to build a single pattern that enforces a complex set of rules.
-   **String Validation:** Demonstrates a powerful and efficient method for validating string formats, which is a very common task in software development.
-   **Problem Solving with Regex vs. `try-except`:** Shows that a problem can often be solved in multiple ways. While regex is excellent for strict format validation, a `try-except` block is a valid alternative for checking if a value can be cast to a certain type.

---

## Additional Resources

-   [Python `re` Module Documentation](https://docs.python.org/3/library/re.html)
-   [Regular-Expressions.info](https://www.regular-expressions.info/)

---

## Conclusion

This solution effectively uses a single, well-crafted regular expression to enforce multiple validation rules. It's a prime example of how regex can be used to write concise and powerful code for string format validation.

**Happy Coding!**
