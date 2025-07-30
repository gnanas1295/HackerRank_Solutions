# Custom Alphanumeric String Sorter

This repository contains a Python solution for a problem that requires sorting a string's characters based on a complex set of rules.

---

## Problem Statement

You are given an alphanumeric string. Your task is to sort it according to the following rules, in order:
1.  All sorted lowercase letters.
2.  All sorted uppercase letters.
3.  All sorted odd digits.
4.  All sorted even digits.

### Input Format
- A single line containing the alphanumeric string.

### Output Format
- The custom-sorted string.

#### Sample Input

```
Sorting1234
```

#### Sample Output

```
ginortS1324
```

## Explanation

The provided solution solves this problem by categorizing each character of the input string into one of four distinct groups.

1.  **Initialization:** Four empty lists are created: `lowerCase`, `upperCase`, `oddDigits`, and `evenDigits`.
2.  **Categorization:** The code iterates through the input string one character at a time. Using `if/elif/else` logic with string methods like `.islower()`, `.isupper()`, and a check for even/odd numbers, it appends each character to its corresponding list.
3.  **Sorting:** After all characters are categorized, each of the four lists is sorted individually using the built-in `sorted()` function.
4.  **Concatenation:** Finally, the sorted lists are joined together in the specified order (lowercase, then uppercase, then odd digits, then even digits) to produce the final output string.

---
## Algorithm Used

This solution uses a **Categorize and Conquer** approach. It's a type of brute-force method where the problem is broken down by separating the input data into distinct buckets. Each bucket is then solved (sorted) independently, and the results are combined.

---
## Key Functions and Modules

### Core Logic
- **`str.islower()`, `str.isupper()`, `str.isdigit()`**: String methods used to determine the type of each character.
- **`sorted()`**: The primary built-in function for sorting, used here on each of the four categorized lists.
- **`str.join()`**: A string method used to concatenate the elements of an iterable (the sorted lists) into a single final string.
- **`%` (Modulo Operator)**: Used to distinguish between odd and even digits.

---

## What You Can Learn

-   **Categorization Strategy:** This is a clear example of how to solve a complex sorting problem by first breaking the data down into simpler, homogeneous groups.
-   **String and List Manipulation:** The solution demonstrates fundamental Python skills for iterating through strings, building lists, and combining them back into a string.
-   **Applying Multiple Sorts:** Shows a straightforward pattern for problems where different subsets of data need to be sorted independently before being recombined.

---

## Additional Resources

-   [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
-   [Python `sorted()` Function](https://docs.python.org/3/library/functions.html#sorted)

---

## Conclusion

This solution provides a very clear and readable implementation of the custom sorting rules. By physically separating the characters into different lists, it makes the logic easy to follow and debug, offering a solid approach to multi-level sorting problems.

**Happy Coding!**
