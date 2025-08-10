# Electronics Shop - Budget Purchase Calculator

This repository contains a Python solution for the "Electronics Shop" problem, which involves finding the most expensive combination of two items that can be purchased within a given budget.

---

## Problem Statement

A person wants to buy a computer keyboard and a USB drive. Given price lists for different models of keyboards and USB drives, and a budget **b**, find the maximum amount of money that can be spent. If it's not possible to buy one of each within the budget, the answer should be -1.

### Input Format
- The first line contains **b** (budget), **n** (number of keyboard models), and **m** (number of drive models).
- The second line contains **n** prices for keyboards.
- The third line contains **m** prices for USB drives.

### Output Format
- A single integer representing the maximum amount of money that can be spent, or -1 if no valid combination exists.

#### Sample Input

```
10 2 3
3 1
5 2 8
```

#### Sample Output

```
9
```

## Explanation

The provided solution uses Python's `itertools` library to find all possible combinations and then determines the most expensive valid option.

1.  **Generate All Pairs:** It first uses `itertools.product(keyboards, drives)` to generate a Cartesian product, which is every possible pair of one keyboard and one drive.
2.  **Filter and Sum:** It then uses a list comprehension, `[i+j for i,j in combi if i+j <= b]`, to create a list of sums. This list only includes the sums of pairs that are less than or equal to the budget **b**.
3.  **Sort for the Maximum:** This list of valid prices is then sorted in descending order (`reverse=True`).
4.  **Find the Result:** The code iterates through the sorted list and returns the very first price it finds, as this will be the highest possible amount. If the list is empty (no valid pairs were found), it returns -1.

---
## Algorithm Used

The algorithm is a **brute-force** approach. It systematically generates and checks every possible combination of one keyboard and one USB drive to find the optimal one that fits the criteria.

### Time and Space Complexity

* **Your Solution:**
    * **Time Complexity: `O(n*m log(n*m))`**. Where `n` is the number of keyboards and `m` is the number of drives. `O(n*m)` to generate all pair sums, and `O(k log k)` (where `k = n*m`) to sort them.
    * **Space Complexity: `O(n*m)`**. Requires space to store the list of all possible pair sums in memory.

* **Optimized Solution (Generator):**
    * **Time Complexity: `O(n*m)`**. It still needs to check every pair, but it avoids the expensive sort operation.
    * **Space Complexity: `O(1)`**. A generator expression does not store the entire list of sums in memory, making it far more memory-efficient.

---
## Key Functions and Modules

### Core Logic
-   **`itertools.product(iter1, iter2)`**: The core function used to efficiently generate the Cartesian product of the keyboard and drive price lists.
-   **List Comprehension**: Used to create a list of sums from the generated pairs, with an `if` clause to filter out sums that are over budget.
-   **`sorted()`**: The built-in function used to sort the list of valid prices in descending order to easily find the maximum.

---

## What You Can Learn

-   **Using `itertools.product`:** This is a perfect example of how `itertools` can simplify problems involving combinations or pairings of items from multiple lists.
-   **Filtering with List Comprehensions:** The solution shows how to embed an `if` condition within a list comprehension to create a new list that only contains items meeting a specific criterion.
-   **Thinking About Efficiency:** The solution works perfectly for the given constraints. Comparing it to a more memory-efficient generator-based solution highlights the importance of considering space complexity for larger datasets.

---

## Additional Resources

-   [`itertools.product` Documentation](https://docs.python.org/3/library/itertools.html#itertools.product)
-   [Python List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

---

## Conclusion

This solution is a very clear and clever implementation that uses powerful Python features to solve the problem directly. It's a great demonstration of the `itertools` library and list comprehensions.

**Happy Coding!**
