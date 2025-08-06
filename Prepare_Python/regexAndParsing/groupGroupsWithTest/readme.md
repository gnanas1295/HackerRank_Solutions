# Find First Repeated Alphanumeric Character

This repository contains a Python solution for a challenge that involves finding the first instance of a consecutively repeated alphanumeric character in a string using regular expressions.

---

## Problem Statement

You are given a string which may contain any characters. Your task is to find the first alphanumeric character (A-Z, a-z, 0-9) that is immediately followed by itself. If such a character exists, print it. Otherwise, print -1.

### Input Format
- A single line containing the input string.

### Output Format
- Print the first consecutively repeated alphanumeric character, or -1 if none exists.

#### Sample Input

```
..12345678910111213141516171820212223
```

#### Sample Output

```
1
```

## Explanation

The provided solution uses a regular expression with a backreference to find the required character.

1.  **Define Pattern:** It uses the pattern `r"([a-zA-Z0-9])\1"`. This pattern is composed of two parts:
    * `([a-zA-Z0-9])`: A **capturing group** that matches and "remembers" any single alphanumeric character. This is Group 1.
    * `\1`: A **backreference** that matches the exact same text that was just captured by Group 1.
2.  **Find All Matches:** It then uses `re.findall()` to find *all* non-overlapping occurrences of this pattern in the entire input string. `re.findall` with a capturing group returns a list of the captured strings (e.g., `['1', '2']` for an input containing `11` and `22`).
3.  **Return Result:** The code checks if the `matching` list is empty. If it has items, it returns the first one (`matching[0]`). If the list is empty (no matches found), it returns `-1`.

---
## Algorithm Used

The core of the solution is a **Regular Expression** that uses a **backreference** to find a specific pattern of consecutive identical characters.

### Time and Space Complexity

* **Your Solution (`re.findall`):**
    * **Time Complexity: `O(L)`**, where `L` is the length of the string. The regex engine must scan the entire string to find all possible matches.
    * **Space Complexity: `O(M)`**, where `M` is the number of repeated characters found. This is because `re.findall` builds a list in memory containing all the matches.

* **Optimized Solution (`re.search`):**
    * **Time Complexity: `O(L)`** in the worst case (if no match exists). However, it is much faster on average because it **stops scanning** as soon as the first match is found.
    * **Space Complexity: `O(1)`**. It only stores a single match object, not a list of all matches, making it more memory-efficient.

---
## Key Functions and Modules

### Core Logic
-   **`re.findall(pattern, string)`**: This function from Python's `re` module finds all occurrences of a pattern and returns them as a list.
-   **Regex Capturing Group `(...)`**: Used to group part of a pattern and remember the text that it matches.
-   **Regex Backreference `\1`**: A special sequence that matches the text previously captured by the Nth group (in this case, the 1st group).

---

## What You Can Learn

-   **Regex Backreferences:** This is a perfect example of how to use backreferences (`\1`, `\2`, etc.) to find repeated or mirrored patterns in text.
-   **Choosing the Right `re` Function:** The solution highlights the important difference between `re.findall()` (find all) and `re.search()` (find the first). For problems that only require the first match, `re.search()` is more efficient and semantically more appropriate.

---

## Additional Resources

-   [Python `re` Module Documentation](https://docs.python.org/3/library/re.html)
-   [Regular-Expressions.info - Backreferences](https://www.regular-expressions.info/backref.html)

---

## Conclusion

This solution effectively uses a concise and powerful regular expression with a backreference to solve the problem. While it works correctly, it can be made more efficient by using `re.search()` instead of `re.findall()` to align with the problem's goal of finding only the first occurrence.

**Happy Coding!**
