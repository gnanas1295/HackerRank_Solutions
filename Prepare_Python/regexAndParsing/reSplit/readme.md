# Regex: Splitting on Delimiters

This repository contains a Python solution for a challenge that involves using regular expressions to split a string by multiple delimiters.

---

## Problem Statement

You are given a string that consists of digits, commas (`,`), and dots (`.`). Your task is to define a regular expression pattern that can be used with Python's `re.split()` function to split the string on every comma and every dot.

### Input Format
- A single line containing the string of digits, commas, and dots.

### Output Format
- The parts of the string, separated by newlines.

#### Sample Input

```
100,000,000.000
```

#### Sample Output

```
100
000
000
000
```

## Explanation

The provided solution focuses on defining a single, concise regular expression pattern.

1.  **Define Pattern:** The solution sets `regex_pattern = r"[,.]"`. This pattern defines a **character set**.
2.  **Split String:** The `re.split()` function takes this pattern and the input string. It scans the string and breaks it into a list of substrings, using any character that matches the pattern (either a comma or a dot) as a delimiter. For the input `100,000,000.000`, this results in the list `['100', '000', '000', '000']`.
3.  **Format Output:** The `"\n".join()` method is then used to join the elements of the resulting list together, with a newline character between each one, producing the final output.

---
## Algorithm Used

The solution uses **Regular Expressions** for tokenization (splitting a string into a sequence of substrings). It does not use a complex algorithm but rather a direct application of a built-in function.

### Time and Space Complexity

* **Time Complexity: `O(L)`**, where `L` is the length of the input string. The `re.split()` function makes a single pass through the string to find all delimiters.
* **Space Complexity: `O(L)`**. In the worst case, the list of split strings returned by `re.split()` can have a total size proportional to the original string.

---
## Key Functions and Modules

### Core Logic
-   **`re.split(pattern, string)`**: The primary function from Python's `re` module used to split a string by the occurrences of a pattern.
-   **Regex Character Set `[...]`**: The core of the pattern. `[,.]` creates a character set that tells the regex engine to match a single character that is *either* a literal comma or a literal dot.
-   **`str.join(iterable)`**: A string method used to concatenate the elements of an iterable into a single string, with the string itself as a separator.

---

## What You Can Learn

-   **Using `re.split()`:** This is a fundamental demonstration of how to split strings based on a pattern, which is more powerful than the basic `str.split()` method.
-   **Regex Character Sets:** Shows the simplest way to define multiple alternative characters for a match or, in this case, for a delimiter.
-   **Concise Problem Solving:** This challenge is a lesson in finding the simplest tool for the job. A complex pattern is not needed when a simple character set suffices.

---

## Additional Resources

-   [Python `re.split()` Documentation](https://docs.python.org/3/library/re.html#re.split)
-   [Regular-Expressions.info - Character Classes](https://www.regular-expressions.info/charclass.html)

---

## Conclusion

This solution is a perfect example of a simple, elegant, and correct answer to a regex challenge. It uses the most direct pattern possible to achieve the desired result, demonstrating a solid understanding of fundamental regex concepts.

**Happy Coding!**
