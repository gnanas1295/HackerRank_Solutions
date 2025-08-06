# Find All Overlapping Substring Indices

This repository contains a Python solution for a challenge that involves finding all starting and ending indices of a substring within a larger string, including any overlapping occurrences.

---

## Problem Statement

You are given two strings, a main string **S** and a substring **k**. Your task is to find all occurrences of **k** within **S** and print the 0-indexed `(start, end)` tuple for each match. The end index should be inclusive. If no matches are found, you should print `(-1, -1)`.

### Input Format
- The first line contains the main string **S**.
- The second line contains the substring **k**.

### Output Format
- Print each `(start, end)` tuple on a new line.
- If no matches are found, print a single line `(-1, -1)`.

#### Sample Input

```
aaadaa
aa
```

#### Sample Output

```
(0, 1)
(1, 2)
(4, 5)
```

## Explanation

The provided solution uses an advanced regular expression technique to find all possible matches, including those that overlap.

1.  **The Pattern:** It defines the pattern `rf'(?=({strToComp}))'`.
    * `(?=...)` is a **positive lookahead**. This is a "zero-width" assertion, meaning it checks for a pattern at a certain position but doesn't "consume" any characters. This is the key to finding overlapping matches. Because it doesn't consume characters, the regex engine can advance just one character at a time.
    * `(...)` is a **capturing group** inside the lookahead. This is what actually matches and captures the substring we are looking for.
2.  **Iteration and Matching:** It uses `re.finditer()` to get an iterator that yields a `match` object for every position where the lookahead finds the substring.
3.  **Handling No Match:** A `flag` variable is used to track whether any matches have been found. It's initialized to `False` and set to `True` inside the loop if a match is found. After the loop, if the flag is still `False`, it knows to add `(-1, -1)` to the results.
4.  **Storing and Printing:** For each `match` object, it calculates the inclusive `(start, end)` indices and appends the result as a formatted string to a list. The main program block then prints each item from this list.

---
## Algorithm Used

The core of the solution is a **Regular Expression** that uses a **zero-width positive lookahead** to enable the finding of all **overlapping matches**. This is a powerful, non-trivial regex technique.

### Time and Space Complexity

* **Time Complexity: `O(S * K)`**, where `S` is the length of the main string and `K` is the length of the substring. In the worst case, the regex engine may need to check for the substring `K` at every one of the `S` positions.
* **Space Complexity: `O(M * L)`**, where `M` is the number of matches found and `L` is the average length of the string representation of an index tuple. This space is required to store the list of results.

---
## Key Functions and Modules

### Core Logic
-   **`re.finditer(pattern, string)`**: Returns an iterator yielding `match` objects over all non-overlapping (but in this case, overlapping due to the lookahead) matches for the pattern in the string.
-   **Positive Lookahead `(?=...)`**: The key regex feature that makes finding overlapping matches possible.
-   **Capturing Group `(...)`**: Used within the lookahead to capture the actual substring text, allowing access to its start and end indices via `match.start(1)` and `match.end(1)`.

---

## What You Can Learn

-   **Advanced Regex for Overlapping Matches:** This solution is a perfect demonstration of how to use zero-width lookaheads, a powerful but non-obvious feature, to solve problems that standard regex functions cannot handle easily.
-   **The `re.finditer()` Iterator:** Shows the use of `finditer` for memory-efficiently processing a potentially large number of matches.
-   **Handling "Not Found" Cases:** The use of a flag variable is a standard programming pattern to keep track of state (e.g., "was anything found?") during an iteration.

---

## Additional Resources

-   [Python `re` Module Documentation](https://docs.python.org/3/library/re.html)
-   [Regular-Expressions.info - Lookarounds](https://www.regular-expressions.info/lookaround.html)

---

## Conclusion

This is a very clever and correct solution that effectively uses an advanced regex feature to overcome the default non-overlapping behavior of standard search functions. It's a great example of the power and flexibility of regular expressions.

**Happy Coding!**
