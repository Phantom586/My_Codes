# The Little Elephant loves Ukraine very much. Most of all he loves town Rozdol (ukr. "Rozdil").

# However, Rozdil is dangerous to settle, so the Little Elephant wants to go to some other town. The Little Elephant
# doesn't like to spend much time on travelling, so for his journey he will choose a town that needs minimum time to
# travel to. If there are multiple such cities, then the Little Elephant won't go anywhere.

# For each town except for Rozdil you know the time needed to travel to this town. Find the town the Little Elephant
# will go to or print "Still Rozdil", if he stays in Rozdil.

# Input
# The first line contains a single integer n (1 ≤ n ≤ 105) — the number of cities. The next line contains n integers,
# separated by single spaces: the i-th integer represents the time needed to go from town Rozdil to the i-th town.
# The time values are positive integers, not exceeding 109.

# You can consider the cities numbered from 1 to n, inclusive. Rozdil is not among the numbered cities.

# Output
# Print the answer on a single line — the number of the town the Little Elephant will go to. If there are multiple
# cities with minimum travel time, print "Still Rozdil" (without the quotes).

# Examples
# inputCopy
#   2
#   7 4
# outputCopy
#   2
# inputCopy
#   7
#   7 4 47 100 4 9 12
# outputCopy
#   Still Rozdil
# Note
# In the first sample there are only two cities where the Little Elephant can go. The travel time for the first town
# equals 7, to the second one — 4. The town which is closest to Rodzil (the only one) is the second one, so the answer
# is 2.

# In the second sample the closest cities are cities two and five, the travelling time to both of them equals 4, so
# the answer is "Still Rozdil".

n = int(input())
lst = list(map(int, input().split()))
mn = []
tmp = [lst[0], 0]
flag = 0

for i in range(1, len(lst)):
    if lst[i] in mn:
        flag = 1
        break
    elif lst[i] < tmp[0]:
        mn.append(lst[i])
        tmp[0] = lst[i]
        tmp[1] = i+1

if flag:
    print("Still Rozdil")
else:
    print(tmp[1])
