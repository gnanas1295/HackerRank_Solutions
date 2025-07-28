# Kangaroo Meet-Up Calculator

This repository contains a Python solution for the "Kangaroo" problem, which determines if two kangaroos moving at constant rates will ever land on the same spot at the same time.

---

## Problem Statement

Two kangaroos are on a number line. The first starts at location **x1** and moves **v1** meters per jump. The second starts at **x2** and moves **v2** meters per jump. Both jump in the positive direction. The task is to determine if they can ever be at the same location at the same time.

### Input Format
- A single line of four space-separated integers: **x1**, **v1**, **x2**, and **v2**.

### Output Format
- Print **YES** if they can meet, otherwise print **NO**.

#### Sample Input

```
0 3 4 2

```

#### Sample Output

```
YES
```

## Explanation

The provided solution attempts to solve the problem mathematically rather than by simulating each jump.

1.  **Calculate Differences:** It first calculates the absolute difference between the starting points (`x1`, `x2`) and the velocities (`v1`, `v2`).
2.  **Estimate Jumps:** It uses integer division (`//`) on these differences to get a rough estimate of the number of jumps it would take for the kangaroos to meet.
3.  **Check Final Positions:** It then calculates the final position of both kangaroos after that estimated number of jumps.
4.  **Compare and Conclude:** Finally, it compares these calculated final positions. If they are equal, it returns "YES"; otherwise, it returns "NO".

---
## Algorithm Used

This solution does not use a named algorithm like "brute-force" or "binary search." Instead, it uses a **direct mathematical formula** to try and solve the problem. It models the kangaroos' movements as linear equations and attempts to solve for a common point without simulating the jumps one by one.

---
## Key Functions and Modules

### Core Logic
- **`abs()`**: The built-in function to get the absolute value of a number, used here to find the magnitude of the differences in position and velocity.
- **`//` (Integer Division):** Used to calculate the number of jumps. This operator divides and then rounds the result down to the nearest whole number.

---

## What You Can Learn

-   **Mathematical Modeling:** This problem is a great example of how a physical scenario can be modeled with simple linear equations.
-   **Avoiding Brute-Force:** The solution demonstrates the value of trying to find a mathematical formula to solve a problem directly, which is often more efficient than simulating every step.
-   **Integer vs. Float Division:** The use of `//` highlights the importance of understanding the difference between integer division (which truncates) and standard division (`/`), as this distinction is key to the logic.

---

## Additional Resources

-   [Python `abs()` Function](https://docs.python.org/3/library/functions.html#abs)
-   [Numeric Types in Python](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

---

## Conclusion

This solution provides a mathematical attempt to solve the Kangaroo problem. By calculating differences and estimating jumps, it directly checks a potential meeting point, showcasing a valuable alternative to step-by-step simulation.

**Happy Coding!**
