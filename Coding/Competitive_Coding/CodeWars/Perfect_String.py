
def check_substr(ch, str):
    print(str)
    d = {"x": [], "y": []}
    c = 1
    for i in range(1, len(str)):
        if str[i-1] == str[i]:
            c += 1
        else:
            d[str[i-1]].append(c)
            c = 1
    d[str[i]].append(c)
    print(d[ch])
    return max(d[ch])


def Perfect_String(str, a):
    chk = []
    chk.append(check_substr("x", str))
    chk.append(check_substr("y", str))
    for i in range(a):
        chk.append(check_substr("x", str.replace('x', 'y', i+1)))
        chk.append(check_substr("y", str.replace('y', 'x', i+1)))
    for j in range(a):
        chk.append(check_substr("y", str.replace('y', 'x', j+1)))
        chk.append(check_substr("x", str.replace('y', 'x', j+1)))
    print(max(chk))


# Perfect_String("xyxxyxyy", 2)
Perfect_String("yxyxxyx", 3)
