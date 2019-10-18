# n soldiers stand in a circle. For each soldier his height ai is known. A reconnaissance unit can be made of such two
# neighbouring soldiers, whose heights difference is minimal, i.e. |ai - aj| is minimal. So each of them will be less
# noticeable with the other. Output any pair of soldiers that can form a reconnaissance unit.

# Input
# The first line contains integer n (2 ≤ n ≤ 100) — amount of soldiers. Then follow the heights of the soldiers in their
# order in the circle — n space-separated integers a1, a2, ..., an (1 ≤ ai ≤ 1000). The soldier heights are given in
# clockwise or counterclockwise direction.

# Output
# Output two integers — indexes of neighbouring soldiers, who should form a reconnaissance unit. If there are many
# optimum solutions, output any of them. Remember, that the soldiers stand in a circle.

# Examples
# input
#   5
#   10 12 13 15 10
# output
#   5 1
#   input
#   4
#   10 20 30 40
# output
#   1 2

n = int(input())
lst = list(map(int, input().split()))
mn = abs(lst[1] - lst[0])
sol = [1, 2]
for i in range(2, len(lst)):
    tmp = abs(lst[i] - lst[i-1])
    if tmp < mn:
        sol[0] = i
        sol[1] = i + 1
        mn = tmp
if abs(lst[-1] - lst[0]) < mn:
    sol[0] = n
    sol[1] = 1
print(sol[0], sol[1])
