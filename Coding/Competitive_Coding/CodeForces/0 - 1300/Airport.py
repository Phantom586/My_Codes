# Lolek and Bolek are about to travel abroad by plane. The local airport has a special "Choose Your Plane" offer. The
# offer's conditions are as follows:

# it is up to a passenger to choose a plane to fly on;
# if the chosen plane has x (x > 0) empty seats at the given moment, then the ticket for such a plane costs x zlotys
# (units of Polish currency).
# The only ticket office of the airport already has a queue of n passengers in front of it. Lolek and Bolek have not
# stood in the queue yet, but they are already wondering what is the maximum and the minimum number of zlotys the
# airport administration can earn if all n passengers buy tickets according to the conditions of this offer?

# The passengers buy tickets in turn, the first person in the queue goes first, then goes the second one, and so on up
# to n-th person.

# Input
# The first line contains two integers n and m (1 ≤ n, m ≤ 1000) — the number of passengers in the queue and the number
# of planes in the airport, correspondingly. The next line contains m integers a1, a2, ..., am (1 ≤ ai ≤ 1000) — ai
# stands for the number of empty seats in the i-th plane before the ticket office starts selling tickets.

# The numbers in the lines are separated by a space. It is guaranteed that there are at least n empty seats in total.

# Output
# Print two integers — the maximum and the minimum number of zlotys that the airport administration can earn,
# correspondingly.

# Examples
# inputCopy
#   4 3
#   2 1 1
# outputCopy
#   5 5
# inputCopy
#   4 3
#   2 2 2
# outputCopy
#   7 6
# Note
# In the first test sample the number of passengers is equal to the number of empty seats, so regardless of the way the
# planes are chosen, the administration will earn the same sum.

# In the second sample the sum is maximized if the 1-st person in the queue buys a ticket to the 1-st plane, the 2-nd
# person — to the 2-nd plane, the 3-rd person — to the 3-rd plane, the 4-th person — to the 1-st plane. The sum is
# minimized if the 1-st person in the queue buys a ticket to the 1-st plane, the 2-nd person — to the 1-st plane, the
# 3-rd person — to the 2-nd plane, the 4-th person — to the 2-nd plane.

# Solution - Though Process

# Calculating Minimum - it is very easy, initially sort the seats in planes list ,then just decrease the value at
# particular index until it becomes zero and simultaneously add it to global min variable, and then move to next index.

# Calculating Maximum - it was a bit tricky for me, but as soon as i realized that after initially sorting the list
# just what we have to do is think to decrease the values in the planes seats list as given below :

# Suppose the list of seats in planes is given as :
# [10, 10, 10, 7, 6, 5, 4, 3, 2, 1], now for maximum we have to find a way to decrease the list as following.
# [9, 10, 10, 7, 6, 5, 4, 3, 2, 1]
# [9, 9, 10, 7, 6, 5, 4, 3, 2, 1]
# [9, 9, 9, 7, 6, 5, 4, 3, 2, 1]
# [8, 9, 9, 7, 6, 5, 4, 3, 2, 1]
# [8, 8, 9, 7, 6, 5, 4, 3, 2, 1]
# [8, 8, 8, 7, 6, 5, 4, 3, 2, 1]
# [7, 8, 8, 7, 6, 5, 4, 3, 2, 1]
# [7, 7, 8, 7, 6, 5, 4, 3, 2, 1]
# [7, 7, 7, 7, 6, 5, 4, 3, 2, 1]
# [6, 7, 7, 7, 6, 5, 4, 3, 2, 1]
# [6, 6, 7, 7, 6, 5, 4, 3, 2, 1]
# [6, 6, 6, 7, 6, 5, 4, 3, 2, 1]
# [6, 6, 6, 6, 6, 5, 4, 3, 2, 1]
# [5, 6, 6, 6, 6, 5, 4, 3, 2, 1], and so on. It will give us the maximum.

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
cst = lst.copy()
mn, mx = 0, 0
i, j = 1, 0
while j < n:
    if cst[(i % m) - 1] != 0:
        mn += cst[(i % m) - 1]
        cst[(i % m) - 1] -= 1
        j += 1
    else:
        i += 1
i, j = 1, 0
cst = lst[::-1]
while j < n:
    index = i
    # print(f'\ni = {i-1}, ({index} >= {cst[index % m]})', end="")
    if cst[(index % m) - 1] != 0 and (cst[(index % m) - 1] >= cst[index % m]):
        if cst[(index % m) - 1] == cst[index % m]:
            # print(" Same neighbour", end="")
            i += 1
        else:
            # print(" Not Same neighbour", end="")
            i = 1
        # print(f' {index} -= {1}')
        mx += cst[(index % m) - 1]
        cst[(index % m) - 1] -= 1
        j += 1
    else:
        # print(' not matched')
        i += 1
    # print(cst, " max : ", mx)
print(mx, mn)
