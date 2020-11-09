from bs4 import BeautifulSoup as bs
from bs4 import Comment
from pprint import pprint
import requests
import string

url = "http://www.pythonchallenge.com/pc/def/ocr.html"

html = requests.get(url)
soup = bs(html.text, 'html.parser')

comments = soup.findAll(text=lambda text:isinstance(text, Comment))
text_com = "%s"%(comments[1])
line_results = text_com.split("\n")
chr_results = ""

for line in line_results:
    for ch in line:
        if ch in string.ascii_letters:
            chr_results += ch
print(chr_results)