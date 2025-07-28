# Apple and Orange Counter

This repository contains a Python solution for the "Apple and Orange" problem, which involves calculating the number of fruits that land within a specific area on a 1D axis.

---

## Problem Statement

Sam's house is located on a 1D axis from a start point **s** to an end point **t**. An apple tree is at location **a**, and an orange tree is at location **b**. When a fruit falls, it travels a certain distance **d** along the axis from its parent tree. Given the locations of the house and trees, and the fall distances for a set of apples and oranges, determine how many of each fruit land on Sam's house.

### Input Format
- The first line contains **s** and **t** (house location).
- The second line contains **a** and **b** (tree locations).
- The third line contains **m** and **n** (number of apples and oranges).
- The fourth line contains **m** distances for apples.
- The fifth line contains **n** distances for oranges.

### Output Format
- Print two lines:
  1. The total number of apples on the house.
  2. The total number of oranges on the house.

#### Sample Input

```
7 11
5 15
3 2
-2 2 1
5 -6
```

#### Sample Output

```
1
1
```

## Explanation

The provided solution calculates the number of fruits landing on the house by rearranging the problem's core inequality.

For a fruit to land on the house, its final position must be between **s** and **t**.
-   Apple position: `a + d_apple`
-   The condition is: `s <= a + d_apple <= t`

Instead of calculating the final position, the code rearranges this inequality to solve for the distance `d`:
-   `s - a <= d_apple <= t - a`

The solution then iterates through each apple's fall distance and checks if it falls within this calculated range. A counter is incremented for each valid fruit. The same logic is applied to the oranges. Finally, the total counts for apples and oranges are printed.

---

## Key Functions and Modules

### Core Logic
-   **`for` loop:** To iterate through the list of fall distances for both apples and oranges.
-   **Conditional (Ternary) Operator:** The line `applesAtHome += 1 if (condition) else 0` provides a concise, one-line way to check the condition and increment the counter.
-   **Mathematical Inequality:** The solution is built around checking if a fruit's fall distance fits within a range derived from algebraic manipulation of the problem's conditions.

---

## What You Can Learn

-   **Problem Translation:** This problem is a good exercise in translating a real-world scenario into a mathematical model on a coordinate plane.
-   **Looping and Conditionals:** It demonstrates the fundamental programming pattern of iterating through a collection of data and applying a conditional test to each item.
-   **Algebraic Manipulation:** The solution shows how rearranging an inequality can be an alternative approach to solving a problem, which can sometimes simplify the required calculations.

---

## Additional Resources

-   [Python For Loops](https://wiki.python.org/moin/ForLoop)
-   [Python Conditional Expressions (Ternary Operator)](https://docs.python.org/3/reference/expressions.html#conditional-expressions)

---

## Conclusion

This solution effectively solves the problem by applying a clever mathematical transformation of the core condition. It demonstrates a solid understanding of loops and conditional logic to count items that meet a specific set of criteria.

**Happy Coding!**
