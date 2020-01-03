# Pashmak decided to give Parmida a pair of flowers from the garden. There are n flowers in the garden and the i-th of
# them has a beauty number bi. Parmida is a very strange girl so she doesn't want to have the two most beautiful flowers
# necessarily. She wants to have those pairs of flowers that their beauty difference is maximal possible!

# Your task is to write a program which calculates two things:

# The maximum beauty difference of flowers that Pashmak can give to Parmida.
# The number of ways that Pashmak can pick the flowers. Two ways are considered different if and only if there is at
# least one flower that is chosen in the first way and not chosen in the second way.
# Input
# The first line of the input contains n (2 ≤ n ≤ 2·105). In the next line there are n space-separated integers b1, b2,
# ..., bn (1 ≤ bi ≤ 109).
#
# Output
# The only line of output should contain two integers. The maximum beauty difference and the number of ways this may
# happen, respectively.
#
# Examples
# inputCopy
# 2
# 1 2
# outputCopy
# 1 1
# inputCopy
# 3
# 1 4 5
# outputCopy
# 4 1
# inputCopy
# 5
# 3 1 2 3 1
# outputCopy
# 2 4
# Note
# In the third sample the maximum beauty difference is 2 and there are 4 ways to do this:
#
# choosing the first and the second flowers;
# choosing the first and the fifth flowers;
# choosing the fourth and the second flowers;
# choosing the fourth and the fifth flowers.

n = int(input())
lst = list(map(int, input().split()))