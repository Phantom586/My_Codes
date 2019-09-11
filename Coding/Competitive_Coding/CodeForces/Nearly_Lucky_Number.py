# Petya loves lucky numbers. We all know that lucky numbers are the positive integers whose decimal representations
# contain only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

# Unfortunately, not all numbers are lucky. Petya calls a number nearly lucky if the number of lucky digits in it
# is a lucky number. He wonders whether number n is a nearly lucky number.

#Input
# The only line contains an integer n (1 ≤ n ≤ 1018).

# Please do not use the %lld specificator to read or write 64-bit numbers in С++.
# It is preferred to use the cin, cout streams or the %I64d specificator.

# Output
# Print on the single line "YES" if n is a nearly lucky number. Otherwise, print "NO" (without the quotes).

# Examples
# inputCopy
#   40047
# outputCopy
#   NO
# inputCopy
#   7747774
# outputCopy
#   YES
# inputCopy
#   1000000000000000000
# outputCopy
#   NO
# Note :

# In the first sample there are 3 lucky digits (first one and last two), so the answer is "NO".
# In the second sample there are 7 lucky digits, 7 is lucky number, so the answer is "YES".
# In the third sample there are no lucky digits, so the answer is "NO".

num = list(input())
if '4' in num and '7' in num:
    if (num.count('4') + num.count('7') == 4) or (num.count('4') + num.count('7') == 7):
        print("YES")
    else:
        print("NO")
elif '4' in num or '7' in num:
    if num.count('4') == 4 or num.count('4') == 7:
        print("YES")
    elif num.count('7') == 4 or num.count('7') == 7:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
