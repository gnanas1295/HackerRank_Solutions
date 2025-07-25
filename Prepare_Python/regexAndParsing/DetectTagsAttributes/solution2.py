# In short, the parser doesn't really see "lines"; it just sees a continuous stream of characters. Feeding it line-by-line is just a way of feeding it that stream in smaller chunks. It always remembers where it was in the process.
# Parser is the stateful object meaning it will store the context and continues from where it left off.


# import sys
# from html.parser import HTMLParser

# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print(tag)
#         if attrs:
#             for name, value in attrs:
#                 print(f"-> {name} > {value}")


# html_input = sys.stdin.read()

# parser = MyHTMLParser()
# parser.feed(html_input)

import sys
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        # Store results in a list instead of printing immediately
        self.output = []

    def handle_starttag(self, tag, attrs):
        self.output.append(tag)
        if attrs:
            for name, value in attrs:
                self.output.append(f"-> {name} > {value}")

# --- Main script ---
parser = MyHTMLParser()
for line in sys.stdin:
    parser.feed(line)

# Join the list and print everything in one go
print('\n'.join(parser.output))
