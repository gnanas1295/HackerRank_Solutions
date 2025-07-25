# Validating UID Challenge

This repository documents multiple Python solutions for the "Validating UID" problem. It explores different approaches, from a simple loop to more advanced regular expressions, to check a string against a complex set of validation rules.

## Problem Statement

A company is creating unique identification numbers (UIDs) for its employees. A valid UID must follow five specific rules:
1.  It must contain at least 2 uppercase English alphabet characters (A-Z).
2.  It must contain at least 3 digits (0-9).
3.  It must only contain alphanumeric characters (a-z, A-Z, 0-9).
4.  No character should repeat.
5.  There must be exactly 10 characters in a valid UID.

Your task is to validate a list of UIDs and print 'Valid' or 'Invalid' for each.

### Input Format
-   The first line contains an integer, **T**, the number of test cases.
-   The next **T** lines each contain a UID string.

### Output Format
-   For each UID, print 'Valid' or 'Invalid' on a new line.

#### Sample Input
2
B1CD102354
B1CDEF2354


#### Sample Output
Invalid
Valid


## Explanation

-   **B1CD102354**: Fails rule 4 because the character '1' is repeated. → **Invalid**
-   **B1CDEF2354**: Passes all five rules. → **Valid**

---

## Approaches and Solutions

There are several ways to solve this problem, each with trade-offs between performance and readability.

### ### Approach 1: The Single-Pass Loop (Most Performant)
This method is the most efficient for very large inputs, as it iterates through the string only once to gather all required counts.

```python
def validate_uid_loop(uid):
    if len(set(uid)) != 10 or not uid.isalnum():
        return 'Invalid'

    upper_count = 0
    digit_count = 0
    for char in uid:
        if char.isupper():
            upper_count += 1
        elif char.isdigit():
            digit_count += 1
            
    if upper_count >= 2 and digit_count >= 3:
        return 'Valid'
    else:
        return 'Invalid'
```

### Approach 2: The Pythonic sum() Method (Most Readable)
This approach is very clear and declarative. Each rule is a self-contained expression. While it makes multiple passes over the string, this is irrelevant for a short string of length 10 and is often preferred for its readability.

### Approach 3: The Hybrid Regex Method (Advanced)
This approach uses a single regular expression to check most of the rules. Regex is powerful for pattern matching but cannot validate character uniqueness, so we still need the set() check.

## Explanation

-   **B1CD102354**: Fails rule 4 because the character '1' is repeated. → **Invalid**
-   **B1CDEF2354**: Passes all five rules:
    1.  Has 6 uppercase letters (C, D, E, F) ≥ 2.
    2.  Has 4 digits (1, 2, 3, 5, 4) ≥ 3.
    3.  All characters are alphanumeric.
    4.  All characters are unique.
    5.  Length is exactly 10. → **Valid**

---

## Key Functions and Concepts

### Validation Logic
The solution checks each of the five rules and uses the built-in `all()` function to ensure every rule returns `True`.

-   **Uniqueness & Length (`len(set(uid)) == 10`)**: This single, efficient check validates two rules at once. A `set` only stores unique items, so if the length of the set is 10, the original 10-character string must have had no duplicates.
-   **Alphanumeric Check (`uid.isalnum()`)**: A built-in string method that returns `True` if all characters are letters or numbers.
-   **Conditional Counting (`sum(1 for c in uid if c.isupper())`)**: A concise, Pythonic way to count items in an iterable that meet a condition. We use it to count both uppercase letters and digits without writing a manual loop.

---

## What You Can Learn

-   **Complex Validation**: How to break down a complex set of requirements into simple, verifiable boolean checks.
-   **Pythonic Idioms**: Using tools like `set()` for uniqueness and `sum()` with generator expressions for counting leads to cleaner and more readable code.
-   **Boolean Logic**: Leveraging functions like `all()` to aggregate multiple checks into a single, clear conditional statement.

---

## Additional Resources

-   [Python `set()` Data Structure](https://docs.python.org/3/tutorial/datastructures.html#sets)
-   [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
-   [Python `sum()` and `all()` built-in functions](https://docs.python.org/3/library/functions.html)

---

## Conclusion

This solution demonstrates an effective strategy for handling multi-rule validation problems. By translating each rule into a simple expression and then combining the results, the code remains readable, robust, and efficient.

**Happy Coding!** ✅