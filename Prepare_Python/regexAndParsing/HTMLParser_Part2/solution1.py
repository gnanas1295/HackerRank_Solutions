from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def handle_comment(self, data):
        dataLines = data.splitlines()
        if len(dataLines) >1:
            print(">>> Multi-line Comment")
            print(data)
        elif len(dataLines) == 1:
            print(">>> Single-line Comment")
            print(data)

        
    def handle_data(self, data):
        if len(data) > 1:
            print(">>> Data")
            print(data)
        
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
