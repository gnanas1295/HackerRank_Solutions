# Deque Operations Challenge

## Problem Statement

You are given a number of operations to perform on an initially empty deque. The operations include `append`, `pop`, `popleft`, and `appendleft`. Your task is to execute these operations and print the resulting elements of the deque separated by a space.

## Input Format

- The first line contains an integer **n**, the number of operations.
- The next **n** lines each contain a command and (optionally) a value, separated by a space. The commands are:
  - `append x`
  - `appendleft x`
  - `pop`
  - `popleft`

## Output Format

- Print the space-separated elements of the deque after performing all operations.

## Sample Input

```
6
append 1
append 2
append 3
appendleft 4
pop
popleft
```

## Sample Output

```
1 2
```


## Explanation

- **Step 1:** Start with an empty deque.
- **Step 2:** `append 1` → deque becomes `[1]`.
- **Step 3:** `append 2` → deque becomes `[1, 2]`.
- **Step 4:** `append 3` → deque becomes `[1, 2, 3]`.
- **Step 5:** `appendleft 4` → deque becomes `[4, 1, 2, 3]`.
- **Step 6:** `pop` → removes `3` from the right, deque becomes `[4, 1, 2]`.
- **Step 7:** `popleft` → removes `4` from the left, deque becomes `[1, 2]`.

The final deque is printed as: `1 2`.

## Key Functions and Modules Used

- **`collections.deque`**  
  Provides a double-ended queue that allows appending and popping from both ends with efficient O(1) operations.

- **`sys.stdin.read()`**  
  Reads all input at once, which is useful for handling multiple lines of input efficiently.

- **`str.split()`**  
  Splits input strings into components, allowing us to separate the command from its value.

## What You Can Learn

- **Deque Operations:**  
  Understand how to efficiently add and remove elements from both ends of a deque.

- **Input Parsing:**  
  Learn techniques for reading and processing multi-line input in Python.

- **Command Dispatching:**  
  See how to use conditional logic (or even mapping techniques) to dispatch commands to corresponding operations.

## Additional Resources

- [Python collections.deque Documentation](https://docs.python.org/3/library/collections.html#collections.deque)
- [Python sys Module Documentation](https://docs.python.org/3/library/sys.html)
- [Deque Recipes in Python](https://docs.python.org/3/library/collections.html#deque-recipes)

## Conclusion

This challenge demonstrates the use of the `deque` data structure for efficient double-ended operations. By solving this problem, you'll enhance your skills in input handling, conditional logic, and using Python’s powerful standard library.

**Happy Coding!**
