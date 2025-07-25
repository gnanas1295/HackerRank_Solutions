# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from html import parser


noOfLines = int(sys.stdin.readline().strip())
# htmlData = sys.stdin.read()

class MyHTMLParser(parser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for key, value in attrs:
                print(f"-> {key} > {value if value else 0}")

htmlDataToBeParsed = sys.stdin.read()

parser = MyHTMLParser()
parser.feed(htmlDataToBeParsed)
