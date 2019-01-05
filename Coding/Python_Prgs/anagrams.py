def anagram(s):
    l = len(s)
    k = int(l / 2)
    if l % 2 == 0:
        c = 0
        a1 = list(s[0:k])
        b1 = list(s[k:])
        p2 = b1.copy()
        for i in a1:
            if i in p2:
                p2.pop(p2.index(i))
            else:
                c += 1
        return c
    else:
        return -1

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)
        print(result)
