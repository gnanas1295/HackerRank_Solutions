# Day of the Programmer Calculator

This repository contains a Python solution for the "Day of the Programmer" problem. This is a unique date calculation challenge that requires accounting for a historical calendar change and different leap year rules.

---

## Problem Statement

Determine the date of the 256th day of a given year in Russia. The calculation must account for the following historical calendar rules:
1.  **From 1700 to 1917 (Julian Calendar):** A leap year is any year divisible by 4.
2.  **Since 1919 (Gregorian Calendar):** A leap year is a year divisible by 400, or divisible by 4 but not by 100.
3.  **The year 1918 (Transition Year):** Russia switched calendars. The day after January 31st was February 14th, effectively skipping 13 days.

The date should be returned in the format `dd.mm.yyyy`.

### Input Format
- A single integer, `year`.

### Output Format
- A string with the full date in `dd.mm.yyyy` format.

#### Sample Input

```
2017
```

#### Sample Output

```
13.09.2017
```


## Explanation

The solution correctly identifies that the problem must be broken down into three distinct cases based on the year.

1.  **Gregorian Era (`year > 1918`):** The code applies the standard Gregorian leap year rule. If it's a leap year, February has 29 days, and the 256th day is September 12th. Otherwise, it's September 13th.
2.  **Julian Era (`year < 1918`):** The code applies the simpler Julian leap year rule (divisible by 4). It then determines if the 256th day is September 12th or 13th.
3.  **Transition Year (`year == 1918`):** For this unique year, 13 days were lost in February. The solution correctly returns the hardcoded date `26.09.1918`, which is the calculated 256th day for that specific year.

The solution uses an `if/elif/else` structure to select the correct logic for the given year and constructs the final date string.

---
## Algorithm Used

The algorithm is a **direct computation based on a set of rules**. It uses a series of conditional checks to select the correct formula. It does not involve iteration, recursion, or complex data structures, making it extremely efficient.

---
## Time and Space Complexity

### Your Solution & The Optimized Solution
* **Time Complexity: `O(1)` (Constant Time)**. The number of calculations (a few modulo operations and comparisons) is fixed and does not change regardless of the input `year`.
* **Space Complexity: `O(1)` (Constant Space)**. The memory used does not scale with the input. It uses a fixed amount of space for variables.

---
## Key Functions and Modules

### Core Logic
-   **`if/elif/else`**: The primary control structure used to differentiate between the three historical calendar periods.
-   **`%` (Modulo Operator)**: Used to perform the divisibility checks required for the leap year calculations.
-   **f-string**: Used for clean and readable formatting of the final date string.

---

## What You Can Learn

-   **Translating Complex Rules to Code:** This problem is an excellent example of how to convert a detailed set of historical and mathematical rules into a clear conditional logic structure.
-   **Handling Edge Cases:** The special handling of the year 1918 demonstrates the importance of identifying and isolating unique edge cases in a problem.
-   **Algorithmic Efficiency:** Shows that not all problems require complex algorithms. A direct, constant-time calculation is the most efficient solution here.

---

## Additional Resources

-   [The Julian and Gregorian Calendars](https://www.timeanddate.com/calendar/julian-gregorian-switch.html)
-   [Python Conditional Statements](https://www.w3schools.com/python/python_conditions.asp)

---

## Conclusion

This solution effectively solves a unique date-calculation problem by carefully implementing the specified historical rules. It showcases a clear, efficient, and direct approach using fundamental conditional logic.

**Happy Coding!**
