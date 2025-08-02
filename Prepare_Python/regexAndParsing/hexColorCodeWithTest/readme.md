# CSS Hex Color Code Extractor

This repository contains a Python solution for a problem that involves parsing CSS code to find and extract all valid hexadecimal color codes used as property values.

---

## Problem Statement

You are given **N** lines of CSS code. Your task is to find all valid hex color codes, but only those used as values for CSS properties (i.e., not as selectors).

A valid hex code:
-   Starts with `#`.
-   Has exactly 3 or 6 subsequent characters.
-   Hex characters are `0-9` and `a-f` (case-insensitive).

### Input Format
- The first line contains an integer **N**, the number of lines.
- The next **N** lines contain the CSS code.

### Output Format
- Print each valid hex color code found, in order of appearance, on a new line.

#### Sample Input

```
11
#BED
{
color: #FfFdF8; background-color:#aef;
font-size: 123px;
background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
background-color: #ABC;
border: 2px dashed #fff;
}
```

#### Sample Output

```
#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
```

## Explanation

The provided solution processes the input line by line.

1.  **Iterate Through Lines:** The code reads the number of lines and then loops, processing one line of CSS at a time.
2.  **Apply Regex:** In each iteration, it applies a sophisticated regular expression to the current line.
3.  **Pattern Logic:** The pattern, `r"(?<=[ :\(,])#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})"`, is designed to find valid hex codes that are used as values. It achieves this using a **positive lookbehind** `(?<=...)` which asserts that the hex code must be preceded by a character like a space or a colon, effectively filtering out codes used as selectors.
4.  **Find and Print:** The `re.findall()` function finds all matching hex codes on the line, which are then immediately printed.

---
## Algorithm Used

The core of the solution is **Regular Expressions (Regex)**. It uses an advanced feature called a **positive lookbehind** to perform contextual pattern matching, which allows it to distinguish between hex codes used as selectors and those used as property values.

### Time and Space Complexity

* **Your Solution & Optimized Solution:**
    * **Time Complexity: `O(L)`** where `L` is the total number of characters in the input. The regex engine must scan through the entire text block once.
    * **Space Complexity: `O(M)`** where `M` is the total number of matches found. The space is required to store the list of results.

---
## Key Functions and Modules

### Core Logic
-   **`re.compile()`**: Creates a reusable regex object from a pattern string.
-   **`re.findall()`**: Finds all non-overlapping matches of the pattern in a string and returns them as a list.
-   **Positive Lookbehind `(?<=...)`**: An advanced regex feature that matches a group before the main expression without including it in the result. This is the key to filtering out selectors.
-   **Non-Capturing Group `(?:...)`**: Groups expressions together (for the `|` operator) without creating a capture group.

---

## What You Can Learn

-   **Advanced Regex with Lookarounds:** This solution is an excellent demonstration of how lookarounds (specifically, positive lookbehind) can be used to match patterns based on their context, leading to more powerful and precise validation.
-   **Input Handling for Structured Text:** The solution highlights a common challenge: processing structured text (like code) that spans multiple lines. While the submitted solution processes line by line, a more robust approach is to read the entire block of text into a single string first to correctly handle rules that cross line breaks.

---

## Additional Resources

-   [Python `re` Module Documentation](https://docs.python.org/3/library/re.html)
-   [Regular-Expressions.info - Lookarounds](https://www.regular-expressions.info/lookaround.html)

---

## Conclusion

This solution effectively uses an advanced regular expression with a positive lookbehind to solve a complex parsing task. It's a great example of the power and precision that regex can offer for text processing challenges.

**Happy Coding!**
