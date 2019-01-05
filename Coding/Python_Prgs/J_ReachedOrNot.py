def SafeReached(base, coor, str, j):
    x = 0
    y = 0
    for i in str:
        if i == 'L':
            x -= 1
        elif i == 'R':
            x += 1
        elif i == 'U':
            y += 1
        elif i == 'D':
            y -= 1
    if x==int(coor[0]) and y==int(coor[1]):
        print("Case",j,": REACHED")
    elif (x > int(base[0]) or x < 0) or (y > int(base[1]) or y < 0):
        print("Case",j,": DANGER")
    else:
        print("Case",j,": SOMEWHERE")

if __name__ == '__main__':
    q = int(input())
    j = 1
    for q_itr in range(q):
        base = list(input().split(' '))
        coor = list(input().split(' '))
        n = int(input())
        str = input()
        SafeReached(base, coor, str, j)
        j += 1