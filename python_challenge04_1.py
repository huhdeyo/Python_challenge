import urllib.request
import urllib.parse
import re
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

def get_num(bef):
    data = {}
    data['nothing'] = bef
    url_values = urllib.parse.urlencode(data)
    full_url = url + '?' + url_values

    html = urllib.request.urlopen(full_url)
    the_page = html.read()
    decoded_page = the_page.decode()
    num_s = re.findall("[0-9]*$", decoded_page)
    integer_val = int(num_s[0])
    return integer_val

if __name__ == "__main__":
    cur_val = 8022
    for i in range(400):
        print(i, cur_val)
        cur_val = get_num(cur_val)

