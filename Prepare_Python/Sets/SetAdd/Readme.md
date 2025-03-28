# Distinct Country Stamps Counter

This repository contains a solution for a challenge where you need to count the total number of distinct country stamps from a collection. The task is to determine how many unique country names are present in the input list.

---

## Problem Statement

Rupal has a huge collection of country stamps. She decides to count the total number of distinct country stamps in her collection. You are given a number of country stamps followed by the country name for each stamp. Your task is to compute the total number of distinct country stamps.

### Input Format
- The first line contains an integer **N**, the total number of country stamps.
- The next **N** lines each contain the name of the country where the stamp is from.

### Output Format
- Print the total number of distinct country stamps on a single line.

#### Sample Input

```
7
UK
China
USA
France
New Zealand
UK
France
```

#### Sample Output

```
5
```

## Explanation

- **Input Processing:**  
  The code reads all input lines using `sys.stdin.read()` and splits them into a list of strings with `.splitlines()`. The first line contains the number of stamps, and the following lines contain the country names for each stamp.

- **Counting Distinct Stamps:**  
  By converting the list of stamps (ignoring the first line) into a set, duplicate country names are automatically removed.  
  Then, the length of the set (i.e., the number of unique country names) is printed.

---

## Key Functions and Modules

### Input Handling
- **`sys.stdin.read()`**  
  Reads the entire input from standard input as a single string.
- **`.splitlines()`**  
  Splits the input string into a list of lines.

### Set Data Structure
- **`set()`**  
  A set is a collection of unique elements. Converting a list to a set removes duplicate values.
- **`len()`**  
  Returns the number of elements in a collection, which, in this case, is the number of distinct country stamps.

---

## What You Can Learn

- **Efficient Input Processing:**  
  How to handle multi-line input using `sys.stdin.read()` and `.splitlines()`.

- **Using Sets for Uniqueness:**  
  Learn how converting a list to a set can be used to quickly identify unique elements, which is a common pattern in problems that require deduplication.

- **Simplifying Code:**  
  Combining the operations into a concise solution can improve both the readability and efficiency of your code.

---

## Additional Resources

- [Python sys Module Documentation](https://docs.python.org/3/library/sys.html)
- [Python Set Documentation](https://docs.python.org/3/tutorial/datastructures.html#sets)
- [Python Built-in Functions: len()](https://docs.python.org/3/library/functions.html#len)

---

## Conclusion

This solution demonstrates how to count distinct elements by efficiently processing input and using Python's set data structure to remove duplicates. By working through this challenge, you'll deepen your understanding of input handling, data structures, and concise coding practices.

**Happy Coding!**