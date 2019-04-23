# The time out error was because you weren't explicitly making A and B as sets.
# The inputs have duplicate values in A and B and we need to remove them.

if __name__ == '__main__':
    happiness = 0
    n, m = (int(i) for i in input().split())
    arr = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    for i in arr:
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1
    print(happiness)