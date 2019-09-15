n = int(input())
drinks = list(map(int, input().split()))
frac = 0.0
for i in drinks:
    frac += i/100
print((frac/n)*100)