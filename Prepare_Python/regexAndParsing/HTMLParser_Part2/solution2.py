from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
        
    def handle_data(self, data):
        # The strip() method removes all leading/trailing whitespace.
        # An empty string is 'falsy', so this prints only if there is
        # non-whitespace content.
        if data.strip():
            print(">>> Data")
            print(data)
            
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
