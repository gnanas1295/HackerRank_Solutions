# HTML Comment and Data Parser

This repository provides a Python solution for a challenge that involves parsing an HTML snippet to identify and format single-line comments, multi-line comments, and data content.

---

## Problem Statement

You are given an HTML code snippet. Your task is to use Python's `html.parser` to process the snippet and print its comments and data content in a specific, structured format. You must differentiate between single-line and multi-line comments.

### Input Format
-   The first line contains an integer, **N**, the number of lines in the HTML snippet.
-   The next **N** lines contain the HTML code.

### Output Format
-   Print the results in the order of their occurrence.
-   Data that consists only of a newline character (`\n`) should be ignored.
-   The output must be formatted as follows:
    ```
    >>> Single-line Comment
    Comment text
    >>> Multi-line Comment
    Multi-line comment text
    >>> Data
    Data text
    ```

#### Sample Input

```
4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->
```

#### Sample Output

```
>>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]
```

## Explanation

The solution uses a custom class inheriting from `html.parser.HTMLParser`. We override two key methods:

  - `handle_comment(data)`: This method is triggered when a comment is found. Inside, we check if the `data` string contains a newline character (`\n`). If it does, we classify it as a multi-line comment; otherwise, it's a single-line comment.
  - `handle_data(data)`: This method is triggered for text content. We use `data.strip()` to remove all surrounding whitespace. If the result is not an empty string, we print the original data. This correctly filters out data that is just `\n` or other whitespace.

-----

## Key Functions and Modules

### `html.parser` Module

  - **`HTMLParser` Class**: The base class for our custom parser.
  - **`handle_comment(self, data)`**: The handler method for processing comments. We inspect the `data` string to determine the comment type.
  - **`handle_data(self, data)`**: The handler method for processing text nodes. We inspect the `data` string to ensure it contains actual content before printing.

### String Methods

  - **`str.strip()`**: Used to check if the data contains any non-whitespace characters, providing a robust way to filter out empty text nodes.

-----

## What You Can Learn

  - **Advanced `html.parser` Usage**: How to handle different types of content like comments and data using specific handler methods.
  - **Content-Based Logic**: How to inspect the string data passed to a handler to make decisions (e.g., distinguishing single-line vs. multi-line comments).
  - **Robust Text Filtering**: Using string methods like `strip()` to effectively clean and validate text data before processing.

-----

## Additional Resources

  - [Python `html.parser` Documentation](https://docs.python.org/3/library/html.parser.html)
  - [Python `str.strip()` Documentation](https://docs.python.org/3/library/stdtypes.html#str.strip)

-----

## Conclusion

This solution demonstrates how to build a simple yet effective HTML parser in Python. By implementing the correct logic within the handler methods, you can accurately classify and format different types of HTML content according to specific rules.

**Happy Coding\!** 📄
