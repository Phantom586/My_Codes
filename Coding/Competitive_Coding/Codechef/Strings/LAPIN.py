# Lapindromes

# Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same
# frequency of each character. If there are odd number of characters in the string, we ignore the middle character and

#
# Input:
# First line of input contains a single integer T, the number of test cases.
# Each test is a single line containing a string S composed of only lowercase English alphabet.
# Output:
# For each test case, output on a separate line: "YES" if the string is a lapindrome and "NO" if it is not.
# Constraints:
# 1 ≤ T ≤ 100
# 2 ≤ |S| ≤ 1000, where |S| denotes the length of S
# Example:
# Input:
# 6
# gaga
# abcde
# rotor
# xyzxy
# abbaab
# ababc
#
#
# Output:
# YES
# NO
# YES
# YES
# NO
# NO

t = int(input())
for _ in range(t):
    st = input()
    l = int(len(st)/2)
    s1 = st[0: l]
    if len(st) % 2 is not 0:
        s2 = st[l+1:]
    else:
        s2 = st[l:]
    flag = 1
    for i in set(s1):
        if s1.count(i) is not s2.count(i):
            flag = 0
            break
    if flag:
        print("YES")
    else:
        print("NO")