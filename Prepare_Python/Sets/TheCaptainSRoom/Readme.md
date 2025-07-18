# Captain's Room Finder

This repository contains a Python solution to efficiently identify a unique room number in a list where all other room numbers appear a fixed number of times (`k`). This problem leverages an elegant mathematical property of sets and sums.

---

## Problem Statement

Mr. Anant Asankhya manages the INFINITE hotel, which has an infinite number of rooms. A finite number of tourists arrive, consisting of a single Captain and an unknown number of family groups, each with `k` members (where `k` is not equal to 1). The Captain receives a separate room, and each family group receives one room.

You are given an unordered list of room entries, where each family group's room number appears `k` times, and the Captain's room number appears only once. Your task is to find the Captain's room number. The total number of tourists or family groups is not known. You only have `k` and the list of room numbers.

### Input Format
- The first line consists of an integer `k`, representing the size of each family group (i.e., how many times family room numbers repeat).
- The second line contains a space-separated list of integers, which are the room numbers for all tourists.

#### Constraints
- The value of `k` will be a positive integer and `k != 1`.
- Room numbers will be positive integers.

### Output Format
- Output a single integer: the Captain's room number.

#### Sample Input

```
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
```

#### Sample Output
```
8
```

## Explanation

The core insight for solving this problem efficiently comes from observing the sums of elements.

Let:
- `k` be the number of times each family room number repeats.
- `C` be the Captain's room number (appears once).
- `F_i` be a distinct room number for a family group.

Consider the sum of all room numbers in the input list (`sum_all_rooms`):
`sum_all_rooms = C * 1 + (F1 * k + F2 * k + ... + Fm * k)`
`sum_all_rooms = C + k * (F1 + F2 + ... + Fm)`

Now, consider the sum of all *unique* room numbers (`sum_unique_rooms`). If we convert the input list to a `set`, we get all distinct room numbers, including the Captain's room and each family's room once:
`sum_unique_rooms = C + (F1 + F2 + ... + Fm)`

We want to isolate `C`. Let's multiply `sum_unique_rooms` by `k`:
`k * sum_unique_rooms = k * (C + F1 + F2 + ... + Fm)`
`k * sum_unique_rooms = k * C + k * (F1 + F2 + ... + Fm)`

Now, subtract `sum_all_rooms` from `k * sum_unique_rooms`:
`(k * sum_unique_rooms) - sum_all_rooms = (k * C + k * (F1 + ... + Fm)) - (C + k * (F1 + ... + Fm))`
`(k * sum_unique_rooms) - sum_all_rooms = k * C - C`
`(k * sum_unique_rooms) - sum_all_rooms = C * (k - 1)`

Therefore, the Captain's room number `C` is:
`C = (k * sum_unique_rooms - sum_all_rooms) / (k - 1)`

This formula elegantly extracts the unique element.

## Alternative Approach (Using `collections.Counter`)

While the summation method is concise, another intuitive approach involves frequency counting:

1.  Use `collections.Counter` to count the occurrences of each room number.
2.  Iterate through the items (room number, count) in the Counter.
3.  The room number whose count is `1` is the Captain's room.

This approach is also `O(N)` and might be more immediately obvious to some. The summation method is often preferred for its mathematical elegance and potentially slightly fewer operations.

---

## Key Functions and Modules

### Python Built-in Functions
-   **`int(input())`**: Reads a line from standard input and converts it to an integer.
-   **`input().split()`**: Reads a line from standard input and splits it into a list of strings by whitespace.
-   **`map(int, iterable)`**: Applies the `int()` function to each item in the `iterable`, returning an iterator of integers. This is used to convert room number strings to actual integers.
-   **`list()`**: Converts an iterable (like the output of `map`) into a list.
-   **`set()`**: Converts an iterable into a `set`, which stores only unique elements. This effectively removes duplicate room numbers.
-   **`sum(iterable)`**: Calculates the sum of all numeric items in an `iterable`.
-   **`//` (Integer Division)**: Used to ensure the result of the division is an integer, as room numbers are whole numbers.

### Optional (Alternative approach)
-   **`collections.Counter`**: A dictionary subclass for counting hashable objects. It's excellent for frequency counting.

---

## Learning Points

-   **Mathematical Properties of Sets and Sums:** This problem beautifully demonstrates how mathematical properties, when combined with appropriate data structures (like sets), can lead to highly efficient and elegant solutions.
-   **Identifying Unique Elements:** Understanding various techniques to find unique elements in a list (e.g., using sets, frequency maps) is a fundamental skill.
-   **Efficiency Considerations:** Both the summation method and `collections.Counter` provide `O(N)` solutions, making them suitable for large inputs. Choosing between them often comes down to personal preference or specific edge cases not present here.
-   **Type Conversion Importance:** Always ensure that data is in the correct type (`int` for arithmetic operations) as early as possible to prevent errors.

---

## Additional Resources

-   [Python Sets Documentation](https://docs.python.org/3/tutorial/datastructures.html#sets)
-   [Python `sum()` function](https://docs.python.org/3/library/functions.html#sum)
-   [Python `map()` function](https://docs.python.org/3/library/functions.html#map)
-   [Python `collections` module (for Counter)](https://docs.python.org/3/library/collections.html#collections.Counter)

---

**Find the Captain, secure the room!**
