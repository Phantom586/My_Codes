# a regex that matches a number with commas for every three digits
# Ex : 
# • '42', 
# • '1,234',
# • '6,368,745'
# but not the following:
# • '12,34,567' (which has only two digits between the commas)
# • '1234' (which lacks commas)
import re

# RE to match sequence of numbers containing pattern '1,234,454', '1,234,456,676'
pattern = re.compile(r'(\d|\d{2})?((,)+(\d{3}))*')

def match_sequence(str):
    m = pattern.match(str)
    print(m.group())

if __name__ == "__main__":
    str = input("Enter a Sequence of Numbers :\n")
    match_sequence(str)