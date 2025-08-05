# Matrix Script Decoder

This repository contains a Python solution for the "Matrix Script" decoding challenge, which involves transposing a character matrix and cleaning the resulting string with regular expressions.

---

## Problem Statement

You are given an `N x M` matrix of characters. To decode it, you must read the characters column by column, from left to right and top to bottom, to form a single string. After decoding, you must replace any sequence of non-alphanumeric characters that appears between two alphanumeric characters with a single space.

### Input Format
- The first line contains integers **N** (rows) and **M** (columns).
- The next **N** lines contain the matrix rows.

### Output Format
- Print the final, cleaned-up decoded script.

#### Sample Input

```
7 3
Tsi
h%x
i #
sM
$a
#t
%ir
```

#### Sample Output

```
This is Matrix#  %!
```

## Explanation

The provided solution follows a two-stage process to decode the script.

1.  **Matrix Transpose:** The code first reads the matrix dimensions and rows. It then uses a nested `for` loop to iterate through each column (`itr`) and then each row (`i`), appending the character `matrix[i][itr]` to a single string, `finalStr`. This effectively reads the matrix column by column.
2.  **Regex Substitution:** After the `finalStr` is created, it applies a regular expression to clean it up. The pattern `r"(?<=[0-9A-Za-z])[^a-zA-Z0-9]{1,}(?=[0-9A-Za-z])"` uses positive lookarounds (`(?<=...)` and `(?=...)`) to find sequences of one or more non-alphanumeric characters that are "sandwiched" between two alphanumeric characters. The `re.sub()` function replaces these matched sequences with a single space.

---
## Algorithm Used

The solution uses a combination of a **manual matrix transpose** algorithm and **Regular Expressions (Regex)** for string substitution. The regex employs an advanced feature known as **lookarounds** to perform contextual replacement based on the characters surrounding a match.

### Time and Space Complexity

* **Time Complexity: `O(N*M)`**. The dominant operations are building the string and running the regex substitution, both of which are proportional to the total number of characters in the matrix (`N * M`).
* **Space Complexity: `O(N*M)`**. The solution requires space to store the entire decoded string in memory.

---
## Key Functions and Modules

### Core Logic
-   **Nested `for` loops**: The primary mechanism used to iterate through the matrix columns and rows to perform the transpose.
-   **`re.sub(pattern, repl, string)`**: The function from Python's `re` module used to perform the search-and-replace operation.
-   **Regex Lookarounds `(?<=...)` and `(?=...)`**: These are the key to the regex pattern. They allow the engine to check for surrounding characters without including them in the part of the string that gets replaced.

---

## What You Can Learn

-   **Matrix Transposition:** The solution demonstrates a direct, procedural approach to transposing a 2D data structure. A more "Pythonic" alternative to learn is the `zip(*matrix)` idiom.
-   **Advanced Regex:** This is a perfect example of how lookarounds can solve complex substitution problems where context is important.
-   **Debugging "Invisible" Errors:** A common challenge in this problem is handling trailing whitespace created from the matrix padding. The final solution requires a cleanup step like `.rstrip()` to pass all test cases, which is a great lesson in debugging outputs that "look" correct but are not.

---

## Additional Resources

-   [Python `re.sub()` Documentation](https://docs.python.org/3/library/re.html#re.sub)
-   [Regular-Expressions.info - Lookarounds](https://www.regular-expressions.info/lookaround.html)

---

## Conclusion

This solution effectively decodes the matrix script by combining a manual transpose with a powerful and precise regular expression. It's a great showcase for using advanced regex features like lookarounds to solve complex string manipulation tasks.

**Happy Coding!**
