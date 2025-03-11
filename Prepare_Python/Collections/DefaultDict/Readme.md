
## DefaultDict_Tutorial Overview

This folder contains a HackerRank challenge solution that uses Python's `defaultdict` to map words to their positions. In this challenge:

- **Group A** contains `n` words.
- **Group B** contains `m` words.

For each word in Group B, the task is to print the 1-indexed positions where the word occurs in Group A. If a word does not appear in Group A, output `-1`.

### Sample I/O

**Input:**

```
5 2 
a 
a 
b 
a 
b 
a 
b
```
**Output:**

```
1 2 4 
3 5
```


## Solutions

### Solution 1: Initial Approach

- **Method:**
  - Reads input using `sys.stdin.read()` and splits the input into tokens.
  - Separates Group A and Group B words manually.
  - Uses nested loops to iterate over Group A and store positions in a `defaultdict`.
  - For each word in Group B, checks if it exists in the dictionary and prints the 1-indexed positions or `-1` if not found.

- **Key Concepts Learned:**
  - How to use the `defaultdict` from the `collections` module.
  - Basic input handling and list manipulation.
  - Converting string inputs to integers.
  - Using loops and conditionals to build data structures.

### Solution 2: Optimized Pythonic Approach

- **Method:**
  - Uses slicing to split the input into Group A and Group B efficiently.
  - Employs the `enumerate()` function with `start=1` to iterate through Group A, which provides both the index (as a 1-indexed value) and the word in a single loop.
  - Utilizes the unpacking operator (`*`) with `print()` to output the positions neatly.
  
- **Key Concepts Learned:**
  - Efficient input handling and slicing.
  - How `enumerate()` simplifies tracking indices during iteration.
  - Printing lists using the unpacking operator to achieve clean output formatting.
  - The benefits of writing Pythonic code for improved readability and performance.

## Key Python Concepts and Functions

### Input Handling
- **sys.stdin.read() & .split():**
  - Reads all input at once, which is useful in competitive programming.
  - Splits the input into a list of strings for easy processing.

### List Manipulation and Slicing
- **Lists:**
  - Used to store groups of words.
- **Slicing:**
  - Efficiently separates parts of the input into Group A and Group B (e.g., `data[2:2+n]`).

### defaultdict from collections
- **defaultdict:**
  - Automatically initializes an empty list for new keys, avoiding manual key checks.
  - Simplifies the process of mapping each word to its list of occurrence positions.

### enumerate
- **enumerate():**
  - Iterates over a list while keeping track of the index.
  - The `start=1` parameter makes it easy to work with 1-indexed positions, aligning with problem requirements.

### Print Unpacking
- **Unpacking Operator (`*`):**
  - The statement `print(*word_positions[word])` unpacks the list so that each element is printed as a separate argument, resulting in a space-separated output.
- **join() Method:**
  - Although not used in these solutions, it can be a handy alternative for joining list elements into a string.

## Conclusion

This repository highlights the evolution from a straightforward, initial solution to a more optimized, Pythonic approach. By comparing both solutions, you gain a deeper understanding of:

- Efficient input handling and data manipulation.
- How to use Python’s built-in functions and data structures (like `defaultdict` and `enumerate()`) effectively.
- Writing clean and maintainable code through the use of concise syntax and optimized loops.

Feel free to explore, run the code, and even contribute with your improvements!

---

# Happy Coding!