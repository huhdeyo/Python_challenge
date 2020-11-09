# cha_st = nsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
cha_st = "map"
result = []
for word in cha_st.split(" "):
    word_result = []
    for ch in word:
        a = ord(ch)
        if a >= 97 and a <= 122:
            a = (( a -95) % 26) + 97
        word_result.append(chr(a))
    line_result = "".join(word_result)
    result.append(line_result)
print(" ".join(result))


