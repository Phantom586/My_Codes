from math import sqrt
a, b = map(int, input().split())


def is_prime(n):
    c = 0
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            c += 1
    if c == 0:
        return True
    else:
        return False


if is_prime(b):
    if (b-a) % 2 == 0:
        if (b-a) > 2:
            flags = []
            temp = a
            for i in range((int((b-a)/2)) - 1):
                temp += 2
                flags.append(is_prime(temp))
            if True in flags:
                print("NO")
            else:
                print("YES")
        else:
            print("YES")
    elif a == 2 and (b-a) == 1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")