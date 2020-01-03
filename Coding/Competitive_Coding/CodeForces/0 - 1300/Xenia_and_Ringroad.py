# Xenia lives in a city that has n houses built along the main ringroad. The ringroad houses are numbered 1 through n in
# the clockwise order. The ringroad traffic is one way and also is clockwise.

# Xenia has recently moved into the ringroad house number 1. As a result, she's got m things to do. In order to complete
# the i-th task, she needs to be in the house number ai and complete all tasks with numbers less than i. Initially,
# Xenia is in the house number 1, find the minimum time she needs to complete all her tasks if moving from a house to a
# neighboring one along the ringroad takes one unit of time.

# Input
# The first line contains two integers n and m (2 ≤ n ≤ 105, 1 ≤ m ≤ 105). The second line contains m integers a1, a2, 
# ..., am (1 ≤ ai ≤ n). Note that Xenia can have multiple consecutive tasks in one house.

# Output
# Print a single integer — the time Xenia needs to complete all tasks.

# Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is preferred to use the cin, cout
# streams or the %I64d specifier.

# Examples
# input
#   4 3
#   3 2 3
# output
#   6
# input
#   4 3
#   2 3 3
# output
#   2
# Note
# In the first test example the sequence of Xenia's moves along the ringroad looks as follows: 1 → 2 → 3 → 4 → 1 → 2 → 3
# . This is optimal sequence. So, she needs 6 time units.

# in this we have to focus only on this... we are initially at 1st position. and we have been given array of house no.'s
# ex : 2 3 3, all we have to do is to calculate the time consumed to traverse through all the house no's from initial
# position house 1, given in the array in circular fashion.

# for ex : 3 2 3 is given to us and total 4 houses:
# then we start from house 1 :-
# 1 -> 2 -> 3 (time consumed = 2 units) , now we have to go to house 2 so,
# 3 -> 4 -> 1 (time consumed = 2 units)
# 1 -> 2 (time consumed = 1 units)
# 2 -> 3 (time consumed = 1 unit) total time consumed = 6 units.

n, m = map(int, input().split())
a = list(map(int, input().split()))
sm = 0
sm += (a[0] - 1)
for i in range(m-1):
    if a[i+1] < a[i]:
        sm += (n - a[i] + 1)
        sm += (a[i+1] - 1)
    else:
        sm += (a[i+1] - a[i])
print(sm)


