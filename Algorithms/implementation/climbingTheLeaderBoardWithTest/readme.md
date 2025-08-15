# Climbing the Leaderboard - Dense Ranking

This repository contains an efficient Python solution for the "Climbing the Leaderboard" problem, which involves calculating a player's rank in a dense ranking system.

---

## Problem Statement

An arcade game uses a "Dense Ranking" system:
1.  The player with the highest score gets rank #1.
2.  Players with equal scores receive the same rank.
3.  The next rank awarded is the immediately following integer (e.g., ranks can be 1, 2, 2, 3, 4, 4, 4, 5).

Given a descending list of leaderboard scores (`ranked`) and an ascending list of a player's scores (`player`), determine the player's rank after each game they play.

### Input Format
-   The first line contains **n**, the number of leaderboard scores.
-   The second line contains **n** space-separated `ranked` scores.
-   The third line contains **m**, the number of player scores.
-   The fourth line contains **m** space-separated `player` scores.

### Output Format
-   An array of integers representing the player's rank after each game.

#### Sample Input

```
7
100 100 50 40 40 20 10
4
5 25 50 120
```

#### Sample Output

```
6
4
2
1
```

## Explanation of the Code

The solution uses an efficient **two-pointer technique** to avoid re-scanning the entire leaderboard for each of the player's new scores.

1.  **Prepare Leaderboard:** It first creates a clean, sorted list of unique scores from the input `ranked` list. This represents the actual ranks (e.g., `[100, 50, 40, 20, 10]` corresponds to ranks 1, 2, 3, 4, 5).
2.  **Initialize Pointers:** It initializes a pointer (`scorePtr`) to the end of the unique leaderboard (pointing to the lowest score). A second implicit pointer iterates through the `player` scores.
3.  **Single Pass Iteration:** The code iterates through the player's scores (which are sorted ascending). For each new `playerScr`, it moves the `scorePtr` up the leaderboard (towards higher scores) as long as the player's score is greater than or equal to the leaderboard score at that position.
4.  **Calculate Rank:** Because the `scorePtr` is **never reset**, it efficiently finds the player's rank in a single coordinated pass through both lists. The rank is calculated as `scorePtr + 2` and appended to a results list. The `+2` is because the index is 0-based, ranks are 1-based, and the player's rank is one position *after* the pointer.

---
## Algorithm Used

The algorithm is a **Two-Pointer Technique**. This is a highly efficient approach for problems involving two sorted arrays. By moving the pointers in a coordinated way (one iterating forward through player scores, the other moving backward through the ranked list), it avoids the O(N*M) complexity of a naive brute-force search.

### Time and Space Complexity

* **Your Solution & The Optimized Solution:**
    * **Time Complexity: `O(N + M)`**. `set(ranked)` and `sorted()` take roughly O(N) time. The main loop is O(N + M) because each pointer (`scorePtr` and the implicit player score pointer) traverses its respective list only once. The total complexity is linear.
    * **Space Complexity: `O(k)`**, where `k` is the number of unique scores on the leaderboard. This space is needed to store the unique ranks.

---
## Key Functions and Modules

### Core Logic
-   **`set()`**: Used to get the unique scores from the leaderboard.
-   **`sorted()`**: Used to re-sort the unique scores into descending order.
-   **`while` loop**: The engine for the core two-pointer logic, which efficiently moves the leaderboard pointer up the ranks as the player's score increases.

---

## What You Can Learn

-   **The Two-Pointer Algorithm:** This solution is a perfect example of this classic algorithm pattern. It shows how to solve a problem efficiently by leveraging the sorted nature of input data to avoid redundant work.
-   **Stateful Iteration:** Instead of restarting a search for each new item, the `scorePtr` maintains its state, which is the key to the solution's linear time complexity.
-   **Data Deduplication:** Demonstrates a standard pattern of cleaning up data (removing duplicates with `set`) before processing.

---

## Additional Resources

-   [Two Pointer Technique - GeeksForGeeks](https://www.geeksforgeeks.org/two-pointers-technique/)

---

## Conclusion

This is an excellent, efficient solution to the "Climbing the Leaderboard" problem. It correctly identifies and implements the two-pointer technique, resulting in clean, readable, and performant code that can handle large inputs.

**Happy Coding!**
