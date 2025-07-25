# Validating Postal Codes

This repository contains a Python solution for the "Validating Postal Codes" challenge, which involves using two distinct regular expressions to check a string against a set of rules.

---

## Problem Statement

A valid postal code must satisfy two conditions:
1.  It must be a number in the range from 100000 to 999999, inclusive.
2.  It must not contain more than one "alternating repetitive digit pair." An alternating pair is two equal digits separated by exactly one other digit (e.g., in `121`, the `1`s form a pair).

### Input Format
- A single string, **P**, representing the postal code.

### Output Format
- The provided code stub prints `True` if the postal code is valid and `False` otherwise.

#### Sample Input

```
110000
```

#### Sample Output
```
False
```

## Explanation

The code uses two regular expressions to validate the input string `P`.

1.  **Range Check (`^[1-9]\d{5}$`)**: This regex ensures the code is a 6-digit number that doesn't start with 0, which perfectly covers the 100000-999999 range. `re.match()` is used to ensure the entire string conforms to this pattern.

2.  **Alternating Pair Check (`(?=(\d)\d\1)`)**: This regex finds all alternating pairs.
    -   `re.findall()` is used to get a list of all such pairs.
    -   The **positive lookahead** `(?=...)` is critical here. It allows the regex engine to find all pairs, even if they overlap (e.g., in `12121`), which a normal pattern would miss.
    -   `(\d)\d\1` is the pattern for the pair, using a **backreference** `\1` to ensure the first and third digits are the same.

The final validation check `len(re.findall(...)) < 2` ensures the number of these pairs is 0 or 1.

---

## Key Concepts and Modules

-   **`re.match(pattern, string)`**: Used to check the range regex. It anchors the search to the beginning of the string.
-   **`re.findall(pattern, string)`**: Used with the alternating pair regex to get a list of all found occurrences.
-   **Regex Anchors (`^`, `$`)**: Used to ensure the entire string matches the range pattern.
-   **Regex Lookaheads (`(?=...)`)**: A non-consuming assertion used to find all overlapping matches of the alternating pairs.
-   **Regex Backreferences (`\1`)**: Used to refer to a previously captured group, which is essential for finding the repeating digits.

---

## What You Can Learn

-   **Hybrid Validation**: How to solve a problem with multiple, distinct rules by combining the results of separate regex checks.
-   **Advanced Regex**: The practical application of lookaheads for finding overlapping matches and backreferences for finding repeated patterns.
-   **Choosing the Right Tool**: Understanding when to use `re.match()` (for full string validation) vs. `re.findall()` (for counting all occurrences).

---

## Additional Resources

-   [Python `re` — Regular expression operations](https://docs.python.org/3/library/re.html)

---

## Conclusion

This problem is a great exercise in advanced regular expressions. It demonstrates that by choosing the right features—like anchors, lookaheads, and backreferences—you can solve complex validation tasks with concise and powerful patterns.

**Happy Coding!** 📮
