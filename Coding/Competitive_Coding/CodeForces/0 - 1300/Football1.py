# Petya loves football very much. One day, as he was watching a football match, he was writing the players' current
# positions on a piece of paper. To simplify the situation he depicted it as a string consisting of zeroes and ones. A
# zero corresponds to players of one team; a one corresponds to players of another team. If there are at least 7 players
# of some team standing one after another, then the situation is considered dangerous. For example, the situation
# 00100110111111101 is dangerous and 11110111011101 is not. You are given the current situation. Determine whether it is
# dangerous or not.

# Input
# The first input line contains a non-empty string consisting of characters "0" and "1", which represents players. The
# length of the string does not exceed 100 characters. There's at least one player from each team present on the field.

# Output
# Print "YES" if the situation is dangerous. Otherwise, print "NO".

# Examples
# input
#   001001
# output
#   NO
# input
#   1000000001
# output
#   YES

p = input()
d = p[0]  # assigned p's first character to d
c = 1
chk = []
for i in range(1, len(p)):
    if p[i] == d:  # now checking if the next character is same as d or not if yes then increase c.
        c += 1
    else:  # otherwise assign p[i] to d and reset c to 1
        d = p[i]
        c = 1
    chk.append(c)  # append result of c in chk, as c will be reset and its value will be lost
if 7 in chk:
    print("YES")
else:
    print("NO")
