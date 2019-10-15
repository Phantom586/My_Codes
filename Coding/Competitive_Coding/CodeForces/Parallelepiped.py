# You've got a rectangular parallelepiped with integer edge lengths. You know the areas of its three faces that have
# a common vertex. Your task is to find the sum of lengths of all 12 edges of this parallelepiped.

# Input
# The first and the single line contains three space-separated integers — the areas of the parallelepiped's faces.
# The area's values are positive ( > 0) and do not exceed 104. It is guaranteed that there exists at least one
# parallelepiped that satisfies the problem statement.

# Output
# Print a single number — the sum of all edges of the parallelepiped.

# Examples
# inputCopy
#   1 1 1
# outputCopy
#   12
# inputCopy
#   4 6 6
# outputCopy
#   28
# Note
# In the first sample the parallelepiped has sizes 1 × 1 × 1, in the second one — 2 × 2 × 3.

from math import sqrt
lst = list(map(int, input().split()))
a = sqrt((lst[0]*lst[2])/lst[1])
b = sqrt((lst[0]*lst[1])/lst[2])
c = sqrt((lst[1]*lst[2])/lst[0])
print(int(4*(a+b+c)))
