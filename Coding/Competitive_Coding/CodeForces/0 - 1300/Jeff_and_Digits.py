# Jeff's got n cards, each card contains either digit 0, or digit 5. Jeff can choose several cards and put them in a
# line so that he gets some number. What is the largest possible number divisible by 90 Jeff can make from the cards
# he's got?

# Jeff must make the number without leading zero. At that, we assume that number 0 doesn't contain any leading zeroes.
# Jeff doesn't have to use all the cards.

# Input
# The first line contains integer n (1 ≤ n ≤ 103). The next line contains n integers a1, a2, ..., an (ai = 0 or ai = 5).
# Number ai represents the digit that is written on the i-th card.

# Output
# In a single line print the answer to the problem — the maximum number, divisible by 90. If you can't make any
# divisible by 90 number from the cards, print -1.

# Examples
# inputCopy
#   4
#   5 0 5 0
# outputCopy
#   0
# inputCopy
#   11
#   5 5 5 5 5 5 5 5 0 5 5
# outputCopy
#   5555555550
# Note#
# In the first test you can make only one number that is a multiple of 90 — 0.

# In the second test you can make number 5555555550, it is a multiple of 90.

# Help :-
# Solution is looking for few cases:
# 1. If we do not have zeros, then the answer is -1.
# 2. If we have less than 9 fives, then the answer is 0.
# 3. Otherwise, the answer is:
# 4. 1. The maximum number of fives divisible by 9
# 4. 2. All zeros, we have

n = int(input())
lst = list(map(int, input().split()))
z = 0
five = 0
for i in lst:
    if i == 0:
        z += 1
    elif i == 5:
        five += 1
if z == 0:
    print(-1)
elif five < 9:
    print(0)
else:
    i = 9
    j = 0
    tmp = "5" * i + "0" * z
    while i <= five:
        tmp = "5" * i + "0" * z
        if int(tmp) % 90 == 0:
            j = i
        i += 1
    print("5" * j + "0" * z)
