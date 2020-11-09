import requests
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html"
html = requests.get(url)
html_txt = html.text

comment = html_txt.split("<!--\n")[1].split("-->")[0]
pattern = re.compile("[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]")
results = re.findall(pattern, comment)

sorted_re = ""
for ch in results:
    sorted_re += ch[4]

print(sorted_re)
