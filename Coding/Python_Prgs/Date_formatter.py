# Takes Differently formatted Dates and prints out it in a Standard Format.
import re

date = re.compile(r'''(
        ( 
        ((\d|\d{2})+(-|/)+(\d|\d{2})+(-|/)+(\d{4})+) | ((\d{4})+(-|/)+(\d|\d{2})+(-|/)+(\d|\d{2})+)
        )
        )''', re.VERBOSE)

str = input("Enter the Date or String of Dates in [DD-MM-YYYY] or [YYYY-MM-DD].\n-->")
inp_dates = []
oup_dates = []
# print(date.match(str))
for g in date.finditer(str):
    item = g.group()
    if '-' in item:
        d = item.split('-')
    elif '/' in item:
        d = item.split('/')
    inp_dates.append(d)

for d in inp_dates:
    if len(d[2]) == 4:
        d[0], d[1], d[2] = d[2], d[1], d[0]
    oup_dates.append('-'.join(d))

str = ''
for i in oup_dates:
    str += i + '\n' 

print("The Standard Formatted String of Dates [MM-DD-YYYY] is -----> ")
print(str)