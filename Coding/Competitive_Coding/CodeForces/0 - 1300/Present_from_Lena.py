# Vasya's birthday is approaching and Lena decided to sew a patterned handkerchief to him as a present. Lena chose
# digits from 0 to n as the pattern. The digits will form a rhombus. The largest digit n should be located in the
# centre. The digits should decrease as they approach the edges. For example, for n = 5 the handkerchief pattern should
# look like that:


#           0
#         0 1 0
#       0 1 2 1 0
#     0 1 2 3 2 1 0
#   0 1 2 3 4 3 2 1 0
# 0 1 2 3 4 5 4 3 2 1 0
#   0 1 2 3 4 3 2 1 0
#     0 1 2 3 2 1 0
#       0 1 2 1 0
#         0 1 0
#           0
# Your task is to determine the way the handkerchief will look like by the given n.

# Input
# The first line contains the single integer n (2 ≤ n ≤ 9).

# Output
# Print a picture for the given n. You should strictly observe the number of spaces before the first digit on each line.
# Every two adjacent digits in the same line should be separated by exactly one space. There should be no spaces after
# the last digit at the end of each line.

# Examples
# input
#   2
# output
#         0
#       0 1 0
#     0 1 2 1 0
#       0 1 0
#         0
# input
#   3
# output
#           0
#         0 1 0
#       0 1 2 1 0
#     0 1 2 3 2 1 0
#       0 1 2 1 0
#         0 1 0
#           0

n = int(input())


# function to return a string that consists of :
# 1 - string of no's in decreasing order from na .... Ex : for {na = 3, "0 1 2"}
# store each no. that is converted to string in list l
# concat the string with na, i.e., Ex: {"0 1 2 3"}
# 2 - then just reverse the list l ,and concat with string resulted in step 1, i.e., Ex: {for na = 3, "0 1 2 3 2 1 0"}
def cus_fact(na):
    l = []
    sr = ""
    for j in range(na):
        sr += str(j) + " "
        l.append(str(j))
    if n >= 1:
        sr += str(na)
        sr += " " + ' '.join(l[::-1])
    # print("S : ", s)
    sr = sr.rstrip()
    return sr


# list to store the resulting string from cust_fact function
lst = []
# loop to generate the unique strings in the pattern and store them in lst and print required spaces and also print the
# resulting string
for i in range(n+1):
    s = cus_fact(i)
    print(" "*(n-i)*2, end="")
    print(s)
    lst.append(s)
# loop to print required spaces and print the rest of the pattern that is already stored in the lst, just in reverse
# order
for i in range(n-1, -1, -1):
    print(" "*(n-i)*2, end="")
    print(lst[i])


