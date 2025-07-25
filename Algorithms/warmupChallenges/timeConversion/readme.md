## Time Conversion (12-hour to 24-hour)

This repository contains an efficient Python solution for converting a time from 12-hour AM/PM format to 24-hour (military) format.

---

## Problem Statement

Given a time in 12-hour AM/PM format (e.g., `07:05:45PM`), convert it to 24-hour format (e.g., `19:05:45`).

**Special Cases:**
* 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
* 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

### Input Format
-   A single string `s` in `hh:mm:ssAM` or `hh:mm:ssPM` format.

### Output Format
-   The time in `HH:MM:SS` 24-hour format.

#### Sample Input

```
07:05:45PM
```

#### Sample Output
```
19:05:45
```

## Algorithm Explanation

This is a classic **String Parsing and Manipulation** problem. The core of the algorithm is a set of conditional rules to transform the hour component based on the AM/PM indicator.

### Algorithmic Perspectives

1.  **String Slicing (Optimal Approach)**: For a fixed-format input string, the most efficient algorithm is to directly parse the components using string slicing. This approach has a time complexity of **O(1)** because the length of the string is constant and the operations (slicing, splitting, conversion) do not depend on the input size. It directly accesses the required memory locations without needing to evaluate a complex pattern.

2.  **Regular Expressions (Alternative Approach)**: Another way to parse the string is by using a regular expression. The regex engine matches the pattern against the string to extract the components. While this is a powerful and flexible method for variable formats, it carries more computational overhead than simple slicing for a fixed format. Its time complexity is still effectively **O(1)** for a short, fixed-length string, but it is less performant in practice.

### Conversion Logic
The transformation logic relies on four conditions:
-   If the time is **PM** and the hour is **1-11**, add 12 to the hour.
-   If the time is **PM** and the hour is **12**, the hour remains 12.
-   If the time is **AM** and the hour is **12**, the hour becomes 0.
-   If the time is **AM** and the hour is **1-11**, the hour remains the same.

---

## Key Functions and Concepts

-   **String Slicing**: Using `s[:-2]` and `s[-2:]` to efficiently separate the time from the AM/PM indicator.
-   **`str.split(':')`**: To break the time component into hours, minutes, and seconds.
-   **Conditional Logic (`if/elif`)**: To apply the specific conversion rules.
-   **Formatted Strings (f-strings)**: Using `f"{hour:02d}"` to format the final hour as a two-digit string with a leading zero if necessary.

---

## What You Can Learn

-   **Choosing the Right Tool**: Understanding when to use simple string slicing over more powerful tools like regular expressions for better performance on fixed-format data.
-   **Handling Edge Cases**: How to identify and implement logic for special cases, such as 12 AM and 12 PM, which often break general rules.
-   **Efficient String Formatting**: Using f-strings with format specifiers is the modern, readable, and efficient way to construct strings in Python.

---

## Additional Resources

-   [Python String Slicing](https://realpython.com/python-strings/#string-slicing)
-   [Python F-Strings](https://realpython.com/python-f-strings/)

---

## Conclusion

This solution demonstrates an optimal, clean, and efficient method for a common time conversion task. By leveraging direct string slicing and clear conditional logic, the code is both performant and easy to understand.

**Happy Coding!** 🕒
