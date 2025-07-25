from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    """
    A custom HTML parser to print start, end, and empty tags
    along with their attributes in a specific format.
    """

    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        self._print_attrs(attrs)

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        self._print_attrs(attrs)

    def _print_attrs(self, attrs):
        """Helper method to print attributes for a tag."""
        if not attrs:
            return
        for name, value in attrs:
            # Handle attributes that have no value (e.g., <... disabled>)
            print(f"-> {name} > {value if value is not None else 'None'}")


# Read number of lines
n = int(input())

# Concatenate all HTML lines into a single string
html_snippet = "".join(input() for _ in range(n))

# Create an instance of the parser and feed it the HTML
parser = MyHTMLParser()
parser.feed(html_snippet)
