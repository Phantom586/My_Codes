# Complete the solve function below.

s = input()
res = []
sl = s.split(' ')
for sle in sl:
    if len(sle) == 0:
      res.append('')
    else:
      res.append(sle[0].upper() + sle[1:])
print(' '.join(res))
