
n, knapsackWeight = map(int, input().split())
values = list(map(int, input().split()))
weights = list(map(int, input().split()))

profitByWeight = []
for i in range(n):
    profitByWeight.append(values[i]/weights[i])

profitByWeight.sort()
currentWeight = 0
max_profit = 0

for i in range(n):
    pass


print(currentWeight, max_profit)