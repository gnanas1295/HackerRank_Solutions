# HTML Parser Challenge

This repository contains a Python solution for a challenge that involves parsing an HTML snippet and printing its tags and attributes according to a specific format, using Python's built-in `html.parser` module.

---

## Problem Statement

You are given an HTML code snippet. Your task is to use Python's `html.parser` to parse the snippet and print the start tags, end tags, and empty tags in the order of their occurrence. For tags with attributes, you must also print their names and values.

### Input Format
- The first line contains an integer, **N**, the number of lines in the HTML snippet.
- The next **N** lines contain the HTML code.

### Output Format
- Print the tags and their attributes formatted as follows:
  - `Start : tag_name`
  - `End   : tag_name`
  - `Empty : tag_name`
- If a tag has attributes, print them on subsequent lines, prefixed with `->`:
  - `-> attribute_name > attribute_value`
- If an attribute has no value, print its value as `None`.

#### Sample Input

```
2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
```

#### Sample Output
```
Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html
```

## Explanation

The solution involves creating a custom class that inherits from `html.parser.HTMLParser`. We then override its "handler" methods to control what happens when the parser encounters different parts of the HTML.

  - `handle_starttag()` is called for tags like `<html>` or `<body ...>`.
  - `handle_endtag()` is called for tags like `</html>` or `</body>`.
  - `handle_startendtag()` is called for empty tags like `<br />`.

Inside these methods, we print the required output, iterating through any attributes and handling cases where an attribute value might be `None`.

-----

## Key Functions and Modules

### `html.parser` Module

  - **`HTMLParser` Class**: The base class we inherit from to create our custom parser.
  - **`.feed(data)`**: This method is used to pass the HTML string to the parser instance.
  - **Handler Methods**:
      - **`handle_starttag(self, tag, attrs)`**: Processes opening tags. The `attrs` argument is a list of `(name, value)` tuples.
      - **`handle_endtag(self, tag)`**: Processes closing tags.
      - **`handle_startendtag(self, tag, attrs)`**: Processes self-closing or "empty" tags.

-----

## What You Can Learn

  - **Using Standard Libraries**: How to leverage powerful built-in Python modules like `html.parser` for common tasks.
  - **Object-Oriented Programming**: The practical application of inheritance by subclassing a base class (`HTMLParser`) and overriding its methods to create custom behavior.
  - **Event-Driven Parsing**: Understanding the concept of event-driven programming, where code execution is triggered by specific events (like finding a start tag).
  - **Handling Edge Cases**: The importance of checking for special conditions, such as attributes with no assigned value.

-----

## Additional Resources

  - [Python `html.parser` Documentation](https://docs.python.org/3/library/html.parser.html)

-----

## Conclusion

This solution demonstrates a practical and effective way to parse HTML in Python. By creating a custom parser class, you gain fine-grained control over how HTML is processed, allowing for flexible and powerful data extraction and analysis.

**Happy Coding\!** 🐍
