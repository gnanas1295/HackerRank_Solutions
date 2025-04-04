# Word Occurrence Counter Challenge

## Problem Statement

You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the order in which the word first appears in the input.

## Input Format

- The first line contains an integer **n**, the number of words.
- The next **n** lines each contain a single word composed of lowercase English letters.

## Output Format

- The first line should contain the number of distinct words.
- The second line should contain the number of occurrences for each distinct word, in the order of their first appearance, separated by a space.

## Sample Input

```
4
bcdef
abcdefg
bcde
bcdef
```

## Sample Output

```
3
2 1 1
```


## Explanation

- There are 3 distinct words:  
  - "bcdef" appears twice.
  - "abcdefg" appears once.
  - "bcde" appears once.
- The order of first appearance is: "bcdef", "abcdefg", "bcde".
- Therefore, the output first prints the count of distinct words (`3`), followed by the counts in order (`2 1 1`).

## Key Functions and Modules Used

- **`sys.stdin.read()`**  
  Reads the entire input from standard input, allowing efficient processing of multiple lines.

- **`collections.OrderedDict` (or a normal dictionary in Python 3.7+ since insertion order is preserved)**  
  Maintains the order of first occurrence of each word while storing their counts.

- **Dictionary Methods:**  
  - `.get(word, default)` is used to retrieve the count for a word, defaulting to 0 if the word isn't present, making it easy to increment counts.

## What You Can Learn

- **Efficient Input Processing:**  
  Handling and processing multi-line input using `sys.stdin.read()`.

- **Preserving Order in Dictionaries:**  
  Understanding how to use `OrderedDict` or leverage Python 3.7+'s built-in dictionaries that preserve insertion order, which is essential for outputting the results in the correct order.

- **Counting Occurrences:**  
  Learn how to efficiently count occurrences of items in a collection using dictionary methods.

## Additional Resources

- [Python Collections - OrderedDict](https://docs.python.org/3/library/collections.html#collections.OrderedDict)
- [Python sys Module Documentation](https://docs.python.org/3/library/sys.html)
- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

## Conclusion

This challenge is an excellent exercise in efficiently processing input, counting item occurrences, and maintaining order using dictionaries. It reinforces practical skills in Python that are widely applicable in data processing and algorithmic problem solving.

**Happy Coding!**