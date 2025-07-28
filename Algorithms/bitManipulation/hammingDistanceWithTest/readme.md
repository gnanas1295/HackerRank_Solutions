# Dynamic String Manipulator (List-Based Approach)

This repository contains a straightforward Python solution for a complex string manipulation problem. This implementation uses Python's built-in `list` data structure to handle all operations.

---

## Problem Statement

You are given a string `S`, consisting of `N` lowercase letters 'a' and 'b'. You must process `M` queries of the following types:

* `C l r c`: Change all symbols in the substring `S[l...r]` to character `c`.
* `S l1 r1 l2 r2`: Swap two consecutive fragments of the string, `S[l1...r1]` and `S[l2...r2]`.
* `R l r`: Reverse the fragment `S[l...r]`.
* `W l r`: Output the substring `S[l...r]`.
* `H l1 l2 len`: Output the Hamming distance between the substrings `S[l1...l1+len-1]` and `S[l2...l2+len-1]`.

All indices are 1-based.

### Input Format
- The first line contains an integer **N**, the length of the string.
- The second line contains the initial string **S**.
- The third line contains an integer **M**, the number of queries.
- The next **M** lines each contain a query.

### Output Format
- For each query of type **W** or **H**, print the answer on a new line.

#### Sample Input

```
10
aabbbabbab
6
R 1 5
W 3 8
C 4 4 a
H 2 1 9
S 5 9 10 10
H 1 2 9
```

#### Sample Output

```
baaabb
4
5
```

## Explanation

This solution works by converting the input string into a list of characters, which is mutable and allows for easy modification. Each query is handled by a dedicated function that manipulates this list directly.

-   **`R 1 5`**: The first five elements `['a', 'a', 'b', 'b', 'b']` are sliced and reversed, resulting in the list representing `bbbaaabbab`.
-   **`S 5 9 10 10`**: The list is split into multiple parts corresponding to the ranges and then reassembled with the two target fragments swapped.
-   **`W` and `H`**: These queries slice the relevant portions of the list and then either join them for printing or iterate over them for comparison.

---

## Key Functions and Modules

This solution relies on direct list manipulation and standard library modules.

### Core Logic
-   **List as a String Buffer**: The primary data structure is a `list` of characters, which acts as a mutable string.
-   **`change(list, start, end, char)`**: Uses list slice assignment (`list[start:end] = ...`) to replace a range of characters.
-   **`swap(list, ...)`**: Manually slices the list into up to five distinct segments and rebuilds it by concatenating the slices in the new, swapped order.
-   **`reversing(list, start, end)`**: Slices the target segment, reverses it in place, and assigns it back to the main list.
-   **`outPutting(list, ...)`** and **`hamming(list, ...)`**: Use list slicing to extract the necessary substrings for their respective tasks.

### Modules Used
-   **`sys`**: The `sys.stdin.readline()` function is used for efficient reading of input lines.

---

## What You Can Learn

-   **Fundamental List Operations**: This code is a great example of using Python's powerful list slicing and manipulation capabilities to solve complex problems.
-   **Mutable vs. Immutable**: It highlights the practical use of a `list` (mutable) to handle operations that would be inefficient with standard `string` objects (immutable).
-   **Problem Decomposition**: Shows how to break a larger problem down into smaller, manageable functions, with each function handling a specific query type.

---

## Additional Resources

-   [Python Documentation: More on Lists](https://docs.python.org/3/tutorial/datastructures.html)
-   [Real Python: Python's `sys` Module](https://realpython.com/python-sys-module/)
-   [GeeksForGeeks: Python String Slicing](https://www.geeksforgeeks.org/string-slicing-in-python/)

---

## Conclusion

This implementation serves as a solid, readable baseline for solving string manipulation challenges. It's a testament to the power of Python's core data structures for rapid prototyping and problem-solving.

**Happy Coding!**
