# Takes Differently formatted Dates and prints out it in a Standard Format.
import re

# Regular Expression for Matching Date Formats Like : DD(-/)MM(-/)YYYY or YYYY(-/)MM(-/)DD
date = re.compile(r'''(
        ( 
        ((\d|\d{2})+(-|/)+(\d|\d{2})+(-|/)+(\d{4})+) | ((\d{4})+(-|/)+(\d|\d{2})+(-|/)+(\d|\d{2})+)
        )
        )''', re.VERBOSE)

str = input("Enter the Date or String of Dates in [DD-MM-YYYY] or [YYYY-MM-DD].\n-->")
inp_dates = []  # list for dates matched from the regular expression.
oup_dates = []  # list for the dates Reformatted in Standard  Format.

# loop to find the matches in string 'str' and then split them according to their respective delimiters '-' or '/'
# then append into the 'inp_dates' list.
for g in date.finditer(str):
    item = g.group()
    if '-' in item:
        d = item.split('-')
    elif '/' in item:
        d = item.split('/')
    inp_dates.append(d)

# loop to change the Dates to standard Format.
for d in inp_dates:
    if len(d[2]) == 4:
        d[0], d[1], d[2] = d[2], d[1], d[0]
    oup_dates.append('-'.join(d))

# Generating a string of Standard Formatted Dates.
# then append to the 'oup_dates' list.
str = ''
for i in oup_dates:
    str += i + '\n' 

print("The Standard Formatted String of Dates [MM-DD-YYYY] is -----> ")
print(str)