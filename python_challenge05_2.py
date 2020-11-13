import urllib.request
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"
html = urllib.request.urlopen(url)
source = html.read()
mess = pickle.loads(source)

result = ""
for i in mess:
        for ch, j in i:
                if ch == '#': result += '#'*j
                if ch == ' ': result += ' '*j
        print(result)
        result = ""