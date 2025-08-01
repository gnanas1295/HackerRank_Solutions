# Email Address Validator

This repository contains a Python solution for a problem that involves parsing and validating email addresses based on a specific set of rules using regular expressions.

---

## Problem Statement

You are given **N** pairs of names and email addresses in the format `name <username@domain.extension>`. Your task is to validate the email address part against a strict set of criteria and print only the pairs that contain a valid email address.

A valid email must meet these rules:
-   **Username**: Starts with a letter, followed by letters, digits, `.` , `-`, or `_`.
-   **Domain**: Contains only letters.
-   **Extension**: Contains only letters and is 1 to 3 characters long.

### Input Format
- The first line contains an integer **N**.
- The next **N** lines each contain a name and email address pair.

### Output Format
- Print the valid name and email address pairs, in the order they appeared in the input.


#### Sample Input

```
2
DEXTER dexter@hotmail.com
VIRUS <virus!@variable.:p>
```

#### Sample Output

```
DEXTER dexter@hotmail.com
```

## Explanation

The provided solution uses a combination of string manipulation, regular expressions, and the `email.utils` library.

1.  **Read Input:** The code reads the number of entries and then loops that many times. In each loop, it reads a full line containing the name and email.
2.  **Regex Validation:** A function `emailValidation` is called for each entry. This function first splits the input string to isolate the email part (e.g., `<dexter@hotmail.com>`). It then tests this part against a compiled regular expression pattern that enforces the problem's rules.
3.  **Parsing and Formatting:** If the regex validation is successful, the code then uses `email.utils.parseaddr()` to parse the original string into a `(name, address)` tuple and `email.utils.formataddr()` to format it back into the original `name <address>` string.
4.  **Conditional Printing:** The main loop checks if the validation function returned a value. If it did, the formatted string is printed.

---
## Algorithm Used

The core of this solution is **Regular Expressions (Regex)**. It defines a pattern that models the specific rules for a valid email address and uses Python's `re` module to test input strings against this pattern. The `email.utils` library is also used for parsing and formatting.

---
## Key Functions and Modules

### Core Logic
-   **`re.compile(pattern)`**: Compiles a regular expression pattern into a regex object for more efficient use inside a loop.
-   **`pattern.match(string)`**: A method on a compiled regex object that checks for a match at the beginning of a string. Since the pattern is anchored with `^`, it effectively validates the whole string.
-   **`email.utils.parseaddr(address)`**: A utility that parses a string containing a name and email address into a `(realname, email_address)` tuple.
-   **`email.utils.formataddr(pair)`**: Does the reverse of `parseaddr`, creating a formatted string from a `(realname, email_address)` tuple.

---

## What You Can Learn

-   **Constructing Complex Regex:** This is a great example of building a regex pattern to validate a string against multiple, specific rules (e.g., starting character, subsequent characters, domain/extension rules).
-   **Using Python's `re` Module:** Demonstrates the standard workflow of compiling a pattern and using its methods to perform validation.
-   **Leveraging Standard Libraries:** Shows an introduction to the `email.utils` library, which contains helpful tools for common tasks like parsing email address strings.

---

## Additional Resources

-   [Python `re` Module Documentation](https://docs.python.org/3/library/re.html)
-   [Python `email.utils` Documentation](https://docs.python.org/3/library/email.utils.html)

---

## Conclusion

This solution effectively validates email addresses by creating a specific regex pattern. It demonstrates a practical application of regular expressions and introduces useful utilities from Python's standard library for handling common data formats.

**Happy Coding!**
