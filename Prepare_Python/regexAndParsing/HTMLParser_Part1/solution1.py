# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser


class myHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")


numOfCases = int(input())


parser = myHtmlParser()

for _ in range(numOfCases):
    parser.feed(input())
