# HackerLand University Grade Rounding

This repository contains a Python solution for a grading policy problem where student grades are rounded up based on a specific set of rules.

---

## Problem Statement

HackerLand University has the following grading policy:
1.  Every student receives a grade in the inclusive range from 0 to 100.
2.  Any grade less than 40 is a failing grade.
3.  If the difference between a student's grade and the next multiple of 5 is less than 3, round the grade up to that multiple of 5.
4.  If the grade is less than 38, no rounding occurs as the result will still be a failing grade.

Your task is to automate the rounding process for a given list of grades.

### Input Format
- The first line contains an integer **n**, the number of students.
- The next **n** lines each contain a single integer representing a student's grade.

### Output Format
- Return an integer array consisting of the rounded grades.

#### Sample Input

```
4
73
67
38
33
```

#### Sample Output

```
75
67
40
33
```

## Explanation

The provided solution iterates through each student's grade and applies the rounding rules.

1.  **Check for Failing Grades:** The code first checks if a grade is less than 38. If it is, no rounding is performed, and the original grade is kept.
2.  **Apply Rounding Logic:** If the grade is 38 or higher, it checks if the grade's remainder when divided by 5 is 3 or greater. This is a shortcut to see if the grade is close to the next multiple of 5.
3.  **Calculate Rounded Grade:** If the condition is met, it calculates the nearest multiple of 5 using the formula `round(grade/5) * 5` and uses that as the final grade. Otherwise, the original grade is kept.
4.  **Return Final Grades:** The final list of processed grades is returned.

---

## Key Functions and Modules

### Core Logic
- **`for` loop:** To iterate through the list of initial grades.
- **`if/else` statement:** To separate the logic for grades below 38 from those that are eligible for rounding.
- **Conditional (Ternary) Operator:** Used for a concise one-line check: `(rounded_value) if (condition) else (original_value)`.
- **`%` (Modulo Operator):** Used to find the remainder when a grade is divided by 5, which helps determine if the grade is a candidate for rounding.
- **`round()`:** The built-in Python function used to calculate the nearest multiple of 5.

---

## What You Can Learn

- **Implementing Custom Rules:** This problem is a great exercise in translating a specific set of business or academic rules into conditional logic.
- **Conditional Logic:** Demonstrates the use of `if/else` statements and ternary operators to handle different cases within a dataset.
- **List Manipulation:** Shows a common pattern of iterating through a list and building a new, modified list based on a set of transformations.

---

## Additional Resources

- [Python `round()` Function Documentation](https://docs.python.org/3/library/functions.html#round)
- [Conditional Expressions in Python](https://docs.python.org/3/reference/expressions.html#conditional-expressions)

---

## Conclusion

This solution provides a direct approach to implementing the specified grading policy. It effectively uses conditional logic and basic arithmetic to process a list of numbers according to a unique set of rounding rules.

**Happy Coding!**
