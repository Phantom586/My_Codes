s = input()
c = 0
str = list("abcdefghijklmnopqrstuvwxyz")
for i in str:
    if i in s:
        c += 1
    elif i.upper() in s:
        c += 1
if c == 26:
    print("pangram")
else:
    print("not pangram")