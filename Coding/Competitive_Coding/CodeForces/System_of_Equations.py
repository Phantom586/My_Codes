# Furik loves math lessons very much, so he doesn't attend them, unlike Rubik. But now Furik wants to get a good mark
# for math. For that Ms. Ivanova, his math teacher, gave him a new task. Furik solved the task immediately. Can you?

# You are given a system of equations:


# You should count, how many there are pairs of integers (a, b) (0 ≤ a, b) which satisfy the system.

# Input
# A single line contains two integers n, m (1 ≤ n, m ≤ 1000) — the parameters of the system. The numbers on the line a
# re separated by a space.

# Output
# On a single line print the answer to the problem.

# Examples
# input
#   9 3
# output
#   1
# input
#   14 28
# output
#   1
# input
#   4 20
# output
#   0
# Note
# In the first sample the suitable pair is integers (3, 0). In the second sample the suitable pair is integers (3, 5).
# In the third sample there is no suitable pair.

n, m = map(int, input().split())
c = 0
for i in range(n):  # Brute Forcing on all the possible combinations that can satisfy the given eqn's.
    for j in range(m):
        if ((i*i) + j) == n and (i + (j*j)) == m:
            c += 1
        if (n*n) == n and n == m:
            c += 1
        if m == n and (m*m) == m:
            c += 1
print(c)

