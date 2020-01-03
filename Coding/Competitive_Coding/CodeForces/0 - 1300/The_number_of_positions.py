# Petr stands in line of n people, but he doesn't know exactly which position he occupies. He can say that there are no
# less than a people standing in front of him and no more than b people standing behind him. Find the number of
# different positions Petr can occupy.

# Input
# The only line contains three integers n, a and b (0 ≤ a, b < n ≤ 100).

# Output
# Print the single number — the number of the sought positions.

# Examples
# input
#   3 1 1
# output
#   2
# input
#   5 2 3
# output
#   3
# Note
# The possible positions in the first sample are: 2 and 3 (if we number the positions starting with 1).

# In the second sample they are 3, 4 and 5.

# Help
# Let's iterate through the each item and check whether it is appropriate to the conditions a ≤ i - 1 and n - i ≤ b
# (for i from 1 to n). The first condition can be converted into a + 1 ≤ i, and the condition n - i ≤ b in n - b ≤ i,
# then the general condition can be written max(a + 1, n - b) ≤ i and then our answer can be calculated by the formula
# n - max(a + 1, n - b) + 1.


n, a, b = map(int, input().split())
print(n - max(a + 1, n - b) + 1)
