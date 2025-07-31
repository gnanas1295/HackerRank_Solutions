# Validating Credit Card Numbers

This repository contains a robust Python solution for the "Validating Credit Card Numbers" challenge, which requires checking a string against multiple complex formatting and content rules using regular expressions.

---

## Problem Statement

A valid credit card number from ABCD Bank must adhere to the following rules:
1.  It must start with a `4`, `5`, or `6`.
2.  It must contain exactly 16 digits.
3.  It must only consist of digits (0-9).
4.  It may have digits in groups of 4, separated by one hyphen `-` (e.g., `4123-4567-8912-3456`).
5.  It must not use any other separators (e.g., space, underscore).
6.  It must not have 4 or more consecutive repeated digits (e.g., `1111`).

### Input Format
-   The first line contains an integer **N**, the number of credit card numbers to validate.
-   The next **N** lines each contain a credit card number string.

### Output Format
-   For each credit card number, print `Valid` or `Invalid` on a new line.

#### Sample Input

```
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
```

#### Sample Output
```
Valid
Valid
Invalid
Valid
Invalid
Invalid
```

## Explanation

The solution uses a two-step hybrid approach, as a single regular expression for all rules would be impractical.

1.  **Format Validation**: A primary regex checks the overall structure. It ensures the string starts with a `4`, `5`, or `6` and has either 16 consecutive digits or four groups of four digits separated by hyphens.
2.  **Consecutive Digit Check**: If the format is valid, all hyphens are removed from the string. A second, simpler regex is then used to search for any digit that is repeated four or more times in a row. If this "bad" pattern is found, the number is invalid.

A card number is only `Valid` if it passes the format check AND fails the consecutive digit check.

---

## Key Functions and Modules

-   **`re.match(pattern, string)`**: Used to check the main format pattern. It is anchored to the beginning of the string, which is perfect for this kind of validation.
-   **`re.search(pattern, string)`**: Used to find the "bad" pattern of repeated digits anywhere in the cleaned string.
-   **`str.replace('-', '')`**: Used to remove hyphens before checking for consecutive digits.
-   **Regex Backreferences `(\d)\1{3}`**: The core of the second check. `(\d)` captures a digit, and `\1{3}` is a backreference that checks if the same captured digit appears three more times.

---

## What You Can Learn

-   **Hybrid Validation**: How to solve complex validation problems by breaking them into parts, using regex for format checking and other logic for content checking.
-   **Advanced Regex Patterns**: Building patterns with anchors (`^`, `$`), character sets (`[456]`), non-capturing groups (`(?:...)`), alternation (`|`), and quantifiers.
-   **Separating Logic from I/O**: Writing functions that perform a single task (like validation) and return a result, which makes code cleaner, more reusable, and easier to test.

---

## Additional Resources

-   [Python `re` — Regular expression operations](https://docs.python.org/3/library/re.html)
-   [Regular Expression Backreferences](https://www.regular-expressions.info/backref.html)

---

## Conclusion

This problem is a great example of the power and limitations of regular expressions. While regex is unbeatable for validating structure and format, combining it with simple string manipulation in Python provides a robust and readable solution for more complex, multi-layered rules.

**Happy Coding!** 💳