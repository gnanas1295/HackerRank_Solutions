# Roman Numeral Validator

This repository contains a Python solution for a challenge that involves validating whether a given string is a valid Roman numeral using regular expressions.

---

## Problem Statement

You are given a string of characters. Your task is to determine if the string represents a valid Roman numeral for a number between 1 and 3999.

### Input Format
- A single line containing a string of uppercase Roman characters.

### Output Format
- Print `True` if the string is a valid Roman numeral, `False` otherwise.

#### Sample Input

```
CDXXI
```

#### Sample Output

```
True
```

## Explanation

The provided solution uses a single, clever regular expression to perform the validation. The logic is split into two main checks within the pattern.

1.  **Character Check:** The main part of the pattern, `[IVXLCDM]+$`, ensures that the string consists of one or more valid Roman numeral characters and nothing else.
2.  **Repetition Check:** The solution uses an advanced feature called a **negative lookahead**, `(?!.*(IIII|...))`, at the beginning. This scans the entire string and causes the match to fail if it finds any common invalid repetition sequences, such as `IIII`, `VV`, or `XXXX`.
3.  **Final Validation:** The `re.match` function, combined with the `^` and `$` anchors, checks if the entire input string adheres to these two rules.

---
## Algorithm Used

The algorithm is a **Regular Expression** based validator. It uses a **negative lookahead** to define and enforce the "invalid repetition" rules, which is a powerful technique for defining patterns that should not exist in the string.

### Time and Space Complexity

* **Your Solution & The Optimized Solution:**
    * **Time Complexity: `O(L)`**, where `L` is the length of the input string. The regex engine makes a single pass over the string to check for a match.
    * **Space Complexity: `O(1)`**. The memory used is constant and does not scale with the input size.

---
## Key Functions and Modules

### Core Logic
-   **`re.match(pattern, string)`**: Used to check if the pattern matches at the beginning of the string. The `^` anchor ensures it behaves like a full-string match.
-   **Negative Lookahead `(?!...)`**: The key feature of the pattern. It asserts that a subpattern (the invalid repetitions) does not exist anywhere in the string.
-   **Anchors `^` and `$`**: Used to ensure the pattern matches the entire string from start to finish.

---

## What You Can Learn

-   **Using Negative Lookaheads:** This solution is a great example of using a negative lookahead to enforce "must not contain" rules in a regex, which is very useful for validation tasks.
-   **Limitations of Simple Regex:** It also highlights the limitations of a simplified approach. While the pattern correctly identifies invalid repetitions, it is not sufficient to validate the complex structural and ordering rules of Roman numerals (e.g., it would incorrectly validate `IXC`). A fully correct regex for Roman numerals must validate the sequence of thousands, hundreds, tens, and ones.

---

## Additional Resources

-   [Python `re` Module Documentation](https://docs.python.org/3/library/re.html)
-   [Regular-Expressions.info - Lookarounds](https://www.regular-expressions.info/lookaround.html)

---

## Conclusion

This solution provides a clever and concise way to check for some of the most common Roman numeral errors using an advanced regex feature. While not a complete validator, it's an excellent demonstration of the power of negative lookaheads.

**Happy Coding!**
