# Little chief has his own restaurant in the city. There are N workers there. Each worker has his own salary. The salary
# of the i-th worker equals to Wi (i = 1, 2, ..., N). Once, chief decided to equalize all workers, that is, he wants to
# make salaries of all workers to be equal. But for this goal he can use only one operation: choose some worker and
# increase by 1 salary of each worker, except the salary of the chosen worker. In other words, the chosen worker is the
# loser, who will be the only worker, whose salary will be not increased during this particular operation. But
# loser-worker can be different for different operations, of course. Chief can use this operation as many times as he
# wants. But he is a busy man. That's why he wants to minimize the total number of operations needed to equalize all
# workers. Your task is to find this number.

# Input
# The first line of the input contains an integer T denoting the number of test cases. The description of T test cases
# follows. The first line of each test case contains a single integer N denoting the number of workers. The second line
# contains N space-separated integers W1, W2, ..., WN denoting the salaries of the workers.

# Output
# For each test case, output a single line containing the minimum number of operations needed to equalize all workers.

# Input:
# 2
# 3
# 1 2 3
# 2
# 42 42
#
# Output:
# 3
# 0

t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    print(sum(lst) - min(lst)*n)
