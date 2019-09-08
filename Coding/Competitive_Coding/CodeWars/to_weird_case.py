# Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all,
# even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased.
# The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.


# The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if,
# there are multiple words. Words will be separated by a single space(' ').

# Examples:
# to_weird_case('String'); # => returns 'StRiNg'
# to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'

# def to_weird_case(string):
#     b = [list(i) for i in string.split()]
#     str = ''
#     for i in range(len(b)):
#         for j, c in enumerate(b[i]):
#             if j % 2 == 0:
#                 b[i][j] = c.upper()
#             else:
#                 b[i][j] = c.lower()
#         str += ''.join(b[i]) + ' '
#     print(str.strip())

# Improved Solution

def to_weird_case_word(string):
    return "".join(c.upper() if i % 2 == 0 else c for i, c in enumerate(string.lower()))


def to_weird_case(string):
    print(" ".join(to_weird_case_word(str) for str in string.split()))


to_weird_case('This')
to_weird_case('is')
to_weird_case('This is a test')