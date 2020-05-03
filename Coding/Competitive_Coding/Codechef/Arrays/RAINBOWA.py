# Chef likes all arrays equally. But he likes some arrays more equally than others. In particular, he loves Rainbow
# Arrays.

# An array is Rainbow if it has the following structure:

# First a1 elements equal 1.
# Next a2 elements equal 2.
# Next a3 elements equal 3.
# Next a4 elements equal 4.
# Next a5 elements equal 5.
# Next a6 elements equal 6.
# Next a7 elements equal 7.
# Next a6 elements equal 6.
# Next a5 elements equal 5.
# Next a4 elements equal 4.
# Next a3 elements equal 3.
# Next a2 elements equal 2.
# Next a1 elements equal 1.
# ai can be any non-zero positive integer.
# There are no other elements in array.
#
# Help Chef in finding out if the given array is a Rainbow Array or not.
#
# Input
# The first line of the input contains an integer T denoting the number of test cases.
# The first line of each test case contains an integer N, denoting the number of elements in the given array.
# The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of array.
# Output
# For each test case, output a line containing "yes" or "no" (without quotes) corresponding to the case if the array is
# rainbow array or not.

# Example
# Input
# 3
# 19
# 1 2 3 4 4 5 6 6 6 7 6 6 6 5 4 4 3 2 1
# 14
# 1 2 3 4 5 6 7 6 5 4 3 2 1 1
# 13
# 1 2 3 4 5 6 8 6 5 4 3 2 1
#
# Output
# yes
# no
# no

# Solution : Thinking Process
# we just have to keep adding elements smartly to the check list but we can't use set() as it'll distort the sequence of
# the given list, so check for the elements in the list if it already exists in the list then don't append the element
# if it doesn't then append, and to append the elements after 7 as they're already present in the list , what we have to
# do is, simply put a check in elif that if the current element is not equal to the last element we've appended in the
# list, then append that element in the list.

t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    check = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
    tmp = []
    if lst == lst[::-1]:
        for i in lst:
            if i not in tmp:
                tmp.append(i)
            elif tmp[-1] is not i:
                tmp.append(i)
        if tmp == check:
            print("yes")
        else:
            print("no")
    else:
        print("no")
