from collections import Counter

X = int(input())
sizes = list(map(int, input().split()))
N = int(input())
tot = 0
stock = Counter(sizes)
for _ in range(N):
    a, b = list(map(int, input().split()))
    if stock.get(a) is not None and stock.get(a) != 0:
        tot += b
        stock[a] -= 1
print(tot)