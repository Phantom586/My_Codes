# Chef likes to write poetry. Today, he has decided to write a X pages long poetry, but unfortunately his notebook has o
# nly Y pages left in it. Thus he decided to buy a new CHEFMATE notebook and went to the stationary shop. Shopkeeper
# showed him some N notebooks, where the number of pages and price of the ith one are Pi pages and Ci rubles
# respectively. Chef has spent some money preparing for Ksen's birthday, and then he has only K rubles left for now.

# Chef wants to buy a single notebook such that the price of the notebook should not exceed his budget and he is able to
# complete his poetry.

# Help Chef accomplishing this task. You just need to tell him whether he can buy such a notebook or not. Note that Chef
# can use all of the Y pages in the current notebook, and Chef can buy only one notebook because Chef doesn't want to
# use many notebooks.

# Input
# The first line of input contains an integer T, denoting the number of test cases. Then T test cases are follow.

# The first line of each test case contains four space-separated integers X, Y, K and N, described in the statement.
# The ith line of the next N lines contains two space-separated integers Pi and Ci, denoting the number of pages and
# price of the ith notebook respectively.

# Output
# For each test case, Print "LuckyChef" if Chef can select such a notebook, otherwise print "UnluckyChef"
# (quotes for clarity).

# Input
# 3
# 3 1 2 2
# 3 4
# 2 2
# 3 1 2 2
# 2 3
# 2 3
# 3 1 2 2
# 1 1
# 1 2
#
# Output
# LuckyChef
# UnluckyChef
# UnluckyChef

t = int(input())
for _ in range(t):
    x, y, k, n = map(int, input().split())
    lst = []
    flag = 0
    for i in range(n):
        lst.append(list(map(int, input().split())))
    for i in lst:
        if y + i[0] >= x and i[1] <= k:
            flag = 1
            break
        else:
            flag = 0
    if flag:
        print("LuckyChef")
    else:
        print("UnluckyChef")
