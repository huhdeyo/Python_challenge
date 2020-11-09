import string

def pyChallenge(beforeTrans):
    new_string = ""
    for letter in beforeTrans:
        found_position = string.ascii_lowercase.find( letter )
        if found_position == -1:
            new_string += letter
            continue
        index = (found_position + 2) % len(string.ascii_lowercase)

        new_string += string.ascii_lowercase[index]
    return new_string

if __name__ == "__main__":
    caption = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    afterTrans = pyChallenge(caption)
    print(afterTrans)
    print("-"*100)
    url = "map"
    afterTrans = pyChallenge(url)
    print(afterTrans)