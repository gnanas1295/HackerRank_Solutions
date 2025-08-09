# Counting Valleys - Hiker's Journey

This repository contains a Python solution for the "Counting Valleys" problem, which is a classic challenge involving state tracking during a sequence of events.

---

## Problem Statement

A hiker walks a path of **steps** consisting of uphill (`U`) and downhill (`D`) steps. The hike starts and ends at sea level (altitude 0). A "valley" is defined as a sequence of steps strictly below sea level, starting with a step down from sea level and ending with a step up to sea level. Your task is to count the number of valleys the hiker traversed.

### Input Format
- The first line contains an integer **steps**, the number of steps.
- The second line contains a string **path** describing the sequence of steps.

### Output Format
- A single integer representing the total number of valleys walked through.

#### Sample Input

```
8
UDDDUDUU
```

#### Sample Output

```
1
```

## Explanation

The provided solution tracks the hiker's journey by maintaining state with two key variables: the current altitude (`tempCounter`) and a boolean flag (`downHill`) to know if the hiker is currently inside a valley.

1.  **Iteration:** It iterates through each `step` in the `path` string.
2.  **Altitude Tracking:** For each step, it updates `tempCounter`: `+1` for an uphill step (`U`) and `-1` for a downhill step (`D`).
3.  **State Management:** After each step, it checks the altitude.
    * If the altitude is below sea level (`< 0`), it sets the `downHill` flag to `True`, indicating the hiker is in a valley.
    * The key condition is `elif tempCounter == 0 and downHill:`. This is only true at the exact moment the hiker returns to sea level *and* the `downHill` flag is `True`. This signifies the completion of one valley.
4.  **Counting:** When a valley is completed, the `seaLevelReached` counter is incremented, and the `downHill` flag is reset.

---
## Algorithm Used

The algorithm is a **Stateful Iteration**, which is a form of **Simulation**. It makes a single pass through the input sequence, and at each step, it updates a set of state variables (`altitude`, `in_a_valley`) based on the current input and the previous state.

### Time and Space Complexity

* **Your Solution & The Optimized Solution:**
    * **Time Complexity: `O(N)`**, where `N` is the number of steps in the path. The solution requires a single pass through the input string.
    * **Space Complexity: `O(1)`**. The solution uses a fixed number of variables to track the state, regardless of the number of steps. The memory usage is constant.

---
## Key Functions and Modules

### Core Logic
-   **`for` loop**: The primary structure for iterating through each step of the hiker's path.
-   **`if/elif/else`**: Used to manage the state transitions: updating the altitude, detecting when the hiker is in a valley, and identifying the moment a valley is completed.
-   **State Variables**: The use of an integer `tempCounter` for altitude and a boolean `downHill` flag are central to the logic.

---

## What You Can Learn

-   **Stateful Programming:** This problem is a classic example of solving a problem by simulating its process step-by-step and tracking the current "state" with variables.
-   **Using Flags:** Demonstrates how a boolean flag can be used to "remember" a past event (having entered a valley) that is critical for making a future decision (counting the valley upon exiting).
-   **Problem Simplification:** While the flag-based approach is correct, this problem can also be solved more simply by only checking for the single event that defines the start (or end) of a valley. This is a good lesson in looking for the simplest possible condition to check.

---

## Additional Resources

-   [Python Control Flow (if, for, etc.)](https://docs.python.org/3/tutorial/controlflow.html)

---

## Conclusion

This solution is a solid and correct implementation that effectively simulates the hiker's journey. It's a great example of how to use state variables and flags to solve problems that involve tracking changes over a sequence of events.

**Happy Coding!**
