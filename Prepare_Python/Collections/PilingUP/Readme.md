# Cube Stacking Challenge

## Problem Statement

There is a horizontal row of cubes, each with a given side length. Your task is to create a new vertical pile (stack) of cubes following these rules:
- You can only pick up either the leftmost or the rightmost cube from the row.
- When stacking, if cube A is placed on top of cube B, then the side length of A must be less than or equal to that of B.
- Determine if it is possible to stack the cubes following these restrictions.

Print "Yes" if it is possible; otherwise, print "No".

## Input Format

- The first line contains a single integer **T**, the number of test cases.
- For each test case:
  - The first line contains an integer **n**, the number of cubes.
  - The second line contains **n** space-separated integers representing the side lengths of the cubes.

## Output Format

For each test case, output a single line containing either "Yes" or "No".

## Sample Input

```
STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]
```
## Sample Output
```
Yes
No
```


## Explanation

- **Test Case 1:**  
  It is possible to stack the cubes in an order that satisfies the condition (for example, by selecting cubes in the order: left, right, left, right, left, right).  
- **Test Case 2:**  
  No matter how the cubes are picked from the ends, it is impossible to form a stack where each cube is not larger than the cube below it.

## Key Functions and Modules Used

- **`sys.stdin.read()`**  
  Used for efficient reading of input.
- **Two-Pointer Technique:**  
  Instead of modifying the list (which is inefficient when using `pop(0)`), two pointers are used to simulate removing elements from both ends.
- **Control Structures:**  
  A `while` loop is used to process elements from the list based on the pointers until the stacking is determined to be possible or impossible.

## What You Can Learn

- **Efficient Data Processing:**  
  Using two pointers to avoid the inefficiency of repeatedly modifying a list.
- **Greedy Algorithms:**  
  How a greedy strategy can be applied to decide which cube to choose next.
- **Input Handling in Python:**  
  Techniques for reading and processing multiple test cases efficiently using `sys.stdin.read()`.

## Additional Resources

- [Python sys.stdin.read() Documentation](https://docs.python.org/3/library/sys.html#sys.stdin)
- [Two-Pointer Technique](https://www.geeksforgeeks.org/two-pointers-technique/)
- [Greedy Algorithms in Python](https://www.programiz.com/dsa/greedy-algorithm)

## Conclusion

This challenge demonstrates the power of efficient input processing and the two-pointer technique to solve a stacking problem under restricted conditions. It offers a practical example of how greedy strategies can be implemented in Python to solve problems with specific order constraints.

**Happy Coding!**

