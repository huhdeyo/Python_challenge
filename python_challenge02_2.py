import requests

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
html = requests.get(url)
html_txt = html.text

mess = html_txt.split("-->")[1].split("<!--\n")[1]
items = {}
for item in mess:
    if item in items:
        items[item] += 1
    else:
        items[item] = 1

found = []
for key in items.keys():
    if( items[key] > 1):
        found += [key]

for item in found:
    mess = mess.replace(item, "")

print(mess)
