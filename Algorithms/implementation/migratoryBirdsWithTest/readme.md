# Migratory Birds - Frequency Counter

This repository contains a Python solution for the "Migratory Birds" problem, which involves finding the most frequently occurring item in a list, with specific rules for tie-breaking.

---

## Problem Statement

You are given an array representing a series of bird sightings, where each element is an ID for a bird type. Your task is to find the bird type that was sighted most frequently. If there is a tie for the most frequent type, return the type with the smallest ID.

### Input Format
- The first line contains an integer **n**, the size of the array.
- The second line contains **n** space-separated integers representing the bird type IDs.

### Output Format
- A single integer representing the ID of the most frequent bird type (and the smallest ID in case of a tie).

#### Sample Input

```
6
1 4 4 4 5 3
```

#### Sample Output

```
4
```

## Explanation

The provided solution uses Python's `collections.Counter` to efficiently count the occurrences of each bird type in the input array.

1.  **Frequency Counting:** It first creates a `Counter` object from the input list, which results in a dictionary-like object mapping each bird ID to its frequency.
2.  **Sorting by Frequency:** It then calls the `.most_common()` method, which returns a list of `(id, count)` tuples, sorted by count in descending order.
3.  **Tie-Breaking Logic:** The code then attempts to handle ties by explicitly checking if the count of the first element in the sorted list (`count[0][1]`) is equal to the count of the second element (`count[1][1]`). If they are tied, it returns the smaller of the two IDs. Otherwise, it returns the ID of the most common element.

---
## Algorithm Used

The algorithm uses a **Frequency Count** approach. It leverages a hash map (via `collections.Counter`) to count items in O(N) time. It then uses a partial sort (`.most_common()`) to order the items by frequency to find the most common one.

---
## Time and Space Complexity

### Your Solution
* **Time Complexity: `O(N)`**. Building the `Counter` takes O(N) time. The `.most_common()` method takes O(k log k) time, where `k` is the number of unique bird types. Since `k` is at most 5, this is a constant factor. Therefore, the overall complexity is dominated by the initial counting, making it O(N).
* **Space Complexity: `O(k)`**. The `Counter` object stores one entry for each unique bird type. Since there are at most 5 unique types, this is effectively O(1) or constant space.

### Optimized Solution
* **Time Complexity: `O(N)`**. The solution makes a single pass through the input array of size N to populate the frequency counts. Finding the max value and its index in the small, fixed-size `counts` array takes constant time.
* **Space Complexity: `O(1)`**. The `counts` array has a fixed size of 6 regardless of the input size N, making the space complexity constant.

---
## Key Functions and Modules

### Core Logic
- **`collections.Counter`**: A specialized dictionary subclass for counting hashable objects. It is the primary tool used to get the frequency of each bird type.
- **`.most_common()`**: A method of `Counter` that returns a list of the `n` most common elements and their counts from the most common to the least.

---

## What You Can Learn

-   **Using `collections.Counter`:** This is a perfect example of how to use Python's specialized collections to write clean and efficient counting code.
-   **Handling Tie-Breakers:** The problem highlights the importance of carefully considering tie-breaking rules. The solution attempts to handle this, but its logic is incomplete as it only considers a two-way tie, revealing a common edge case to watch out for.
-   **Analyzing Constraints:** The optimal solution leverages the problem's constraint (bird types are 1-5) to use a simple array as a highly efficient frequency map, which is a common optimization technique in competitive programming.

---

## Additional Resources

-   [`collections.Counter` Documentation](https://docs.python.org/3/library/collections.html#collections.Counter)

---

## Conclusion

This solution effectively uses a powerful tool from Python's standard library to solve the core counting part of the problem. It serves as a great illustration of `collections.Counter` and also as a valuable lesson in the importance of creating robust logic to handle all possible tie-breaking scenarios.

**Happy Coding!**
