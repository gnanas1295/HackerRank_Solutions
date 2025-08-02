# Bon Appétit - Bill Split Calculator

This repository contains a Python solution for the "Bon Appétit" problem, a challenge that involves verifying a shared bill calculation.

---

## Problem Statement

Anna and Brian are splitting a dinner bill. Brian calculates Anna's portion, but he might have made a mistake by including an item that Anna didn't eat. Your task is to determine if Anna was overcharged. If she was, print the amount she is owed. If the calculation was correct, print "Bon Appetit".

### Input Format
- The first line contains **n** (number of items) and **k** (the index of the item Anna didn't eat).
- The second line contains the costs of the **n** items.
- The third line contains **b**, the amount Brian charged Anna.

### Output Format
- Print "Bon Appetit" if the charge was correct.
- Otherwise, print the integer amount Brian must refund to Anna.

#### Sample Input

```
4 1
3 10 2 9
12
```

#### Sample Output

```
5
```

## Explanation

The provided solution directly calculates Anna's fair share of the bill.

1.  **Remove Item:** It first takes the list of all item costs (`bill`) and removes the item Anna didn't eat using the `bill.pop(k)` method. This modifies the list, leaving only the items that were shared.
2.  **Calculate Share:** It then calculates the `sum()` of the costs in this new, shorter list and divides it by two to determine Anna's actual share.
3.  **Compare and Print:** Finally, it compares this calculated share to the amount Anna was charged (`b`). A conditional f-string is used to print "Bon Appetit" if the amounts are equal, or the difference (`b - eachShare`) if Anna was overcharged.

---
## Algorithm Used

The algorithm is a **direct computation**. It follows the problem's logic by removing the unshared item, summing the remaining items, and performing a final comparison.

### Time and Space Complexity

* **Your Solution:**
    * **Time Complexity: `O(N)`**. The `sum(bill)` operation takes O(N) time. The `bill.pop(k)` operation can also take up to O(N) time in the worst case (if `k` is at the beginning of the list), because subsequent elements must be shifted. Therefore, the overall complexity is linear.
    * **Space Complexity: `O(1)`**. The list is modified *in-place*, so no significant extra space is used that scales with the input size.

* **Optimized Solution (No Side Effects):**
    * **Time Complexity: `O(N)`**. The `sum(bill)` operation is the dominant step, taking O(N) time. The rest of the operations are constant time. The complexity is still linear, but it avoids the potentially costly `pop` operation, making it slightly faster in practice.
    * **Space Complexity: `O(1)`**. No extra space that scales with the input size is used.

---
## Key Functions and Modules

### Core Logic
-   **`list.pop(index)`**: A list method used to remove an item at a specific index. It's important to note that this method **modifies the original list**.
-   **`sum(iterable)`**: The built-in function used to calculate the sum of the items in the list.
-   **f-string**: Used for a concise and readable way to format the final output string.

---

## What You Can Learn

-   **Direct Problem Solving:** The solution is a great example of a direct and straightforward implementation of a problem's requirements.
-   **Function Side Effects:** This solution provides a practical example of a function with "side effects" (modifying its inputs). While it works here, it's a crucial concept in software design to understand why this is often discouraged in favor of "pure" functions that do not modify external state. This helps prevent unexpected bugs in larger applications.

---

## Additional Resources

-   [Python `list.pop()` Documentation](https://docs.python.org/3/tutorial/datastructures.html)
-   [Understanding Side Effects in Programming](https://en.wikipedia.org/wiki/Side_effect_(computer_science))

---

## Conclusion

This solution correctly calculates the bill split in a simple and direct manner. It serves as an excellent illustration of basic list manipulation and also provides a valuable learning opportunity about the important programming concept of function side effects.

**Happy Coding!**
