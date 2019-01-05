def alternatingCharacters(s):
    str = list(s)
    c = 0
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            c += 1
    return c

if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        print(result)
