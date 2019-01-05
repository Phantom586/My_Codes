
def marsExploration(s):
    k = int(len(s)/3)
    msg = []
    chk = list("SOS")
    l = 0
    r = 3
    c = 0
    for i in range(k):
        msg.append(s[l:r])
        l += 3
        r += 3
    print(msg)
    for i in msg:
        ch = chk.copy()
        for j in list(i):
            if ch.pop() != j:
                c += 1
    return c



if __name__ == '__main__':

    s = input()

    result = marsExploration(s)

    print(result)