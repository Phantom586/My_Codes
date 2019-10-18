# Once Bob got to a sale of old TV sets. There were n TV sets at that sale. TV set with index i costs ai bellars.
# Some TV sets have a negative price — their owners are ready to pay Bob if he buys their useless apparatus. Bob can
# «buy» any TV sets he wants. Though he's very strong, Bob can carry at most m TV sets, and he has no desire to go to
# the sale for the second time. Please, help Bob find out the maximum sum of money that he can earn.

# Input
# The first line contains two space-separated integers n and m (1 ≤ m ≤ n ≤ 100) — amount of TV sets at the sale, and
# amount of TV sets that Bob can carry. The following line contains n space-separated integers ai ( - 1000 ≤ ai ≤ 1000)
# — prices of the TV sets.

# Output
# Output the only number — the maximum sum of money that Bob can earn, given that he can carry at most m TV sets.

# Examples
# input
#   5 3
#   -6 0 35 -2 4
# output
#   8
# input
#   4 2
#   7 0 0 -7
# output
#   7

n, m = map(int, input().split())
lst = list(map(int, input().split()))
neg_list = []
for i in lst:
    if i < 0:  # checking for (-)ve elements and adding them to neg_list.
        neg_list.append(i)
neg_list.sort()  # sorting the neg_list in-order to obtain the maximum cost first in the list.
print(abs(sum(neg_list[0:m])))  # printing the (+)ve sum of the m elements from the neg_list.

