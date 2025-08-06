# Vowel Substring Finder

This repository contains a Python solution for a challenge that involves finding specific substrings of vowels that are located between consonants in a larger string.

---

## Problem Statement

You are given a string that consists of alphanumeric characters and symbols. Your task is to find all substrings that meet the following criteria:
1.  The substring must contain two or more vowels (`aeiouAEIOU`).
2.  The substring must consist *only* of vowels.
3.  The substring must be immediately preceded by a consonant.
4.  The substring must be immediately followed by a consonant.

Consonants are defined as `QWRTYPSDFGHJKLZXCVBNM` and `qwrtypsdfghjklzxcvbnm`.

### Input Format
- A single line containing the input string.

### Output Format
- Print each matched substring on a new line, in the order of its occurrence.
- If no matches are found, print `-1`.

#### Sample Input

```
rabcdeefgyYhFjkIoomnpOeorteeeeet
```

#### Sample Output

```
ee
Ioo
Oeo
eeeee
```

## Explanation

The provided solution uses a single regular expression with lookarounds to find the required vowel substrings.

1.  **Pattern Definition:** It defines the pattern `r"(?<=\w)([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])"`.
2.  **Lookbehind `(?<=\w)`:** It attempts to ensure the substring is preceded by a "word character" (any letter, digit, or underscore).
3.  **Main Match `([aeiouAEIOU]{2,})`:** It correctly identifies and captures sequences of two or more vowels.
4.  **Lookahead `(?=[^aeiouAEIOU])`:** It attempts to ensure the substring is followed by a "non-vowel" character.
5.  **Execution:** The `re.findall()` function is used to find all matching substrings. The main script then checks if the resulting list is empty. If it is, it prints `-1`; otherwise, it prints each found item on a new line.

---
## Algorithm Used

The solution's core is a **Regular Expression** that uses **Lookarounds** to perform a contextual search. It's designed to find patterns that are preceded and followed by other specific patterns, without including the context in the final result.

### Time and Space Complexity

* **Time Complexity: `O(L)`**, where `L` is the length of the input string. The regex engine makes a single pass through the string.
* **Space Complexity: `O(M)`**, where `M` is the total number of characters in all the matched substrings. This space is required to store the list of results.

---
## Key Functions and Modules

### Core Logic
-   **`re.findall(pattern, string)`**: The function from Python's `re` module used to find all non-overlapping matches of a pattern in a string.
-   **Positive Lookbehind `(?<=\w)`**: An advanced regex feature that checks the characters *before* the main pattern.
-   **Positive Lookahead `(?=...)`**: An advanced regex feature that checks the characters *after* the main pattern.

---

## What You Can Learn

-   **Advanced Regex with Lookarounds:** This solution is a great example of using lookarounds to solve complex pattern-matching problems where the context of a match is important.
-   **The Importance of Precision:** It also highlights a critical lesson in regex: the character sets you use must be precise. The solution is flawed because `\w` (word character) and `[^aeiouAEIOU]` (not a vowel) are not the same as the problem's strict definition of a **consonant**. A correct solution requires a character set that contains only the specified consonant characters.

---

## Additional Resources

-   [Python `re` Module Documentation](https://docs.python.org/3/library/re.html)
-   [Regular-Expressions.info - Lookarounds](https://www.regular-expressions.info/lookaround.html)

---

## Conclusion

This solution demonstrates a strong attempt at solving a complex regex problem with advanced features. While the specific character sets in the lookarounds are not perfectly aligned with the problem's constraints, the overall structure and approach are sound.

**Happy Coding!**
