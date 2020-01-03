# A string is called a k-string if it can be represented as k concatenated copies of some string. For example, the
# string "aabaabaabaab" is at the same time a 1-string, a 2-string and a 4-string, but it is not a 3-string, a 5-string,
# or a 6-string and so on. Obviously any string is a 1-string.

# You are given a string s, consisting of lowercase English letters and a positive integer k. Your task is to reorder
# the letters in the string s in such a way that the resulting string is a k-string.

# Input
# The first input line contains integer k (1 ≤ k ≤ 1000). The second line contains s, all characters in s are lowercase
# English letters. The string length s satisfies the inequality 1 ≤ |s| ≤ 1000, where |s| is the length of string s.

# Output
# Rearrange the letters in string s in such a way that the result is a k-string. Print the result on a single output
# line. If there are multiple solutions, print any of them.

# If the solution doesn't exist, print "-1" (without quotes).

# Examples
# input
#   2
#   aazz
# output
#   azaz
# input
#   3
#   abcabcabz
# output
#   -1

# Little Help for the Solution
# Count the occurrences of each character. If any character appears a number of times not divisible by K, obviously,
# there is no solution. Otherwise, form the solution by first making the string B. The string B can be any string with
# the following property: if some character ch appears q times in the string B, the same character appears q***K** times
# in the given string. Now, just print that string K times.


k = int(input())
st = input()
flag = 1
for i in set(st):
    if st.count(i) % k != 0:
        flag = 0
if flag:
    s = ""
    for i in set(st):
        a = st.count(i) // k
        s += i * a
    print(s*k)
else:
    print(-1)
