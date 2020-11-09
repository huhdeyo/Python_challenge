import re

line = "Beautiful is better than ugly."
matches = re.findall("Beautiful", line)
# print(matches)
matches2 = re.findall("beautiful", line, re.IGNORECASE)
# print(type(matches2))

zen2 = """Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

m = re.findall("^If", zen2, re.MULTILINE)
m2 = re.findall("idea\.", zen2, re.MULTILINE)
m22 = re.findall("idea.", zen2, re.MULTILINE)
m3 = re.findall("idea.$", zen2, re.MULTILINE)
# print(m, m2, m22, m3)

string_ex = "Two aa too"
m = re.findall("t[ow]o", string_ex, re.IGNORECASE)
# print(m)
m = re.findall("t[^w]o", string_ex, re.IGNORECASE)
# print(m)

string_ex = "123?45yy7890 hi 999 hello"
m1 = re.findall("\d", string_ex)
m2 = re.findall("[0-9]{1,2}", string_ex)
m3 = re.findall("[1-5]{1,2}", string_ex)

# print("m1=", m1)
# print("m2=", m2)
# print("m3=", m3)
pattern = re.compile("(\d{1,3})")
mm = re.findall(pattern, string_ex)
# print(mm)

# for m in re.finditer(pattern, string_ex):
#     # print(m.groups())

string_ex = "aaaaa<hr>This"
pattern = re.compile("<(.*)>")
mm = re.findall(pattern, string_ex)
print(mm)
