# Drawing Book - Page Turn Counter

This repository contains a Python solution for the "Drawing Book" problem, which is a logic puzzle about finding the minimum number of page turns to reach a specific page in a book.

---

## Problem Statement

A student needs to turn to page **p** in a book of **n** pages. They can start turning from the front (page 1) or from the back. Page 1 is always on the right. Students turn pages one at a time. The goal is to find the minimum number of turns to reach page **p**.

### Input Format
- The first line contains **n**, the total number of pages in the book.
- The second line contains **p**, the page to turn to.

### Output Format
- A single integer representing the minimum number of page turns.

#### Sample Input

```
6
2
```

#### Sample Output

```
1
```

## Explanation

The provided solution first determines whether it's likely faster to start from the front or the back by comparing the target page `p` to the middle of the book (`n / 2`).

* **From the Front:** If the target page is in the first half of the book, the solution correctly calculates the number of turns as `p // 2` (integer division). This works because pages 2 and 3 require 1 turn, 4 and 5 require 2 turns, and so on.
* **From the Back:** If the target page is in the second half, the solution enters a complex series of nested `if/else` statements. It attempts to derive the number of turns from the back by handling cases for even and odd total page counts (`n`) separately, with further special conditions inside each branch.

---
## Algorithm Used

The algorithm is a **direct computation based on conditional logic**. It branches based on the target page's position (first half or second half of the book) and then uses different arithmetic formulas and checks depending on the properties of the input numbers.

### Time and Space Complexity

* **Your Solution & The Optimized Solution:**
    * **Time Complexity: `O(1)` (Constant Time)**. The solution involves a fixed number of simple arithmetic operations and comparisons. The number of calculations does not depend on the size of `n` or `p`.
    * **Space Complexity: `O(1)` (Constant Space)**. The memory used is constant and does not scale with the input.

---
## Key Functions and Modules

### Core Logic
-   **`if/elif/else`**: The primary control structure used to separate the logic for starting from the front versus the back, with further nested checks.
-   **`//` (Integer Division)**: Used to calculate the number of page turns from the front.
-   **`%` (Modulo Operator)**: Used to distinguish between books with an even or odd number of pages.

---

## What You Can Learn

-   **Problem Decomposition:** The solution demonstrates an attempt to solve a problem by breaking it down into many specific cases (front/back, even/odd).
-   **Searching for Simplicity:** It also highlights how this case-by-case approach can become very complex and difficult to manage. The key takeaway from this problem is to search for a simpler, more general mathematical formula or abstraction that can cover all cases, as this often leads to much cleaner and more robust code.

---

## Additional Resources

-   [Python Mathematical Operators](https://www.w3schools.com/python/python_operators.asp)

---

## Conclusion

This solution correctly approaches the problem by considering the two possible starting points. While the logic for calculating turns from the back is very complex, the underlying strategy is sound. It serves as a great example of how a problem with simple rules can lead to complex conditional logic if a unifying mathematical insight is not found.

**Happy Coding!**
