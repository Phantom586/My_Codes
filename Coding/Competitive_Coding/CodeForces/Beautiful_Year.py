# It seems like the year of 2013 came only yesterday. Do you know a curious fact? The year of 2013 is the first year
# after the old 1987 with only distinct digits.

# Now you are suggested to solve the following problem: given a year number, find the minimum year number which is
# strictly larger than the given one and has only distinct digits.

# Input
# The single line contains integer y (1000 ≤ y ≤ 9000) — the year number.

# Output
# Print a single integer — the minimum year number that is strictly larger than y and all it's digits are distinct.
# It is guaranteed that the answer exists.

# Examples
# input
#   1987
# output
#   2013
# input
#   2013
# output
#   2014


year = list(map(int, input()))
f = 1
for i in range(len(year)):
    c = year.count(i)
    if c > 1:
        f = 0
        c = year.index(i, year.index(i)+1)
        year[c] += 1
if f:
    year[3] += 1
print(''.join(map(str, year)))
