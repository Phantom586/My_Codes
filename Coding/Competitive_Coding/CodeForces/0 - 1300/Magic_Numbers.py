# A magic number is a number formed by concatenation of numbers 1, 14 and 144. We can use each of these numbers any
# number of times. Therefore 14144, 141414 and 1411 are magic numbers but 1444, 514 and 414 are not.

# You're given a number. Determine if it is a magic number or not.

# Input
# The first line of input contains an integer n, (1 ≤ n ≤ 109). This number doesn't contain leading zeros.

# Output
# Print "YES" if n is a magic number or print "NO" if it's not.

# Examples
# input
#   114114
# output
#   YES
# input
#   1111
# output
#   YES
# input
#   441231
# output
#   NO

n = input()
i = 0
flag = 1
while i < len(n):
    if n[i] == '1':
        if n[i:i+3] == '144':
            i += 3
        elif n[i:i+2] == '14':
            i += 2
        else:
            i += 1
    else:
        i += 1
        flag = 0
if flag:
    print("YES")
else:
    print("NO")