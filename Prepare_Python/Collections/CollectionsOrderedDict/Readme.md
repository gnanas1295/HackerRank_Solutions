# Net Price Aggregator Using OrderedDict

This repository contains a solution for calculating the net price of items sold in a supermarket. The challenge is to sum the prices for each unique item while preserving the order of their first appearance.

---

## Problem Statement

You are the manager of a supermarket. You have a list of items with their prices (each item may appear multiple times). Your task is to compute the net price for each item (i.e., the sum of its prices) and print the item names along with their net price in the order they first appear.

### Input Format
- The first line contains an integer, **N**, the number of items.
- The next **N** lines each contain the item's name and price separated by a space.

### Output Format
- Print the item name and its net price for each unique item, in the order of their first occurrence.

#### Sample Input

```
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
```

#### Sample Output

```
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
```

## Explanation

### Input Processing:
- We read all input lines using `sys.stdin.read()` and split them into a list with `.splitlines()`.
- The first line contains the number of items (n), and the remaining lines contain the item details.

### Using OrderedDict:
- An `OrderedDict` is used to maintain the insertion order, ensuring that items are printed in the order of their first occurrence.

### Aggregating Item Prices:
- **`items.get(item, 0)`**: Checks if the item already exists in the dictionary; if not, it returns `0`.
- **`int(price)`**: Converts the price from a string to an integer.
- The result is the current net price (or `0` if the item is new) plus the price of the current occurrence.
- This aggregated value is then assigned back to `items[item]`.

### Output:
- Finally, we iterate through the `OrderedDict` and print each item along with its aggregated net price.

---

## Key Functions and Modules

### Input Handling
- **`sys.stdin.read()`**  
  Reads the entire input from standard input as a single string.
- **`.splitlines()`**  
  Splits the input string into a list of lines.

### Collections Module
- **`collections.OrderedDict()`**  
  A dictionary that remembers the order of key insertion. This is crucial for preserving the order of the items as they first appear.

### Dictionary Methods
- **`.get(key, default)`**  
  Retrieves the value for a given key if it exists; otherwise, it returns the provided default value.  
  In our code, `items.get(item, 0)` ensures that if an item is not yet in the dictionary, its value defaults to `0` before adding the current price.
- **Updating Dictionary Values:**  
  The expression:
  ```python
  items[item] = items.get(item, 0) + int(price)
  ```
  succinctly adds the current price to the net price for that item.

### String Splitting
- **`rsplit(" ", 1)`**  
  Splits the string from the right at the last occurrence of a space. This is useful when the item name may contain spaces.

### Output Formatting
- Iterating through the `OrderedDict` allows us to print the items in their original order.

---

## What You Can Learn

- **Efficient Input Processing:**  
  Learn to handle multi-line input using `sys.stdin.read()` and `.splitlines()`.

- **Using OrderedDict:**  
  Understand how `OrderedDict` preserves insertion order, which is essential when order matters.

- **Dictionary Aggregation Patterns:**  
  The use of `items.get(item, 0) + int(price)` is a common idiom for summing values in a dictionary.

- **String Manipulation:**  
  Learn to use `rsplit()` to correctly separate data when the delimiter might be present in the data itself.

- **Code Optimization:**  
  Combining operations in a single loop for clarity and efficiency.

---

## Additional Resources

- [Python Collections: OrderedDict Documentation](https://docs.python.org/3/library/collections.html#collections.OrderedDict)
- [Python sys Module Documentation](https://docs.python.org/3/library/sys.html)
- [Python String Methods Documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)

---

## Conclusion

This solution demonstrates how to compute the net price of items using Python's `OrderedDict` along with efficient input handling and dictionary aggregation techniques. By working through this challenge, you'll gain a deeper understanding of data parsing, dictionary operations, and preserving order in Python.

**Happy Coding!**

