def funnyString(s):
    a = []
    r = []
    resa = []
    resb = []
    for i in s:
        a.append(ord(i))
    for i in s[::-1]:
        r.append(ord(i))
    for i in range(len(a)-1):
        resa.append(abs(a[i] - a[i+1]))
        resb.append(abs(r[i] - r[i+1]))
    if resa == resb:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()
        result = funnyString(s)
        print(result)