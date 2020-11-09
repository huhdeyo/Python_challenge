import string

caption = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

lower_case = string.ascii_lowercase

new_case = ""

for i in range(len(lower_case)):
    j = (i+2)% (len(lower_case))
    new_case = new_case + lower_case[j] 

new_caption = caption.maketrans(lower_case, new_case)

print(caption.translate(new_caption))