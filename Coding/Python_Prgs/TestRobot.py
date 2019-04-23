# TSTROBOT

t = int(input())
for _ in range(t):
    n, x = list(map(int, input().split()))
    str = input()
    c = [x]
    for i in str:
        if i == 'L':
            x += 1
        elif i == 'R':
            x -= 1
        c.append(x)
    print(len(set(c)))