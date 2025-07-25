# Detect HTML Tags, Attributes and Values

This repository contains a Python solution for a challenge that involves parsing an HTML snippet to detect and print all HTML tags and their attributes in a specific custom format.

---

## Problem Statement

You are given an HTML code snippet. Your task is to detect and print all the HTML tags, along with their attributes and attribute values. Comments should be ignored.

### Input Format
-   The first line contains an integer, **N**, the number of lines in the HTML code snippet.
-   The next **N** lines contain the HTML code.

### Output Format
-   Print the tags and attributes in the order of their occurrence.
-   If a tag has no attributes, print only the tag name.
-   If a tag has attributes, print the tag name on one line, followed by its attributes on subsequent lines, formatted as `-> attribute_name > attribute_value`.

#### Sample Input

```
9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
```

#### Sample Output
```
head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high
```

## Explanation

The solution uses Python's built-in `html.parser.HTMLParser`. A custom class `MyHTMLParser` is created that inherits from it.

We only need to override the `handle_starttag(self, tag, attrs)` method. This method is automatically called by the parser for both start tags (e.g., `<object ...>`) and empty tags (e.g., `<param ... />`).

Inside this method, we first print the `tag` name. Then, we check if the `attrs` list is not empty. If it contains attributes, we loop through it and print each `(name, value)` pair in the required format.

-----

## Key Functions and Modules

### `html.parser` Module

  - **`HTMLParser` Class**: The base class used to create our custom event-driven parser.
  - **`handle_starttag(self, tag, attrs)`**: The handler method that is called whenever the parser encounters a start tag or an empty tag. The `attrs` argument is a list of `(name, value)` tuples representing the tag's attributes.

### `sys` Module

  - **`sys.stdin.read()`**: Used to efficiently read the entire multi-line HTML input from the user at once.

-----

## What You Can Learn

  - **Event-Driven Parsing**: How to use the `html.parser` library to process HTML based on events like encountering a start tag.
  - **Handling Attributes**: How to access and iterate through the attributes of an HTML tag within the parser.
  - **Efficient Input Handling**: Using `sys.stdin.read()` to manage multi-line input streams effectively.

-----

## Additional Resources

  - [Python `html.parser` Documentation](https://docs.python.org/3/library/html.parser.html)
  - [Python `sys` Module Documentation](https://docs.python.org/3/library/sys.html)

-----

## Conclusion

This solution showcases how to use Python's `html.parser` to build a simple but powerful tool for extracting structured information from HTML. By overriding a single method, we can fulfill the custom printing requirements of the challenge efficiently.

**Happy Coding\!** 💻
