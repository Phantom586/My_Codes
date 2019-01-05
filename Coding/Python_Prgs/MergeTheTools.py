string = input()
k = int(input())

n = len(string)
s = int(n/k)
str = []
j = 0
l = k
print(n)
for i in range(k):
    str.append(set(string[j:l]))
    j += k
    l += k
for i in str:
    print(''.join(i))