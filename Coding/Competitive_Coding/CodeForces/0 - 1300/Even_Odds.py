# Being a nonconformist, Volodya is displeased with the current state of things, particularly with the order of natural
# numbers (natural number is positive integer number). He is determined to rearrange them. But there are too many
# natural numbers, so Volodya decided to start with the first n. He writes down the following sequence of numbers:
# firstly all odd integers from 1 to n (in ascending order), then all even integers from 1 to n
# (also in ascending order). Help our hero to find out which number will stand at the position number k.

# Input
# The only line of input contains integers n and k (1 ≤ k ≤ n ≤ 1012).

# Please, do not use the %lld specifier to read or write 64-bit integers in C++. It is preferred to use the cin, cout
# streams or the %I64d specifier.

# Output
# Print the number that will stand at the position number k after Volodya's manipulations.

# Examples
# input
#   10 3
# output
#   5
# input
#   7 7
# output
#   6
# Note
#   In the first sample Volodya's sequence will look like this: {1, 3, 5, 7, 9, 2, 4, 6, 8, 10}. The third place in the
#   sequence is therefore occupied by the number 5.


n, k = map(int, input().split())
if n % 2 == 0:  # using the concept of A.P(Arithmetic Progression, with same difference)
    if k <= n/2:
        s = 1 + (k - 1) * 2  # a = 1, as 1st element in odd no.'s will always be 1
        print(int(s))
    else:
        s = 2 + (k - (n/2) - 1) * 2  # a = 2, as 1st element in even no.'s will always be 2, and k - (n/2)
        # as to select only the even series
        print(int(s))
else:
    if k <= ((n/2) + 1):
        s = 1 + (k - 1) * 2  # a = 1, as 1st element in odd no.'s will always be 1
        print(int(s))
    else:
        s = 2 + (k - (int(n/2) + 1) - 1) * 2  # a = 2, as 1st element in even no.'s will always be 2, and k - ((n/2)+1)
        # as to select only the even series
        print(int(s))
