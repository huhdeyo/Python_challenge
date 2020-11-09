import urllib.request
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"
html = urllib.request.urlopen(url)
source = html.read()
mess = pickle.loads(source)
result = ""
for i in mess:
    for ch, j in i:
        if ch == '#' :
        # result += cur

# with open('list.txt', 'w') as f:
#     f.write(result)