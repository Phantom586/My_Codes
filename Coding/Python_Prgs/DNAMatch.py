s1 = list(input())
s2 = list(input())
c = 0
l = len(s1)
for i in range(l):
    if s1.pop() == s2.pop():
        c += 1
print("{}/{}".format(c,l))