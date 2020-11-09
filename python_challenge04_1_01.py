import urllib.request
import urllib.parse
import re
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

data = {}
data['nothing'] = 66831
url_values = urllib.parse.urlencode(data)
full_url = url + '?' + url_values

html = urllib.request.urlopen(full_url)
the_page = html.read()
print(the_page)
# decoded_page = the_page.decode()
# num_s = re.findall("[0-9]*$", decoded_page)
# print(num_s[0])
# integer_val = int(num_s[0])